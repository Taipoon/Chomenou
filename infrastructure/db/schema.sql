PRAGMA foreign_keys=false;


DROP TABLE IF EXISTS `account_types`;
DROP TABLE IF EXISTS `accounts`;
DROP TABLE IF EXISTS `statements`;


PRAGMA foreign_keys=true;


CREATE TABLE IF NOT EXISTS `account_types` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT ,
    `type_name` TEXT NOT NULL UNIQUE ,
    `type_name_hepburn` TEXT NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS `accounts` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT ,
    `account_name` TEXT NOT NULL UNIQUE ,
    `account_name_hepburn` TEXT NOT NULL UNIQUE ,
    `account_type_id` INTEGER NOT NULL ,
    `default_amount` INTEGER NOT NULL DEFAULT 0 ,
    FOREIGN KEY (`account_type_id`) REFERENCES `account_types`(`id`)
);


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
