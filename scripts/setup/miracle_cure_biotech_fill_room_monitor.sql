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
-- Table structure for table `fill_room_monitor`
--

DROP TABLE IF EXISTS `fill_room_monitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fill_room_monitor` (
  `fill_room_monitor_id` int NOT NULL,
  `fill_room_id` int DEFAULT NULL,
  `humidity` int DEFAULT NULL,
  `last_stir_delta` int DEFAULT NULL,
  `temp` int DEFAULT NULL,
  `asset_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`fill_room_monitor_id`),
  KEY `fill_room_monitor_fill_room_FK_idx` (`fill_room_id`),
  CONSTRAINT `fill_room_monitor_fill_room_FK` FOREIGN KEY (`fill_room_id`) REFERENCES `fill_room` (`fill_room_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fill_room_monitor`
--

LOCK TABLES `fill_room_monitor` WRITE;
/*!40000 ALTER TABLE `fill_room_monitor` DISABLE KEYS */;
INSERT INTO `fill_room_monitor` VALUES (1,1,40,79,38,'VAT001'),(2,2,60,82,35,'VAT002'),(3,3,70,90,37,'VAT003'),(4,4,60,75,38,'VAT001'),(5,5,90,60,36,,'VAT002');
/*!40000 ALTER TABLE `fill_room_monitor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-23 14:34:02
