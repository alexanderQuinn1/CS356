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
-- Table structure for table `flask_monitor`
--

DROP TABLE IF EXISTS `flask_monitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flask_monitor`
(
    `flask_monitor_id` int NOT NULL AUTO_INCREMENT,
    `expansion_id`     int NOT NULL,
    `temp`             int         DEFAULT NULL,
    `ph`               int         DEFAULT NULL,
    `osmolality`       int         DEFAULT NULL,
    `asset_id`         varchar(45) DEFAULT NULL,
    PRIMARY KEY (`flask_monitor_id`),
    KEY                `flask_monitor_expansion_FK_idx` (`expansion_id`),
    CONSTRAINT `flask_monitor_expansion_FK` FOREIGN KEY (`expansion_id`) REFERENCES `expansion` (`expansion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flask_monitor`
--

LOCK
TABLES `flask_monitor` WRITE;
/*!40000 ALTER TABLE `flask_monitor` DISABLE KEYS */;
INSERT INTO `flask_monitor`
VALUES (1, 1, 37, 0, 0, 'FLASK001'),
       (2, 1, 37, 5, 285, 'FLASK002'),
       (3, 1, 88, 5, 290, 'FLASK003'),
       (4, 1, 90, 6, 292, 'FLASK004'),
       (5, 2, 37, 100, 100, 'FLASK001'),
       (6, 2, 37, 100, 100, 'FLASK002'),
       (7, 2, 37, 7, 294, 'FLASK003'),
       (8, 2, 37, 8, 295, 'FLASK004'),
       (9, 3, 37, 7, 290, 'FLASK001'),
       (10, 3, 77, 7, 274, 'FLASK002'),
       (11, 3, 78, 7, 283, 'FLASK003'),
       (12, 3, 79, 7, 280, 'FLASK004'),
       (13, 4, 75, 6, 275, 'FLASK001'),
       (14, 4, 75, 6, 275, 'FLASK002'),
       (15, 4, 78, 5, 278, 'FLASK003'),
       (16, 4, 77, 6, 278, 'FLASK004'),
       (17, 5, 66, 7, 250, 'FLASK001'),
       (18, 5, 68, 7, 260, 'FLASK002'),
       (19, 5, 69, 8, 270, 'FLASK003'),
       (20, 5, 73, 9, 280, 'FLASK004'),
       (21, 6, 65, 12, 280, 'FLASK001'),
       (22, 6, 66, 11, 270, 'FLASK002'),
       (23, 6, 70, 13, 275, 'FLASK003'),
       (24, 6, 77, 12, 280, 'FLASK004'),
       (25, 7, 130, 12, 180, 'FLASK001'),
       (26, 7, 140, 12, 190, 'FLASK002'),
       (27, 7, 150, 12, 200, 'FLASK003'),
       (28, 7, 130, 10, 170, 'FLASK004'),
       (29, 8, 125, 12, 120, 'FLASK001'),
       (30, 8, 132, 8, 123, 'FLASK002'),
       (31, 8, 128, 9, 132, 'FLASK003'),
       (32, 8, 127, 9, 145, 'FLASK004'),
       (33, 9, 140, 10, 198, 'FLASK001'),
       (34, 9, 149, 11, 200, 'FLASK002'),
       (35, 9, 150, 12, 190, 'FLASK003'),
       (36, 9, 129, 8, 150, 'FLASK004'),
       (37, 10, 37, 7, 200, 'FLASK001'),
       (38, 10, 38, 5, 254, 'FLASK002'),
       (39, 10, 45, 7, 244, 'FLASK003'),
       (40, 10, 37, 7, 267, 'FLASK004'),
       (41, 11, 38, 6, 256, 'FLASK001'),
       (42, 11, 37, 6, 277, 'FLASK002'),
       (43, 11, 36, 5, 266, 'FLASK003'),
       (44, 11, 37, 7, 266, 'FLASK004'),
       (45, 12, 37, 6, 278, 'FLASK001'),
       (46, 12, 37, 6, 244, 'FLASK002'),
       (47, 12, 36, 7, 255, 'FLASK003'),
       (48, 12, 35, 6, 274, 'FLASK004');
/*!40000 ALTER TABLE `flask_monitor` ENABLE KEYS */;
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

-- Dump completed on 2023-06-23 14:34:02
