-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: miracle_cure_biotech
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `passage_monitor`
--

DROP TABLE IF EXISTS `passage_monitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passage_monitor`
(
    `passage_monitor_id` int NOT NULL AUTO_INCREMENT,
    `passage_id`         int         DEFAULT NULL,
    `cell_count`         int         DEFAULT NULL,
    `peristaltic_pump`   varchar(10) DEFAULT NULL,
    PRIMARY KEY (`passage_monitor_id`),
    KEY                  `passage_monitor_Passage_FK_idx` (`passage_id`),
    CONSTRAINT `passage_monitor_passage_FK` FOREIGN KEY (`passage_id`) REFERENCES `passage` (`passage_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passage_monitor`
--

LOCK
TABLES `passage_monitor` WRITE;
/*!40000 ALTER TABLE `passage_monitor` DISABLE KEYS */;
INSERT INTO `passage_monitor`
VALUES (1, 1, 123, 'low'),
       (2, 2, 25, 'off'),
       (3, 3, 24, 'high'),
       (4, 4, 345, 'low'),
       (5, 5, 64, 'low'),
       (6, 6, 34, 'high'),
       (7, 7, 56, 'off'),
       (8, 8, 23, 'low'),
       (9, 9, 122, 'low'),
       (10, 10, 125, 'high'),
       (11, 11, 145, 'low'),
       (12, 12, 130, 'off');
/*!40000 ALTER TABLE `passage_monitor` ENABLE KEYS */;
UNLOCK
TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-23 14:34:03
