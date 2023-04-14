meta_dict = {}


def _generate_metaclass(bases, metas, priority):
    t = lambda m: sum([issubclass(M, m) for M in metas], m is type)

    meta_bs = tuple([mb for mb in map(type, bases) if not t(mb)])

    meta_bases = (meta_bs + metas, metas + meta_bs)[priority]

    if meta_bases in meta_dict:
        # already generated metaclass
        return meta_dict[meta_bases]

    elif not meta_bases:
        # trivial metabase
        meta = type

    elif len(meta_bases) == 1:
        # single metabase
        meta = meta_bases[0]

    else:
        # multiple meta_bases
        metaname = "_" + ''.join([m.__name__ for m in meta_bases])
        meta = make_cls()(metaname, meta_bases, {})

    return meta_dict.setdefault(meta_bases, meta)


def make_cls(*metas, **options):
    priority = options.get('priority', False)
    return lambda n, b, d: _generate_metaclass(b, metas, priority)(n, b, d)
