-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: test_maker
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class` (
  `class_number` int NOT NULL AUTO_INCREMENT,
  `class_roman` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`class_number`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES (1,'I','2024-11-28 02:41:27','2024-11-28 02:41:27'),(2,'II','2024-11-28 02:41:27','2024-11-28 02:41:27'),(3,'III','2024-11-28 02:41:27','2024-11-28 02:41:27'),(4,'IV','2024-11-28 02:41:27','2024-11-28 02:41:27'),(5,'V','2024-11-28 02:41:27','2024-11-28 02:41:27'),(6,'VI','2024-11-28 02:41:27','2024-11-28 02:41:27'),(7,'VII','2024-11-28 02:41:27','2024-11-28 02:41:27'),(8,'VIII','2024-11-28 02:41:27','2024-11-28 02:41:27'),(9,'IX','2024-11-28 02:41:27','2024-11-28 02:41:27'),(10,'X','2024-11-28 02:41:27','2024-11-28 02:41:27'),(11,'XI','2024-11-28 02:41:27','2024-11-28 02:41:27'),(12,'XII','2024-11-28 02:41:27','2024-11-28 02:41:27');
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fib`
--

DROP TABLE IF EXISTS `fib`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fib` (
  `id` varchar(36) NOT NULL,
  `question_id` varchar(36) NOT NULL,
  `missing_word` text NOT NULL,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fib_question_details_FK` (`question_id`),
  CONSTRAINT `fib_question_details_FK` FOREIGN KEY (`question_id`) REFERENCES `question_details` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fib`
--

LOCK TABLES `fib` WRITE;
/*!40000 ALTER TABLE `fib` DISABLE KEYS */;
INSERT INTO `fib` VALUES ('8429dae3-a76b-11ef-a59c-5254003fef98','84291e17-a76b-11ef-a59c-5254003fef98','fib word 3 1','2024-11-28 02:45:02','2024-11-28 02:45:02'),('842aa294-a76b-11ef-a59c-5254003fef98','84291e17-a76b-11ef-a59c-5254003fef98','fib word 3 2','2024-11-28 02:45:02','2024-11-28 02:45:02'),('89314a0d-5fe7-11ef-a6ac-5254003fef98','89306b7f-5fe7-11ef-a6ac-5254003fef98','fib word 1','2024-11-28 02:45:02','2024-11-28 02:45:02'),('8931ea9e-5fe7-11ef-a6ac-5254003fef98','89306b7f-5fe7-11ef-a6ac-5254003fef98','fib word 2','2024-11-28 02:45:02','2024-11-28 02:45:02'),('bdaf990b-a76b-11ef-a59c-5254003fef98','bdaf0e74-a76b-11ef-a59c-5254003fef98','fib word 41','2024-11-28 02:45:02','2024-11-28 02:45:02'),('bdafc240-a76b-11ef-a59c-5254003fef98','bdaf0e74-a76b-11ef-a59c-5254003fef98','fib word 42','2024-11-28 02:45:02','2024-11-28 02:45:02'),('c374dc7f-b27d-11ef-b086-5254003fef98','c374ba34-b27d-11ef-b086-5254003fef98','fib word 61','2024-12-05 01:54:29','2024-12-05 01:54:29'),('c374ff92-b27d-11ef-b086-5254003fef98','c374ba34-b27d-11ef-b086-5254003fef98','fib word 62','2024-12-05 01:54:29','2024-12-05 01:54:29'),('ce21b596-b27d-11ef-b086-5254003fef98','ce219550-b27d-11ef-b086-5254003fef98','fib word 71','2024-12-05 01:54:47','2024-12-05 01:54:47'),('ce21ceac-b27d-11ef-b086-5254003fef98','ce219550-b27d-11ef-b086-5254003fef98','fib word 72','2024-12-05 01:54:47','2024-12-05 01:54:47'),('ddb19688-b27d-11ef-b086-5254003fef98','ddb16f15-b27d-11ef-b086-5254003fef98','fib word 81','2024-12-05 01:55:13','2024-12-05 01:55:13'),('ddb1b69d-b27d-11ef-b086-5254003fef98','ddb16f15-b27d-11ef-b086-5254003fef98','fib word 82','2024-12-05 01:55:13','2024-12-05 01:55:13'),('ffde1e89-aa92-11ef-8508-5254003fef98','ffdd1dd3-aa92-11ef-8508-5254003fef98','fib word 51','2024-11-28 02:45:02','2024-11-28 02:45:02'),('ffde5ef8-aa92-11ef-8508-5254003fef98','ffdd1dd3-aa92-11ef-8508-5254003fef98','fib word 52','2024-11-28 02:45:02','2024-11-28 02:45:02');
/*!40000 ALTER TABLE `fib` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `match_a`
--

DROP TABLE IF EXISTS `match_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match_a` (
  `id` varchar(36) NOT NULL,
  `question_id` varchar(36) NOT NULL,
  `match_option` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `match_a_question_details_FK` (`question_id`),
  CONSTRAINT `match_a_question_details_FK` FOREIGN KEY (`question_id`) REFERENCES `question_details` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match_a`
