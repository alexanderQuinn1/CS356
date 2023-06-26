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
-- Table structure for table `expansion`
--

DROP TABLE IF EXISTS `expansion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expansion` (
  `expansion_id` int NOT NULL AUTO_INCREMENT,
  `batch_id` varchar(11) DEFAULT NULL,
  `stage` int DEFAULT NULL,
  PRIMARY KEY (`expansion_id`),
  KEY `expansion_batch_fk_idx` (`batch_id`),
  KEY `expansion_stage_lookup_fk_idx` (`stage`),
  CONSTRAINT `expansion_batch_fk` FOREIGN KEY (`batch_id`) REFERENCES `batch` (`batch_no`),
  CONSTRAINT `expansion_stage_lookup_fk` FOREIGN KEY (`stage`) REFERENCES `stage_lookup` (`stage_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expansion`
--

LOCK TABLES `expansion` WRITE;
/*!40000 ALTER TABLE `expansion` DISABLE KEYS */;
INSERT INTO `expansion` VALUES (1,'IRV2305001',2),(2,'IRV2305001',4),(3,'IRV2305001',6),(4,'IRV2305003',2),(5,'IRV2305003',4),(6,'IRV2305003',6),(7,'IRV2305004',2),(8,'IRV2305004',4),(9,'IRV2305004',6),(10,'IRV2306001',2),(11,'IRV2306001',4),(12,'IRV2306001',6),(13,'IRV2306002',2),(14,'IRV2306002',4),(15,'IRV2306002',6);
/*!40000 ALTER TABLE `expansion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-23 14:34:03
