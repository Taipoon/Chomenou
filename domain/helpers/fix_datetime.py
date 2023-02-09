import datetime


class FixDateTime(object):
    def __init__(self):
        self._is_fixed = False
        self._datetime = datetime.datetime.now()

    def fix(self, year: int, month: int, day: int, hour: int, minute: int, second: int):
        self._is_fixed = True
        self._datetime = datetime.datetime(year, month, day, hour, minute, second)

    def now(self):
        if self._is_fixed:
            return self._datetime
        return datetime.datetime.now()

    def today(self):
        if self._is_fixed:
            return self._datetime.date()
        return datetime.datetime.today()

    def reset(self):
        self._is_fixed = False

    @property
    def year(self):
        return self._datetime.year

    @property
    def month(self):
        return self._datetime.month

    @property
    def day(self):
        return self._datetime.day


if __name__ == '__main__':
    fixed_datetime = FixDateTime()
    # fixed_datetime.fix(2000, 9, 3, 0, 0, 0)

    print(fixed_datetime.now())
    fixed_datetime.fix(2000, 9, 3, 12, 34 ,56)
    print(fixed_datetime.now())
    print(fixed_datetime.today())
    print(fixed_datetime.now())

    fixed_datetime.reset()
    print(fixed_datetime.now())
    print(fixed_datetime.today())
    print(fixed_datetime.now())
