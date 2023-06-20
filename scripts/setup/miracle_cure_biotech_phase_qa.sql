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
-- Table structure for table `passage_qa`
--

DROP TABLE IF EXISTS `passage_qa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passage_qa` (
  `passage_qa_id` int NOT NULL AUTO_INCREMENT,
  `passage_id` int DEFAULT NULL,
  `date_time` datetime DEFAULT NULL,
  `cell_count` int DEFAULT NULL,
  `ph` int DEFAULT NULL,
  `osmolality` int DEFAULT NULL,
  `sterility` int DEFAULT NULL,
  `passed` tinyint DEFAULT NULL,
  PRIMARY KEY (`passage_qa_id`),
  CONSTRAINT `passage_qa_passage_FK` FOREIGN KEY (`passage_id`) REFERENCES `passage` (`passage_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passage_qa`
--

LOCK TABLES `passage_qa` WRITE;
/*!40000 ALTER TABLE `passage_qa` DISABLE KEYS */;
INSERT INTO `passage_qa` VALUES (1,1,'2023-05-16 13:30:00',100,6,280,100,1),(2,2,'2023-05-16 14:00:00',120,7,275,111,1),(3,3,'2023-05-16 14:30:00',140,5,295,12,1),(4,4,'2023-05-17 13:30:00',210,8,80,9,1),(5,5,'2023-05-17 14:30:00',220,7,250,9,1),(6,6,'2023-05-17 15:30:00',200,10,281,12,0),(7,7,'2023-05-18 16:30:00',100,9,180,14,1),(8,8,'2023-05-18 17:30:00',120,12,190,18,1),(9,9,'2023-05-18 19:30:00',128,11,195,24,1);
/*!40000 ALTER TABLE `passage_qa` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-01 14:58:58
