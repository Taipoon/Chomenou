PRAGMA foreign_keys=false;


DROP TABLE IF EXISTS `account_types`;
DROP TABLE IF EXISTS `accounts`;
DROP TABLE IF EXISTS `statements`;
DROP TABLE IF EXISTS  `fiscal_years`;


PRAGMA foreign_keys=true;


CREATE TABLE IF NOT EXISTS `account_types` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT ,
    `type_name` TEXT NOT NULL UNIQUE
);
INSERT INTO `account_types` (`type_name`)
VALUES ('変動費'),
       ('固定費'),
       ('売上');


CREATE TABLE IF NOT EXISTS `accounts` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT ,
    `account_name` TEXT NOT NULL UNIQUE ,
    `account_type_id` INTEGER NOT NULL ,
    `default_amount` INTEGER NOT NULL DEFAULT 0 ,
    FOREIGN KEY (`account_type_id`) REFERENCES `account_types`(`id`)
);
INSERT INTO `accounts` (`account_name`, `account_type_id`, `default_amount`)
VALUES ('仕入', 1, 0),
       ('接待', 1, 0),
       ('売上', 3, 0),
       ('おしぼり', 2, 8800);


CREATE TABLE IF NOT EXISTS `statements` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT ,
    `month` INTEGER NOT NULL ,
    `day` INTEGER NOT NULL ,
    `account_id` INTEGER NOT NULL ,
    `amount` INTEGER NOT NULL ,
    `created_at` TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')) ,
    FOREIGN KEY (`account_id`) REFERENCES `accounts`(`id`)
);


CREATE TABLE IF NOT EXISTS `fiscal_years` (
    `year` INTEGER PRIMARY KEY
);
INSERT INTO `fiscal_years` (`year`)
VALUES (2020),
       (2021),
       (2022);