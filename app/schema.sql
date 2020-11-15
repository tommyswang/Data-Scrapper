
DROP TABLE IF EXISTS `scrape_job`;
CREATE TABLE `scrape_job` (
  `id` int NOT NULL AUTO_INCREMENT,
  `status` varchar(50) DEFAULT NULL,
  `jobType` varchar(20) DEFAULT NULL,
  `jobInput` varchar(300) DEFAULT NULL,
  `fileId` varchar(64) DEFAULT NULL,
  `extra` text,
  `name` varchar(64),
  `sys_created_on` timestamp DEFAULT CURRENT_TIMESTAMP,
  `sys_updated_on` timestamp DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ;


DROP TABLE IF EXISTS `scrape_file`;
CREATE TABLE `scrape_file` (
  `id` varchar(64) NOT NULL,
  `name` varchar(64) DEFAULT NULL,
  `path` text,
  `sys_created_on` timestamp DEFAULT CURRENT_TIMESTAMP,
  `sys_updated_on` timestamp DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
);

