DROP TABLE IF EXISTS `2000`;
CREATE TABLE IF NOT EXISTS `2000` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT ,
    `month` INTEGER NOT NULL ,
    `day` INTEGER NOT NULL ,
    `account_id` INTEGER NOT NULL ,
    `amount` INTEGER NOT NULL ,
    `created_at` TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')) ,
    FOREIGN KEY (`account_id`) REFERENCES `accounts`(`id`)
);

insert into `2000` (month, day, account_id, amount, created_at)
values  (1, 1, 1, 1300, '2023-01-06 06:58:17'),
        (1, 1, 2, 5310, '2023-01-06 06:58:17'),
        (1, 3, 2, 5330, '2023-01-06 06:58:17'),
        (1, 2, 1, 10800, '2023-01-06 06:58:17'),
        (1, 2, 3, 800, '2023-01-06 06:58:17'),
        (1, 3, 2, 9000, '2023-01-06 06:58:17'),
        (1, 4, 1, 80060, '2023-01-06 06:58:17');
