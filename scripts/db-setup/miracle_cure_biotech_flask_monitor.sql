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
CREATE TABLE `flask_monitor` (
  `flask_monitor_id` int NOT NULL,
  `expansion_id` int NOT NULL,
  `temp` int DEFAULT NULL,
  `ph` int DEFAULT NULL,
  `osmoality` int DEFAULT NULL,
  PRIMARY KEY (`flask_monitor_id`),
  KEY `flask_monitor_expansion_FK_idx` (`expansion_id`),
  CONSTRAINT `flask_monitor_expansion_FK` FOREIGN KEY (`expansion_id`) REFERENCES `expansion` (`expansion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flask_monitor`
--

LOCK TABLES `flask_monitor` WRITE;
/*!40000 ALTER TABLE `flask_monitor` DISABLE KEYS */;
INSERT INTO `flask_monitor` VALUES (1,1,78,5,285),(2,1,82,5,285),(3,1,88,5,290),(4,1,90,6,292),(5,2,78,6,289),(6,2,94,7,289),(7,2,98,7,294),(8,2,100,8,295),(9,3,75,7,290),(10,3,77,7,274),(11,3,78,7,283),(12,3,79,7,280),(13,4,75,6,275),(14,4,75,6,275),(15,4,78,5,278),(16,4,77,6,278),(17,5,66,7,250),(18,5,68,7,260),(19,5,69,8,270),(20,5,73,9,280),(21,6,65,12,280),(22,6,66,11,270),(23,6,70,13,275),(24,6,77,12,280),(25,7,130,12,180),(26,7,140,12,190),(27,7,150,12,200),(28,7,130,10,170),(29,8,125,12,120),(30,8,132,8,123),(31,8,128,9,132),(32,8,127,9,145),(33,9,140,10,198),(34,9,149,11,200),(35,9,150,12,190),(36,9,129,8,150);
/*!40000 ALTER TABLE `flask_monitor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-18 13:45:12
