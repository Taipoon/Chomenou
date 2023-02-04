DROP TABLE IF EXISTS `statements`;
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

insert into `statements` (year, month, day, account_id, amount, created_at)
values  (2020, 1, 1, 1, 1300, '2023-01-06 06:58:17'),
        (2020, 1, 1, 2, 5310, '2023-01-06 06:58:17'),
        (2020, 1, 3, 2, 5330, '2023-01-06 06:58:17'),
        (2020, 1, 6, 2, 1300, '2023-01-06 06:58:17'),
        (2020, 1, 10, 3, 5310, '2023-01-06 06:58:17'),
        (2020, 1, 15, 4, 5330, '2023-01-06 06:58:17'),
        (2020, 1, 2, 1, 10800, '2023-01-06 06:58:17'),
        (2020, 2, 1, 1, 1300, '2023-01-06 06:58:17'),
        (2020, 2, 2, 2, 5310, '2023-01-06 06:58:17'),
        (2020, 2, 1, 2, 5330, '2023-01-06 06:58:17'),
        (2020, 2, 3, 3, 10800, '2023-01-06 06:58:17'),
        (2020, 2, 1, 1, 800, '2023-01-06 06:58:17'),
        (2021, 1, 3, 2, 9000, '2023-01-06 06:58:17'),
        (2021, 1, 4, 1, 80060, '2023-01-06 06:58:17');