--

LOCK TABLES `match_a` WRITE;
/*!40000 ALTER TABLE `match_a` DISABLE KEYS */;
INSERT INTO `match_a` VALUES ('0ef1757d-aa93-11ef-8508-5254003fef98','0ef13c5c-aa93-11ef-8508-5254003fef98','match a 41','2024-11-28 02:54:42','2024-11-28 02:54:42'),('0ef1c68e-aa93-11ef-8508-5254003fef98','0ef13c5c-aa93-11ef-8508-5254003fef98','match a 42','2024-11-28 02:54:42','2024-11-28 02:54:42'),('2442dfd5-a76c-11ef-a59c-5254003fef98','24424f52-a76c-11ef-a59c-5254003fef98','match a 31','2024-11-28 02:54:42','2024-11-28 02:54:42'),('244300df-a76c-11ef-a59c-5254003fef98','24424f52-a76c-11ef-a59c-5254003fef98','match a 32','2024-11-28 02:54:42','2024-11-28 02:54:42'),('4c7c9aff-5fe8-11ef-a6ac-5254003fef98','4c7ad71a-5fe8-11ef-a6ac-5254003fef98','match_option=\'match a 1\'','2024-11-28 02:54:42','2024-11-28 02:54:42'),('4c7ce26d-5fe8-11ef-a6ac-5254003fef98','4c7ad71a-5fe8-11ef-a6ac-5254003fef98','match_option=\'match a 2\'','2024-11-28 02:54:42','2024-11-28 02:54:42'),('a29cc94f-5fe8-11ef-a6ac-5254003fef98','a29c1391-5fe8-11ef-a6ac-5254003fef98','match a 11','2024-11-28 02:54:42','2024-11-28 02:54:42'),('a29cef74-5fe8-11ef-a6ac-5254003fef98','a29c1391-5fe8-11ef-a6ac-5254003fef98','match a 21','2024-11-28 02:54:42','2024-11-28 02:54:42');
/*!40000 ALTER TABLE `match_a` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `match_b`
--

DROP TABLE IF EXISTS `match_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match_b` (
  `id` varchar(36) NOT NULL,
  `question_id` varchar(36) NOT NULL,
  `match_option` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `match_b_question_details_FK` (`question_id`),
  CONSTRAINT `match_b_question_details_FK` FOREIGN KEY (`question_id`) REFERENCES `question_details` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match_b`
--

LOCK TABLES `match_b` WRITE;
/*!40000 ALTER TABLE `match_b` DISABLE KEYS */;
INSERT INTO `match_b` VALUES ('0ef1efc4-aa93-11ef-8508-5254003fef98','0ef13c5c-aa93-11ef-8508-5254003fef98','match b 41','2024-11-28 02:54:45','2024-11-28 02:54:45'),('0ef26578-aa93-11ef-8508-5254003fef98','0ef13c5c-aa93-11ef-8508-5254003fef98','match b 42','2024-11-28 02:54:45','2024-11-28 02:54:45'),('24433306-a76c-11ef-a59c-5254003fef98','24424f52-a76c-11ef-a59c-5254003fef98','match b 31','2024-11-28 02:54:45','2024-11-28 02:54:45'),('24435c60-a76c-11ef-a59c-5254003fef98','24424f52-a76c-11ef-a59c-5254003fef98','match b 32','2024-11-28 02:54:45','2024-11-28 02:54:45'),('4c7d3771-5fe8-11ef-a6ac-5254003fef98','4c7ad71a-5fe8-11ef-a6ac-5254003fef98','match_option=\'match b 1\'','2024-11-28 02:54:45','2024-11-28 02:54:45'),('4c7d7b6e-5fe8-11ef-a6ac-5254003fef98','4c7ad71a-5fe8-11ef-a6ac-5254003fef98','match_option=\'match b 2\'','2024-11-28 02:54:45','2024-11-28 02:54:45'),('a29d1022-5fe8-11ef-a6ac-5254003fef98','a29c1391-5fe8-11ef-a6ac-5254003fef98','match b 11','2024-11-28 02:54:45','2024-11-28 02:54:45'),('a29d24c8-5fe8-11ef-a6ac-5254003fef98','a29c1391-5fe8-11ef-a6ac-5254003fef98','match b 21','2024-11-28 02:54:45','2024-11-28 02:54:45');
/*!40000 ALTER TABLE `match_b` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mcq`
--

DROP TABLE IF EXISTS `mcq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mcq` (
  `id` varchar(36) NOT NULL,
  `question_id` varchar(36) NOT NULL,
  `option_text` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `mcq_question_details_FK` (`question_id`),
  CONSTRAINT `mcq_question_details_FK` FOREIGN KEY (`question_id`) REFERENCES `question_details` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mcq`
--

LOCK TABLES `mcq` WRITE;
/*!40000 ALTER TABLE `mcq` DISABLE KEYS */;
INSERT INTO `mcq` VALUES ('0300cf91-b27e-11ef-b086-5254003fef98','0300ab85-b27e-11ef-b086-5254003fef98','option 5a','2024-12-05 01:56:15','2024-12-05 01:56:15'),('0300e961-b27e-11ef-b086-5254003fef98','0300ab85-b27e-11ef-b086-5254003fef98','option 5b','2024-12-05 01:56:15','2024-12-05 01:56:15'),('848e3f62-a76c-11ef-a59c-5254003fef98','848d743a-a76c-11ef-a59c-5254003fef98','option 2a','2024-11-28 02:54:59','2024-11-28 02:54:59'),('848e67c3-a76c-11ef-a59c-5254003fef98','848d743a-a76c-11ef-a59c-5254003fef98','option 2b','2024-11-28 02:54:59','2024-11-28 02:54:59'),('91f38452-a76c-11ef-a59c-5254003fef98','91f3009c-a76c-11ef-a59c-5254003fef98','option 3a','2024-11-28 02:54:59','2024-11-28 02:54:59'),('91f3a62e-a76c-11ef-a59c-5254003fef98','91f3009c-a76c-11ef-a59c-5254003fef98','option 3b','2024-11-28 02:54:59','2024-11-28 02:54:59'),('e43585ea-5e6c-11ef-b4c0-5254003fef98','e4356373-5e6c-11ef-b4c0-5254003fef98','option a','2024-11-28 02:54:59','2024-11-28 02:54:59'),('e479f5df-5e6c-11ef-b4c0-5254003fef98','e4356373-5e6c-11ef-b4c0-5254003fef98','option b','2024-11-28 02:54:59','2024-11-28 02:54:59'),('fcb20231-b27d-11ef-b086-5254003fef98','fcb1cb5c-b27d-11ef-b086-5254003fef98','option 4a','2024-12-05 01:56:05','2024-12-05 01:56:05'),('fcb24aaa-b27d-11ef-b086-5254003fef98','fcb1cb5c-b27d-11ef-b086-5254003fef98','option 4b','2024-12-05 01:56:05','2024-12-05 01:56:05');
/*!40000 ALTER TABLE `mcq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_details`
--

DROP TABLE IF EXISTS `question_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question_details` (
  `id` varchar(36) NOT NULL,
  `question_type_id` int NOT NULL,
  `subject_id` varchar(36) NOT NULL,
  `difficulty` varchar(36) NOT NULL,
  `marks` int NOT NULL,
  `content` longtext,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_ques_details_subject` (`subject_id`),
  KEY `fk_ques_details_difficulty` (`difficulty`) USING BTREE,
  KEY `question_details_question_type_FK` (`question_type_id`),
  CONSTRAINT `question_details_question_difficulty_FK` FOREIGN KEY (`difficulty`) REFERENCES `question_difficulty` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `question_details_question_type_FK` FOREIGN KEY (`question_type_id`) REFERENCES `question_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `question_details_subject_FK` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_details`
--

LOCK TABLES `question_details` WRITE;
/*!40000 ALTER TABLE `question_details` DISABLE KEYS */;
INSERT INTO `question_details` VALUES ('0300ab85-b27e-11ef-b086-5254003fef98',2,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',3,'mcq question 5','2024-12-05 01:56:15','2024-12-05 01:56:15'),('03d70f13-a76b-11ef-a59c-5254003fef98',6,'0969b86598d8416bbf188b6b45efc8c3','1',2,'subjective 1','2024-11-28 02:55:12','2024-11-28 02:55:12'),('0ef13c5c-aa93-11ef-8508-5254003fef98',4,'0969b86598d8416bbf188b6b45efc8c3','1',3,'match question 4','2024-11-28 02:55:12','2024-11-28 02:55:12'),('186609c2-b27e-11ef-b086-5254003fef98',6,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',2,'subjective 2','2024-12-05 01:56:51','2024-12-05 01:56:51'),('1aa7b083-b27e-11ef-b086-5254003fef98',6,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',2,'subjective 3','2024-12-05 01:56:55','2024-12-05 01:56:55'),('1cdf8bfe-b27e-11ef-b086-5254003fef98',6,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',2,'subjective 4','2024-12-05 01:56:59','2024-12-05 01:56:59'),('24424f52-a76c-11ef-a59c-5254003fef98',4,'0969b86598d8416bbf188b6b45efc8c3','1',3,'match question 3','2024-11-28 02:55:12','2024-11-28 02:55:12'),('36f54da4-a76a-11ef-a59c-5254003fef98',1,'0969b86598d8416bbf188b6b45efc8c3','1',1,'hello world 1','2024-11-28 02:55:12','2024-11-28 02:55:12'),('3a6adcc0-b27e-11ef-b086-5254003fef98',1,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',2,'general 1','2024-12-05 01:57:48','2024-12-05 01:57:48'),('3dc68b75-b27e-11ef-b086-5254003fef98',1,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',2,'general 2','2024-12-05 01:57:54','2024-12-05 01:57:54'),('4062ba95-b27e-11ef-b086-5254003fef98',1,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',2,'general 3','2024-12-05 01:57:58','2024-12-05 01:57:58'),('42cc77a5-b27e-11ef-b086-5254003fef98',1,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',2,'general 4','2024-12-05 01:58:02','2024-12-05 01:58:02'),('4c7ad71a-5fe8-11ef-a6ac-5254003fef98',4,'0969b86598d8416bbf188b6b45efc8c3','2',2,'match question 1','2024-11-28 02:55:12','2024-11-28 02:55:12'),('84291e17-a76b-11ef-a59c-5254003fef98',3,'0969b86598d8416bbf188b6b45efc8c3','1',3,'fib question 3','2024-11-28 02:55:12','2024-11-28 02:55:12'),('848d743a-a76c-11ef-a59c-5254003fef98',2,'0969b86598d8416bbf188b6b45efc8c3','1',3,'mcq question 2','2024-11-28 02:55:12','2024-11-28 02:55:12'),('850546a4-b27d-11ef-b086-5254003fef98',3,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',3,'fib question 9','2024-12-05 01:52:44','2024-12-05 02:55:03'),('877eef56-5ff0-11ef-a6ac-5254003fef98',1,'0969b86598d8416bbf188b6b45efc8c3','4',4,'hello world 2','2024-11-28 02:55:12','2024-11-28 02:55:12'),('89306b7f-5fe7-11ef-a6ac-5254003fef98',3,'0969b86598d8416bbf188b6b45efc8c3','5',5,'fib question 2','2024-11-28 02:55:12','2024-11-28 02:55:12'),('896db7c8-5fe9-11ef-a6ac-5254003fef98',7,'0969b86598d8416bbf188b6b45efc8c3','1',6,'ra question 1','2024-11-28 02:55:12','2024-11-28 02:55:12'),('91f3009c-a76c-11ef-a59c-5254003fef98',2,'0969b86598d8416bbf188b6b45efc8c3','1',3,'mcq question 3','2024-11-28 02:55:12','2024-11-28 02:55:12'),('a29c1391-5fe8-11ef-a6ac-5254003fef98',4,'0969b86598d8416bbf188b6b45efc8c3','2',7,'match question 2','2024-11-28 02:55:12','2024-11-28 02:55:12'),('bdaf0e74-a76b-11ef-a59c-5254003fef98',3,'0969b86598d8416bbf188b6b45efc8c3','1',3,'fib question 4','2024-11-28 02:55:12','2024-11-28 02:55:12'),('c374ba34-b27d-11ef-b086-5254003fef98',3,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',3,'fib question 6','2024-12-05 01:54:29','2024-12-05 01:54:29'),('c9e400e3-a76b-11ef-a59c-5254003fef98',7,'0969b86598d8416bbf188b6b45efc8c3','1',3,'ra question 2','2024-11-28 02:55:12','2024-11-28 02:55:12'),('ce219550-b27d-11ef-b086-5254003fef98',3,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',3,'fib question 7','2024-12-05 01:54:47','2024-12-05 01:54:47'),('d49ddd5b-a76b-11ef-a59c-5254003fef98',7,'0969b86598d8416bbf188b6b45efc8c3','1',3,'ra question 3','2024-11-28 02:55:12','2024-11-28 02:55:12'),('ddb16f15-b27d-11ef-b086-5254003fef98',3,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',3,'fib question 8','2024-12-05 01:55:13','2024-12-05 01:55:13'),('e4356373-5e6c-11ef-b4c0-5254003fef98',2,'0969b86598d8416bbf188b6b45efc8c3','3',8,'mcq question 1','2024-11-28 02:55:12','2024-11-28 02:55:12'),('e44baf76-a76a-11ef-a59c-5254003fef98',5,'0969b86598d8416bbf188b6b45efc8c3','1',2,'true false 1','2024-11-28 02:55:12','2024-11-28 02:55:12'),('ed3a6e26-b27d-11ef-b086-5254003fef98',7,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',3,'ra question 4','2024-12-05 01:55:39','2024-12-05 01:55:39'),('f293c1ab-b27d-11ef-b086-5254003fef98',7,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',3,'ra question 5','2024-12-05 01:55:48','2024-12-05 01:55:48'),('fcb1cb5c-b27d-11ef-b086-5254003fef98',2,'9c88cfb63ed34e80a8b12c479fbf6b3d','1',3,'mcq question 4','2024-12-05 01:56:05','2024-12-05 01:56:05'),('ffdd1dd3-aa92-11ef-8508-5254003fef98',3,'0969b86598d8416bbf188b6b45efc8c3','1',3,'fib question 5','2024-11-28 02:55:12','2024-11-28 02:55:12');
/*!40000 ALTER TABLE `question_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_difficulty`
--

DROP TABLE IF EXISTS `question_difficulty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question_difficulty` (
  `id` varchar(36) NOT NULL,
  `level` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_difficulty`
--

LOCK TABLES `question_difficulty` WRITE;
/*!40000 ALTER TABLE `question_difficulty` DISABLE KEYS */;
INSERT INTO `question_difficulty` VALUES ('1','very easy','2024-11-28 02:55:22','2024-11-28 02:55:22'),('2','easy','2024-11-28 02:55:22','2024-11-28 02:55:22'),('3','medium','2024-11-28 02:55:22','2024-11-28 02:55:22'),('4','hard','2024-11-28 02:55:22','2024-11-28 02:55:22'),('5','very hard','2024-11-28 02:55:22','2024-11-28 02:55:22');
/*!40000 ALTER TABLE `question_difficulty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_images`
--

DROP TABLE IF EXISTS `question_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question_images` (
  `id` varchar(36) NOT NULL,
  `question_id` varchar(36) NOT NULL,
  `image_position` int NOT NULL DEFAULT '0',
  `image_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_ques_images_question_id` (`question_id`),
  CONSTRAINT `question_images_question_details_FK` FOREIGN KEY (`question_id`) REFERENCES `question_details` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_images`
--

LOCK TABLES `question_images` WRITE;
/*!40000 ALTER TABLE `question_images` DISABLE KEYS */;
/*!40000 ALTER TABLE `question_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_subquestion_map`
--

DROP TABLE IF EXISTS `question_subquestion_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question_subquestion_map` (
  `id` varchar(36) NOT NULL,
  `test_id` varchar(36) NOT NULL,
  `question_id` varchar(36) NOT NULL,
  `subquestion_id` varchar(36) NOT NULL,
  `subquestion_number` int NOT NULL DEFAULT (0),
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_ques_subques_map_ques_id` (`question_id`),
  KEY `fk_ques_subques_map_subques_id` (`subquestion_id`),
  KEY `fk_ques_subques_map_test_id` (`test_id`),
  CONSTRAINT `question_subquestion_map_question_details_FK` FOREIGN KEY (`question_id`) REFERENCES `question_details` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `question_subquestion_map_question_details_FK_1` FOREIGN KEY (`subquestion_id`) REFERENCES `question_details` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `question_subquestion_map_test_FK` FOREIGN KEY (`test_id`) REFERENCES `test` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_subquestion_map`
--

LOCK TABLES `question_subquestion_map` WRITE;
/*!40000 ALTER TABLE `question_subquestion_map` DISABLE KEYS */;
INSERT INTO `question_subquestion_map` VALUES ('14f71b53-b279-11ef-b086-5254003fef98','14f634f8-b279-11ef-b086-5254003fef98','36f54da4-a76a-11ef-a59c-5254003fef98','ffdd1dd3-aa92-11ef-8508-5254003fef98',1,'2024-12-05 01:20:58','2024-12-05 01:20:58'),('14f7563e-b279-11ef-b086-5254003fef98','14f634f8-b279-11ef-b086-5254003fef98','36f54da4-a76a-11ef-a59c-5254003fef98','24424f52-a76c-11ef-a59c-5254003fef98',2,'2024-12-05 01:20:58','2024-12-05 01:20:58'),('e6b51f6b-b280-11ef-b086-5254003fef98','e6b48eab-b280-11ef-b086-5254003fef98','ce219550-b27d-11ef-b086-5254003fef98','3a6adcc0-b27e-11ef-b086-5254003fef98',1,'2024-12-05 02:16:56','2024-12-05 02:16:56'),('e6b53650-b280-11ef-b086-5254003fef98','e6b48eab-b280-11ef-b086-5254003fef98','ce219550-b27d-11ef-b086-5254003fef98','3dc68b75-b27e-11ef-b086-5254003fef98',2,'2024-12-05 02:16:56','2024-12-05 02:16:56');
/*!40000 ALTER TABLE `question_subquestion_map` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_type`
--

DROP TABLE IF EXISTS `question_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question_type` (
  `id` int NOT NULL,
  `type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_type`
--

LOCK TABLES `question_type` WRITE;
/*!40000 ALTER TABLE `question_type` DISABLE KEYS */;
INSERT INTO `question_type` VALUES (1,'general','2024-11-28 02:55:45','2024-11-28 02:55:45'),(2,'multiple choice','2024-11-28 02:55:45','2024-11-28 02:55:45'),(3,'fill in the blanks','2024-11-28 02:55:45','2024-11-28 02:55:45'),(4,'match the column','2024-11-28 02:55:45','2024-11-28 02:55:45'),(5,'true or false','2024-11-28 02:55:45','2024-11-28 02:55:45'),(6,'subjective','2024-11-28 02:55:45','2024-11-28 02:55:45'),(7,'reason assertion','2024-11-28 02:55:45','2024-11-28 02:55:45');
/*!40000 ALTER TABLE `question_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reason_assertion`
--

DROP TABLE IF EXISTS `reason_assertion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reason_assertion` (
  `id` varchar(36) NOT NULL,
  `question_id` varchar(36) NOT NULL,
  `reason_statement` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `assertion_statement` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `reason_assertion_question_details_FK` (`question_id`),
  CONSTRAINT `reason_assertion_question_details_FK` FOREIGN KEY (`question_id`) REFERENCES `question_details` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reason_assertion`
--

LOCK TABLES `reason_assertion` WRITE;
/*!40000 ALTER TABLE `reason_assertion` DISABLE KEYS */;
INSERT INTO `reason_assertion` VALUES ('896e7207-5fe9-11ef-a6ac-5254003fef98','896db7c8-5fe9-11ef-a6ac-5254003fef98','reason 1','assertion 1','2024-11-28 02:55:50','2024-11-28 02:55:50'),('c9e4d80f-a76b-11ef-a59c-5254003fef98','c9e400e3-a76b-11ef-a59c-5254003fef98','reason 21','assertion 21','2024-11-28 02:55:50','2024-11-28 02:55:50'),('d49e4b86-a76b-11ef-a59c-5254003fef98','d49ddd5b-a76b-11ef-a59c-5254003fef98','reason 31','assertion 31','2024-11-28 02:55:50','2024-11-28 02:55:50'),('ed3aaac7-b27d-11ef-b086-5254003fef98','ed3a6e26-b27d-11ef-b086-5254003fef98','reason 41','assertion 41','2024-12-05 01:55:39','2024-12-05 01:55:39'),('f293f86b-b27d-11ef-b086-5254003fef98','f293c1ab-b27d-11ef-b086-5254003fef98','reason 51','assertion 51','2024-12-05 01:55:48','2024-12-05 01:55:48');
/*!40000 ALTER TABLE `reason_assertion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school`
--

DROP TABLE IF EXISTS `school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `school` (
  `id` varchar(36) NOT NULL,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `logo_filename` text,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='contains records of schools enlisted with app';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school`
--

LOCK TABLES `school` WRITE;
/*!40000 ALTER TABLE `school` DISABLE KEYS */;
INSERT INTO `school` VALUES ('2ff31c49e65e4c0b8d5c43a88918b75b','Doon International School',NULL,'2024-11-28 02:55:53','2024-11-28 02:55:53');
/*!40000 ALTER TABLE `school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject` (
  `id` varchar(36) NOT NULL,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES ('0969b86598d8416bbf188b6b45efc8c3','Chemistry','2024-11-28 02:55:58','2024-11-28 02:55:58'),('38ba8617d88844c5b9a4756a2389f920','Hindi','2024-11-28 02:55:58','2024-11-28 02:55:58'),('42ccc051e7884d7a8f87c9d4c9e988de','Maths','2024-11-28 02:55:58','2024-11-28 02:55:58'),('50368fe987d94411a2643dab5728405d','Social Studies','2024-11-28 02:55:58','2024-11-28 02:55:58'),('6507e3a0c65c43c0977fab55ddf195dc','Physics','2024-11-28 02:55:58','2024-11-28 02:55:58'),('724017b7d2524eb1820287da48067c04','Science','2024-11-28 02:55:58','2024-11-28 02:55:58'),('9c88cfb63ed34e80a8b12c479fbf6b3d','English','2024-11-28 02:55:58','2024-11-28 02:55:58'),('d0772a093f3f47ad9e1a23a940701433','Computer','2024-11-28 02:55:58','2024-11-28 02:55:58'),('efd0ca1eadf547efb3b56740464c95d7','Biology','2024-11-28 02:55:58','2024-11-28 02:55:58'),('f1e5c4d6-f286-4f15-9955-afd6af7ffb05','GK','2024-12-05 03:05:37','2024-12-05 03:05:37');
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test` (
  `id` varchar(36) NOT NULL,
  `file_name` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `school_id` varchar(36) DEFAULT NULL,
  `class_number` int DEFAULT NULL,
  `subject_id` varchar(36) DEFAULT NULL,
  `test_type_id` varchar(36) DEFAULT NULL,
  `section_count` int DEFAULT NULL,
  `time_duration` int NOT NULL,
  `maximum_marks` int NOT NULL,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_test_school_id` (`school_id`),
  KEY `fk_test_class_number` (`class_number`),
  KEY `fk_test_subject_id` (`subject_id`),
  KEY `fk_test_type_id` (`test_type_id`),
  CONSTRAINT `test_class_FK` FOREIGN KEY (`class_number`) REFERENCES `class` (`class_number`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `test_school_FK` FOREIGN KEY (`school_id`) REFERENCES `school` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `test_subject_FK` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `test_test_type_FK` FOREIGN KEY (`test_type_id`) REFERENCES `test_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
INSERT INTO `test` VALUES ('14f634f8-b279-11ef-b086-5254003fef98','test_file_1','2ff31c49e65e4c0b8d5c43a88918b75b',10,'42ccc051e7884d7a8f87c9d4c9e988de','1',5,120,100,'2024-12-05 01:20:58','2024-12-05 02:13:55'),('e6b48eab-b280-11ef-b086-5254003fef98','test_file_2','2ff31c49e65e4c0b8d5c43a88918b75b',10,'9c88cfb63ed34e80a8b12c479fbf6b3d','2',2,120,100,'2024-12-05 02:16:56','2024-12-05 02:16:56');
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_question_map`
--

DROP TABLE IF EXISTS `test_question_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_question_map` (
  `id` varchar(36) NOT NULL,
  `test_id` varchar(36) NOT NULL,
  `question_id` varchar(36) NOT NULL,
  `question_position` int NOT NULL DEFAULT '0',
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_test_ques_map_test_id` (`test_id`),
  KEY `fk_test_ques_map_ques_id` (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_question_map`
--

LOCK TABLES `test_question_map` WRITE;
/*!40000 ALTER TABLE `test_question_map` DISABLE KEYS */;
INSERT INTO `test_question_map` VALUES ('14f69310-b279-11ef-b086-5254003fef98','14f634f8-b279-11ef-b086-5254003fef98','e44baf76-a76a-11ef-a59c-5254003fef98',1,'2024-12-05 01:20:58','2024-12-05 01:20:58'),('14f6c803-b279-11ef-b086-5254003fef98','14f634f8-b279-11ef-b086-5254003fef98','36f54da4-a76a-11ef-a59c-5254003fef98',2,'2024-12-05 01:20:58','2024-12-05 01:20:58'),('14f6e607-b279-11ef-b086-5254003fef98','14f634f8-b279-11ef-b086-5254003fef98','c9e400e3-a76b-11ef-a59c-5254003fef98',3,'2024-12-05 01:20:58','2024-12-05 01:20:58'),('e6b4d38e-b280-11ef-b086-5254003fef98','e6b48eab-b280-11ef-b086-5254003fef98','c374ba34-b27d-11ef-b086-5254003fef98',1,'2024-12-05 02:16:56','2024-12-05 02:16:56'),('e6b4f2ca-b280-11ef-b086-5254003fef98','e6b48eab-b280-11ef-b086-5254003fef98','850546a4-b27d-11ef-b086-5254003fef98',2,'2024-12-05 02:16:56','2024-12-05 02:16:56'),('e6b50845-b280-11ef-b086-5254003fef98','e6b48eab-b280-11ef-b086-5254003fef98','ce219550-b27d-11ef-b086-5254003fef98',3,'2024-12-05 02:16:56','2024-12-05 02:16:56');
/*!40000 ALTER TABLE `test_question_map` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_section_map`
--

DROP TABLE IF EXISTS `test_section_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_section_map` (
  `id` varchar(36) NOT NULL,
  `test_id` varchar(36) NOT NULL,
  `section_number` int NOT NULL DEFAULT '0',
  `initial_ques_number` int NOT NULL DEFAULT (0),
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_test_section_map_test_id` (`test_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_section_map`
--

LOCK TABLES `test_section_map` WRITE;
/*!40000 ALTER TABLE `test_section_map` DISABLE KEYS */;
INSERT INTO `test_section_map` VALUES ('e9fda93b-b280-11ef-b086-5254003fef98','e6b48eab-b280-11ef-b086-5254003fef98',1,1,'2024-12-05 02:17:02','2024-12-05 02:17:02'),('e9fdeef9-b280-11ef-b086-5254003fef98','e6b48eab-b280-11ef-b086-5254003fef98',2,3,'2024-12-05 02:17:02','2024-12-05 02:17:02');
/*!40000 ALTER TABLE `test_section_map` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_type`
--

DROP TABLE IF EXISTS `test_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_type` (
  `id` varchar(36) NOT NULL,
  `type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_type`
--

LOCK TABLES `test_type` WRITE;
/*!40000 ALTER TABLE `test_type` DISABLE KEYS */;
INSERT INTO `test_type` VALUES ('1','end term','2024-11-28 02:56:22','2024-11-28 02:56:22'),('2','periodic','2024-11-28 02:56:22','2024-11-28 02:56:22'),('3','summative','2024-11-28 02:56:22','2024-11-28 02:56:22'),('4','half term','2024-11-28 02:56:22','2024-11-28 02:56:22');
/*!40000 ALTER TABLE `test_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'test_maker'
--

--
-- Dumping routines for database 'test_maker'
--
/*!50003 DROP PROCEDURE IF EXISTS `create_fib_missing_word` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_fib_missing_word`(IN questionId VARCHAR(36), IN word TEXT)
BEGIN
	SET @id = UUID();
	INSERT INTO fib(id, question_id, missing_word, created_on, updated_on)
	VALUES(@id, questionId, word, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
	
	SELECT * FROM fib WHERE id = @id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `create_general_question` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_general_question`(
    IN questionTypeId INT,
    IN subjectId VARCHAR(36),
    IN difficulty VARCHAR(36),
    IN marks INT,
    IN content LONGTEXT
)
BEGIN
    SET @id = UUID();
    INSERT INTO question_details(id, question_type_id, subject_id, difficulty, marks, content, created_on, updated_on)
    VALUES (@id, questionTypeId, subjectId, difficulty, marks, content, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
    
    SELECT * FROM question_details WHERE id = @id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `create_match_a_option` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_match_a_option`(
    IN questionId VARCHAR(36),
    IN optionText TEXT
)
BEGIN
    SET @id = UUID();
    INSERT INTO match_a (id, question_id, match_option, created_on, updated_on)
    VALUES (@id, questionId, optionText, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
    
    SELECT * FROM match_a WHERE id = @id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `create_match_b_option` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_match_b_option`(
    IN questionId VARCHAR(36),
    IN optionText TEXT
)
BEGIN
    SET @id = UUID();
    INSERT INTO match_b (id, question_id, match_option, created_on, updated_on)
    VALUES (@id, questionId, optionText, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
    
    SELECT * FROM match_b WHERE id = @id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `create_mcq_option` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_mcq_option`(
    IN questionId VARCHAR(36),
    IN optionText TEXT
)
BEGIN
    SET @id = UUID();
    INSERT INTO mcq (id, question_id, option_text, created_on, updated_on)
    VALUES (@id, questionId, optionText, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
    
    SELECT * FROM mcq WHERE id = @id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `create_question_images` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_question_images`(
    IN testId VARCHAR(36),
    IN questionId VARCHAR(36),
    IN imagePosition INT,
    IN imageName VARCHAR(50)
)
BEGIN
    SET @id = UUID();
    INSERT INTO question_images
        (id, test_id, question_id, image_position, image_name, created_on, updated_on)
    VALUES
        (@id, testId, questionId, imagePosition, imageName, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
    
    SELECT * FROM question_images WHERE id = @id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `create_question_subquestion_map` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_question_subquestion_map`(
    IN testId VARCHAR(36),
    IN questionId VARCHAR(36),
    IN subquestionId VARCHAR(36),
    IN subquestionNumber INT
)
BEGIN
    SET @id = UUID();
    INSERT INTO question_subquestion_map
        (id, test_id, question_id, subquestion_id, subquestion_number, created_on, updated_on)
    VALUES
        (@id, testId, questionId, subquestionId, subquestionNumber, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
    
    SELECT * FROM question_subquestion_map WHERE id = @id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `create_reason_assertion_question` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_reason_assertion_question`(
    IN questionId VARCHAR(36),
    IN reasonStatement TEXT,
    IN assertionStatement TEXT
)
BEGIN
    SET @id = UUID();
    
    INSERT INTO reason_assertion
        (id, question_id, reason_statement, assertion_statement, created_on, updated_on)
    VALUES
        (@id, questionId, reasonStatement, assertionStatement, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

    SELECT * FROM reason_assertion WHERE id = @id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `create_test` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_test`(
    IN fileName LONGTEXT, 
    IN schoolId VARCHAR(36), 
    IN classNumber INT, 
    IN subjectId VARCHAR(36), 
    IN testTypeId VARCHAR(36), 
    IN sectionCount INT, 
    IN timeDuration INT, 
    IN maximumMarks INT
)
BEGIN
    SET @id = UUID();
    INSERT INTO test
        (id, file_name, school_id, class_number, subject_id, test_type_id, section_count, time_duration, maximum_marks, created_on, updated_on)
    VALUES
        (@id, fileName, schoolId, classNumber, subjectId, testTypeId, sectionCount, timeDuration, maximumMarks, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

    SELECT * FROM test WHERE id = @id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `create_test_question_map` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_test_question_map`(
    IN testId VARCHAR(36),
    IN questionId VARCHAR(36),
    IN questionPosition INT
)
BEGIN
    SET @id = UUID();
    INSERT INTO test_question_map
        (id, test_id, question_id, question_position, created_on, updated_on)
    VALUES
        (@id, testId, questionId, questionPosition, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

    SELECT * FROM test_question_map WHERE id = @id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `create_test_section_map` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_test_section_map`(
    IN testId VARCHAR(36),
    IN sectionNumber INT,
    IN initialQuesNumber INT
)
BEGIN
    SET @id = UUID();
    INSERT INTO test_section_map
        (id, test_id, section_number, initial_ques_number, created_on, updated_on)
    VALUES
        (@id, testId, sectionNumber, initialQuesNumber, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

    SELECT * FROM test_section_map WHERE id = @id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-07  1:04:03
