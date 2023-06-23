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
-- Table structure for table `fill_room_qa`
--

DROP TABLE IF EXISTS `fill_room_qa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fill_room_qa`
(
    `fill_room_qa_id` int NOT NULL,
    `fill_room_id`    int           DEFAULT NULL,
    `date_time`       datetime      DEFAULT NULL,
    `mycoplasma`      varchar(15)   DEFAULT NULL,
    `virus_testing`   varchar(15)   DEFAULT NULL,
    `amino_acids`     varchar(15)   DEFAULT NULL,
    `trace_elements`  varchar(15)   DEFAULT NULL,
    `cell_count`      int           DEFAULT NULL,
    `ph`              int           DEFAULT NULL,
    `osmolality`      int           DEFAULT NULL,
    `sterility`       int           DEFAULT NULL,
    `passed`          tinyint       DEFAULT NULL,
    `analysis`        VARCHAR(3000) DEFAULT NULL,
    PRIMARY KEY (`fill_room_qa_id`),
    KEY               `fill_room_qa_fill_room_FK_idx` (`fill_room_id`),
    CONSTRAINT `fill_room_qa_fill_room_FK` FOREIGN KEY (`fill_room_id`) REFERENCES `fill_room` (`fill_room_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fill_room_qa`
--

LOCK
TABLES `fill_room_qa` WRITE;
/*!40000 ALTER TABLE `fill_room_qa` DISABLE KEYS */;
INSERT INTO `fill_room_qa`
VALUES
    (1, 1, '2023-05-16 16:00:00', 'favourable', 'intermediate', 'favourable', 'non-favourable', 120, 6, 280, 100, 0,''),
    (2, 2, '2023-05-17 16:00:00', 'favourable', 'favourable', 'favourable', 'favourable', 145, 8, 250, 122, 1, ''),
    (3, 3, '2023-05-18 21:00:00', 'intermediate', 'non-favourable', 'favourable', 'favourable', 180, 12, 180, 123, 0,'');
/*!40000 ALTER TABLE `fill_room_qa` ENABLE KEYS */;
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
