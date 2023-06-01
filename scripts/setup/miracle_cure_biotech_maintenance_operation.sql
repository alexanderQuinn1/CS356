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
-- Table structure for table `maintenance_operation`
--

DROP TABLE IF EXISTS `maintenance_operation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `maintenance_operation` (
  `maintenance_id` int NOT NULL,
  `date` date DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  `plant_id` varchar(9) DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL,
  `man_hours` int DEFAULT NULL,
  `parts_replaced` varchar(2000) DEFAULT NULL,
  `cost` decimal(10,0) DEFAULT NULL,
  `shutdown_required` tinyint DEFAULT NULL,
  `planned_activity` tinyint DEFAULT NULL,
  PRIMARY KEY (`maintenance_id`),
  KEY `maintenance_operation_plant_fk_idx` (`plant_id`),
  CONSTRAINT `maintenance_operation_plant_fk` FOREIGN KEY (`plant_id`) REFERENCES `plant` (`plant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_operation`
--

LOCK TABLES `maintenance_operation` WRITE;
/*!40000 ALTER TABLE `maintenance_operation` DISABLE KEYS */;
INSERT INTO `maintenance_operation` VALUES (10,'2023-05-15','09:00:00','13:00:00','IRV100111','Change Perstalic Pump',3,'Perstalic Pump',1000,1,1),(11,'2023-05-16','09:30:00','13:30:00','IRV100112','Change Flask sensor',NULL,'Flask Sensor',300,1,0),(12,'2023-05-14','12:00:00','14:00:00','IRV100113','Change Perstalic Pump',3,'Perstalic Pump',1000,1,1);
/*!40000 ALTER TABLE `maintenance_operation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-18 13:45:15
