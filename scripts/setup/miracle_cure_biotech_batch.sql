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
-- Table structure for table `batch`
--

DROP TABLE IF EXISTS `batch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `batch`
(
    `batch_no`         varchar(11) NOT NULL,
    `quantity`         int        DEFAULT NULL,
    `prod_type_code`   varchar(6) DEFAULT NULL,
    `current_stage`    int        DEFAULT NULL,
    `prod_schedule_id` int        DEFAULT NULL,
    PRIMARY KEY (`batch_no`),
    KEY                `product_type_batch_fk_idx` (`prod_type_code`),
    KEY                `batch_stage_lookup_FK_idx` (`current_stage`),
    KEY                `batch_production_schedule_fk_idx` (`prod_schedule_id`),
    CONSTRAINT `batch_production_schedule_fk` FOREIGN KEY (`prod_schedule_id`) REFERENCES `production_schedule` (`prod_schedule_id`),
    CONSTRAINT `batch_stage_lookup_FK` FOREIGN KEY (`current_stage`) REFERENCES `stage_lookup` (`stage_id`),
    CONSTRAINT `product_type_batch_fk` FOREIGN KEY (`prod_type_code`) REFERENCES `product_type` (`prod_type_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `batch`
--

LOCK
TABLES `batch` WRITE;
/*!40000 ALTER TABLE `batch` DISABLE KEYS */;
INSERT INTO `batch`
VALUES ('IRV2305001', 100, 'XXX10', 9, 4),
       ('IRV2305003', 100, 'XXX11', 9, 5),
       ('IRV2305004', 100, 'XXX12', 8, 6),
       ('IRV2306001', 100, 'XXX11', 2, 7),
       ('IRV2306002', 100, 'XXX12', 1, 8);
/*!40000 ALTER TABLE `batch` ENABLE KEYS */;
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
