PRAGMA foreign_keys=false;


DROP TABLE IF EXISTS `account_types`;
DROP TABLE IF EXISTS `accounts`;
DROP TABLE IF EXISTS `statements`;
-- DROP TABLE IF EXISTS `fiscal_years`;


PRAGMA foreign_keys=true;


CREATE TABLE IF NOT EXISTS `account_types` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT ,
    `type_name` TEXT NOT NULL UNIQUE ,
    `type_name_hepburn` TEXT NOT NULL UNIQUE
);
INSERT INTO `account_types` (`type_name`, 'type_name_hepburn')
VALUES ('変動費', 'hendohi'),
       ('固定費', 'koteihi'),
       ('売上', 'uriage');


CREATE TABLE IF NOT EXISTS `accounts` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT ,
    `account_name` TEXT NOT NULL UNIQUE ,
    `account_name_hepburn` TEXT NOT NULL UNIQUE ,
    `account_type_id` INTEGER NOT NULL ,
    `default_amount` INTEGER NOT NULL DEFAULT 0 ,
    FOREIGN KEY (`account_type_id`) REFERENCES `account_types`(`id`)
);
INSERT INTO `accounts` (`account_name`, `account_name_hepburn`, `account_type_id`, `default_amount`)
VALUES ('仕入', 'shiire', 1, 0),
       ('接待','settai', 1, 0),
       ('雑費', 'zappi', 1, 0),
       ('消耗品','shomohin', 1, 0),
       ('家賃', 'yachin', 1, 0),
       ('アイス', 'aisu', 1, 0),
       ('大阪ガス', 'osakagas', 1, 0),
       ('保険', 'hoken', 1, 0),
       ('通信費', 'tsushinhi', 1, 0),
       ('修繕費', 'shuzenhi', 1, 0),
       ('広告費', 'kokokuhi', 1, 0),
       ('自動車税', 'jidoshazei', 1, 0),
       ('酒代', 'sakadai', 1, 0),
       ('備品', 'bihin', 1, 0),

       ('おしぼり', 'oshibori', 2, 0),
       ('駆除器', 'kujoki', 2, 0),
       ('リース植木', 'risueki', 2, 0),
       ('著作権', 'chosakuken', 2, 0),
       ('カラオケ', 'karaoke', 2, 0),

       ('売上', 'uriage', 3, 0);


CREATE TABLE IF NOT EXISTS `statements` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT ,
    `year` INTEGER NOT NULL ,
    `month` INTEGER NOT NULL ,
    `day` INTEGER NOT NULL ,
    `account_id` INTEGER NOT NULL ,
    `amount` INTEGER NOT NULL ,
    `created_at` TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')) ,
    FOREIGN KEY (`account_id`) REFERENCES `accounts`(`id`)
);
