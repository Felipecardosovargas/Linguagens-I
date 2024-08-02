-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: livraria
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `livro`
--

DROP TABLE IF EXISTS `livro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `livro` (
  `Cod_livro` int NOT NULL AUTO_INCREMENT,
  `Titulo` varchar(255) NOT NULL,
  `Ano_publicacao` date DEFAULT NULL,
  `Autor` varchar(255) DEFAULT NULL,
  `Editora` int DEFAULT NULL,
  `Categoria` varchar(255) DEFAULT NULL,
  `Valor` decimal(10,2) NOT NULL,
  `ISBN` bigint NOT NULL,
  `FK_Editora_Cod_editora` int DEFAULT NULL,
  `FK_ESTOQUE_Cod_livro` int DEFAULT NULL,
  `FK_ESTOQUE_Cod_editora` int DEFAULT NULL,
  PRIMARY KEY (`Cod_livro`),
  KEY `Editora` (`Editora`),
  KEY `FK_LIVRO_Editora` (`FK_Editora_Cod_editora`),
  KEY `FK_LIVRO_Estoque` (`FK_ESTOQUE_Cod_livro`,`FK_ESTOQUE_Cod_editora`),
  CONSTRAINT `FK_LIVRO_Editora` FOREIGN KEY (`FK_Editora_Cod_editora`) REFERENCES `editora` (`Cod_editora`) ON DELETE RESTRICT,
  CONSTRAINT `FK_LIVRO_Estoque` FOREIGN KEY (`FK_ESTOQUE_Cod_livro`, `FK_ESTOQUE_Cod_editora`) REFERENCES `estoque` (`Cod_livro`, `Cod_editora`) ON DELETE CASCADE,
  CONSTRAINT `livro_ibfk_1` FOREIGN KEY (`Editora`) REFERENCES `editora` (`Cod_editora`) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `livro`
--

LOCK TABLES `livro` WRITE;
/*!40000 ALTER TABLE `livro` DISABLE KEYS */;
/*!40000 ALTER TABLE `livro` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-25 20:19:00
