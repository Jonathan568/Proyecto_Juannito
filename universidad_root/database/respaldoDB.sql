CREATE DATABASE  IF NOT EXISTS `proyecto_universitario` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `proyecto_universitario`;
-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: proyecto_universitario
-- ------------------------------------------------------
-- Server version	8.0.45

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
-- Table structure for table `alumno`
--

DROP TABLE IF EXISTS `alumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumno` (
  `idAlumno` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) NOT NULL,
  `apellido_paterno` varchar(45) NOT NULL,
  `matricula` varchar(45) NOT NULL,
  `estatus` enum('activo','inactivo') NOT NULL,
  `idUsuario` int DEFAULT NULL,
  PRIMARY KEY (`idAlumno`),
  UNIQUE KEY `matricula` (`matricula`),
  KEY `idUsuario` (`idUsuario`),
  CONSTRAINT `alumno_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`idUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno`
--

LOCK TABLES `alumno` WRITE;
/*!40000 ALTER TABLE `alumno` DISABLE KEYS */;
/*!40000 ALTER TABLE `alumno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alumno_grupo`
--

DROP TABLE IF EXISTS `alumno_grupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumno_grupo` (
  `idAlumno` int NOT NULL,
  `idGrupo` int NOT NULL,
  `idPeriodo` int NOT NULL,
  PRIMARY KEY (`idAlumno`,`idGrupo`,`idPeriodo`),
  KEY `idGrupo` (`idGrupo`),
  KEY `idPeriodo` (`idPeriodo`),
  CONSTRAINT `alumno_grupo_ibfk_1` FOREIGN KEY (`idAlumno`) REFERENCES `alumno` (`idAlumno`),
  CONSTRAINT `alumno_grupo_ibfk_2` FOREIGN KEY (`idGrupo`) REFERENCES `grupo` (`idGrupo`),
  CONSTRAINT `alumno_grupo_ibfk_3` FOREIGN KEY (`idPeriodo`) REFERENCES `periodo_escolar` (`idPeriodo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno_grupo`
--

LOCK TABLES `alumno_grupo` WRITE;
/*!40000 ALTER TABLE `alumno_grupo` DISABLE KEYS */;
/*!40000 ALTER TABLE `alumno_grupo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alumno_licenciatura`
--

DROP TABLE IF EXISTS `alumno_licenciatura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumno_licenciatura` (
  `idAlumno` int NOT NULL,
  `idLicenciatura` int NOT NULL,
  PRIMARY KEY (`idAlumno`,`idLicenciatura`),
  KEY `idLicenciatura` (`idLicenciatura`),
  CONSTRAINT `alumno_licenciatura_ibfk_1` FOREIGN KEY (`idAlumno`) REFERENCES `alumno` (`idAlumno`),
  CONSTRAINT `alumno_licenciatura_ibfk_2` FOREIGN KEY (`idLicenciatura`) REFERENCES `licenciatura` (`idLicenciatura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno_licenciatura`
--

LOCK TABLES `alumno_licenciatura` WRITE;
/*!40000 ALTER TABLE `alumno_licenciatura` DISABLE KEYS */;
/*!40000 ALTER TABLE `alumno_licenciatura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alumno_semestre`
--

DROP TABLE IF EXISTS `alumno_semestre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumno_semestre` (
  `idAlumno` int NOT NULL,
  `idSemestre` int NOT NULL,
  `idPeriodo` int NOT NULL,
  PRIMARY KEY (`idAlumno`,`idSemestre`,`idPeriodo`),
  KEY `idSemestre` (`idSemestre`),
  KEY `idPeriodo` (`idPeriodo`),
  CONSTRAINT `alumno_semestre_ibfk_1` FOREIGN KEY (`idAlumno`) REFERENCES `alumno` (`idAlumno`),
  CONSTRAINT `alumno_semestre_ibfk_2` FOREIGN KEY (`idSemestre`) REFERENCES `semestre` (`idSemestre`),
  CONSTRAINT `alumno_semestre_ibfk_3` FOREIGN KEY (`idPeriodo`) REFERENCES `periodo_escolar` (`idPeriodo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno_semestre`
--

LOCK TABLES `alumno_semestre` WRITE;
/*!40000 ALTER TABLE `alumno_semestre` DISABLE KEYS */;
/*!40000 ALTER TABLE `alumno_semestre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',3,'add_permission'),(6,'Can change permission',3,'change_permission'),(7,'Can delete permission',3,'delete_permission'),(8,'Can view permission',3,'view_permission'),(9,'Can add group',2,'add_group'),(10,'Can change group',2,'change_group'),(11,'Can delete group',2,'delete_group'),(12,'Can view group',2,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add alumno',7,'add_alumno'),(26,'Can change alumno',7,'change_alumno'),(27,'Can delete alumno',7,'delete_alumno'),(28,'Can view alumno',7,'view_alumno'),(29,'Can add usuario',8,'add_usuario'),(30,'Can change usuario',8,'change_usuario'),(31,'Can delete usuario',8,'delete_usuario'),(32,'Can view usuario',8,'view_usuario'),(33,'Can add cargo alumno',9,'add_cargoalumno'),(34,'Can change cargo alumno',9,'change_cargoalumno'),(35,'Can delete cargo alumno',9,'delete_cargoalumno'),(36,'Can view cargo alumno',9,'view_cargoalumno'),(37,'Can add concepto',10,'add_concepto'),(38,'Can change concepto',10,'change_concepto'),(39,'Can delete concepto',10,'delete_concepto'),(40,'Can view concepto',10,'view_concepto'),(41,'Can add pago',11,'add_pago'),(42,'Can change pago',11,'change_pago'),(43,'Can delete pago',11,'delete_pago'),(44,'Can view pago',11,'view_pago'),(45,'Can add libro',12,'add_libro'),(46,'Can change libro',12,'change_libro'),(47,'Can delete libro',12,'delete_libro'),(48,'Can view libro',12,'view_libro'),(49,'Can add libro fisico',13,'add_librofisico'),(50,'Can change libro fisico',13,'change_librofisico'),(51,'Can delete libro fisico',13,'delete_librofisico'),(52,'Can view libro fisico',13,'view_librofisico'),(53,'Can add prestamo',14,'add_prestamo'),(54,'Can change prestamo',14,'change_prestamo'),(55,'Can delete prestamo',14,'delete_prestamo'),(56,'Can view prestamo',14,'view_prestamo'),(57,'Can add alumno grupo',15,'add_alumnogrupo'),(58,'Can change alumno grupo',15,'change_alumnogrupo'),(59,'Can delete alumno grupo',15,'delete_alumnogrupo'),(60,'Can view alumno grupo',15,'view_alumnogrupo'),(61,'Can add grupo',16,'add_grupo'),(62,'Can change grupo',16,'change_grupo'),(63,'Can delete grupo',16,'delete_grupo'),(64,'Can view grupo',16,'view_grupo'),(65,'Can add licenciatura',17,'add_licenciatura'),(66,'Can change licenciatura',17,'change_licenciatura'),(67,'Can delete licenciatura',17,'delete_licenciatura'),(68,'Can view licenciatura',17,'view_licenciatura'),(69,'Can add periodo escolar',18,'add_periodoescolar'),(70,'Can change periodo escolar',18,'change_periodoescolar'),(71,'Can delete periodo escolar',18,'delete_periodoescolar'),(72,'Can view periodo escolar',18,'view_periodoescolar'),(73,'Can add semestre',19,'add_semestre'),(74,'Can change semestre',19,'change_semestre'),(75,'Can delete semestre',19,'delete_semestre'),(76,'Can view semestre',19,'view_semestre');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$1200000$idn1stQuvqUnxyKxGgZ1F7$0JZ37zX6+ZTdl+c5Uggu11YRKAcU5hbVtGthtKvCKsw=','2026-05-04 23:46:25.740438',1,'Jonathan','','','jon.gr2020@gmail.com',1,1,'2026-05-04 23:39:01.892109'),(2,'pbkdf2_sha256$1200000$t2Js3DSZS9NFg8dsxLgs7O$74wYbUxFUcqPaaMG9LydqKfBR5aP3110n6/kczvPOIM=','2026-05-04 23:49:29.063400',0,'Kinari_Admin','Kinari','','',1,1,'2026-05-04 23:44:25.000000'),(3,'pbkdf2_sha256$1200000$lreNI2F7kxbv9HE7DAAtFi$lLw/zzEMCl3kodbzM1XNkUQG0FP0V4JdtN+AAn73mXM=',NULL,0,'Emmanuel_Admin','','','',1,1,'2026-05-04 23:45:01.000000'),(4,'pbkdf2_sha256$1200000$fZAFv1Y8ov9xarfnW7GXj7$YB/rnLFd+nMv0tuOmn3BcpclBT4RRuZPyHyp8FWdB68=','2026-05-04 23:46:10.265273',0,'Julio','','','',0,1,'2026-05-04 23:45:33.535023'),(5,'pbkdf2_sha256$1200000$EendJt8r4dLqkyC74eLRUm$/gx7vrYpjalucu7kkopGJDTIl9oboRBv9qRn7Enk8jk=',NULL,0,'Josmar','','','',0,1,'2026-05-04 23:47:13.929541'),(6,'pbkdf2_sha256$1200000$DOYt0pFuthWFms9WKkGgcy$dUhYywurDLAGF3DRjsBngd9ZZvicnTdTmv0MHVp6P3A=',NULL,0,'Vanessa','','','',0,1,'2026-05-04 23:47:37.007580'),(7,'pbkdf2_sha256$1200000$D68J2qnmmdEU3Bum15YQ5U$Ga9K2O6M2f9SF7yEuH89MRFwoNHIqP9s+IM4cn2rmyU=',NULL,0,'Tania','','','',0,1,'2026-05-04 23:48:10.861600'),(8,'pbkdf2_sha256$1200000$IKpclq6tZaY7oe92zgWU31$XCYgiI88x6PpvGHmsan8yBDmbOIdFeEDIV8Pg26FhP0=',NULL,0,'Vladimir','','','',0,1,'2026-05-04 23:48:33.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargo_alumno`
--

DROP TABLE IF EXISTS `cargo_alumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cargo_alumno` (
  `idCargo` int NOT NULL AUTO_INCREMENT,
  `idAlumno` int DEFAULT NULL,
  `idConcepto` int DEFAULT NULL,
  `idPago` int DEFAULT NULL,
  `monto` decimal(10,2) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `estatus` enum('pendiente','pagado') DEFAULT NULL,
  PRIMARY KEY (`idCargo`),
  KEY `idAlumno` (`idAlumno`),
  KEY `idConcepto` (`idConcepto`),
  KEY `idPago` (`idPago`),
  CONSTRAINT `cargo_alumno_ibfk_1` FOREIGN KEY (`idAlumno`) REFERENCES `alumno` (`idAlumno`),
  CONSTRAINT `cargo_alumno_ibfk_2` FOREIGN KEY (`idConcepto`) REFERENCES `concepto` (`idConcepto`),
  CONSTRAINT `cargo_alumno_ibfk_3` FOREIGN KEY (`idPago`) REFERENCES `pago` (`idPago`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargo_alumno`
--

LOCK TABLES `cargo_alumno` WRITE;
/*!40000 ALTER TABLE `cargo_alumno` DISABLE KEYS */;
/*!40000 ALTER TABLE `cargo_alumno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `concepto`
--

DROP TABLE IF EXISTS `concepto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `concepto` (
  `idConcepto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  PRIMARY KEY (`idConcepto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `concepto`
--

LOCK TABLES `concepto` WRITE;
/*!40000 ALTER TABLE `concepto` DISABLE KEYS */;
/*!40000 ALTER TABLE `concepto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2026-05-04 23:44:26.535128','2','Kinari_Admin',1,'[{\"added\": {}}]',4,1),(2,'2026-05-04 23:44:39.814112','2','Kinari_Admin',2,'[{\"changed\": {\"fields\": [\"First name\", \"Staff status\"]}}]',4,1),(3,'2026-05-04 23:45:02.027010','3','Emmanuel_Admin',1,'[{\"added\": {}}]',4,1),(4,'2026-05-04 23:45:10.236005','3','Emmanuel_Admin',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1),(5,'2026-05-04 23:45:34.191757','4','Julio',1,'[{\"added\": {}}]',4,1),(6,'2026-05-04 23:47:14.585743','5','Josmar',1,'[{\"added\": {}}]',4,1),(7,'2026-05-04 23:47:37.672893','6','Vanessa',1,'[{\"added\": {}}]',4,1),(8,'2026-05-04 23:48:11.518158','7','Tania',1,'[{\"added\": {}}]',4,1),(9,'2026-05-04 23:48:34.543139','8','Vladimir',1,'[{\"added\": {}}]',4,1),(10,'2026-05-04 23:48:40.411552','8','Vladimir',2,'[]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(12,'Biblioteca','libro'),(13,'Biblioteca','librofisico'),(14,'Biblioteca','prestamo'),(5,'contenttypes','contenttype'),(15,'ControlEscolar','alumnogrupo'),(16,'ControlEscolar','grupo'),(17,'ControlEscolar','licenciatura'),(18,'ControlEscolar','periodoescolar'),(19,'ControlEscolar','semestre'),(9,'Finanzas','cargoalumno'),(10,'Finanzas','concepto'),(11,'Finanzas','pago'),(6,'sessions','session'),(7,'Usuarios','alumno'),(8,'Usuarios','usuario');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Biblioteca','0001_initial','2026-05-04 23:32:16.942475'),(2,'Usuarios','0001_initial','2026-05-04 23:32:16.949007'),(3,'ControlEscolar','0001_initial','2026-05-04 23:32:16.953322'),(4,'Finanzas','0001_initial','2026-05-04 23:32:16.956790'),(5,'contenttypes','0001_initial','2026-05-04 23:32:16.983498'),(6,'auth','0001_initial','2026-05-04 23:32:17.299306'),(7,'admin','0001_initial','2026-05-04 23:32:17.385919'),(8,'admin','0002_logentry_remove_auto_add','2026-05-04 23:32:17.392258'),(9,'admin','0003_logentry_add_action_flag_choices','2026-05-04 23:32:17.398912'),(10,'contenttypes','0002_remove_content_type_name','2026-05-04 23:32:17.470604'),(11,'auth','0002_alter_permission_name_max_length','2026-05-04 23:32:17.509048'),(12,'auth','0003_alter_user_email_max_length','2026-05-04 23:32:17.527977'),(13,'auth','0004_alter_user_username_opts','2026-05-04 23:32:17.533634'),(14,'auth','0005_alter_user_last_login_null','2026-05-04 23:32:17.570842'),(15,'auth','0006_require_contenttypes_0002','2026-05-04 23:32:17.572706'),(16,'auth','0007_alter_validators_add_error_messages','2026-05-04 23:32:17.578394'),(17,'auth','0008_alter_user_username_max_length','2026-05-04 23:32:17.625443'),(18,'auth','0009_alter_user_last_name_max_length','2026-05-04 23:32:17.668021'),(19,'auth','0010_alter_group_name_max_length','2026-05-04 23:32:17.684537'),(20,'auth','0011_update_proxy_permissions','2026-05-04 23:32:17.697652'),(21,'auth','0012_alter_user_first_name_max_length','2026-05-04 23:32:17.741541'),(22,'sessions','0001_initial','2026-05-04 23:32:17.765875');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupo`
--

DROP TABLE IF EXISTS `grupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grupo` (
  `idGrupo` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`idGrupo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupo`
--

LOCK TABLES `grupo` WRITE;
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libro`
--

DROP TABLE IF EXISTS `libro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libro` (
  `idLibro` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) DEFAULT NULL,
  `autor` varchar(100) DEFAULT NULL,
  `isbn` varchar(13) DEFAULT NULL,
  `editorial` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idLibro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libro`
--

LOCK TABLES `libro` WRITE;
/*!40000 ALTER TABLE `libro` DISABLE KEYS */;
/*!40000 ALTER TABLE `libro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libro_fisico`
--

DROP TABLE IF EXISTS `libro_fisico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libro_fisico` (
  `idLibroFisico` int NOT NULL AUTO_INCREMENT,
  `codigo_barras` varchar(50) DEFAULT NULL,
  `estado` enum('disponible','prestado','danado') DEFAULT NULL,
  `idLibro` int DEFAULT NULL,
  PRIMARY KEY (`idLibroFisico`),
  KEY `idLibro` (`idLibro`),
  CONSTRAINT `libro_fisico_ibfk_1` FOREIGN KEY (`idLibro`) REFERENCES `libro` (`idLibro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libro_fisico`
--

LOCK TABLES `libro_fisico` WRITE;
/*!40000 ALTER TABLE `libro_fisico` DISABLE KEYS */;
/*!40000 ALTER TABLE `libro_fisico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `licenciatura`
--

DROP TABLE IF EXISTS `licenciatura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `licenciatura` (
  `idLicenciatura` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `abreviatura` varchar(10) NOT NULL,
  PRIMARY KEY (`idLicenciatura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `licenciatura`
--

LOCK TABLES `licenciatura` WRITE;
/*!40000 ALTER TABLE `licenciatura` DISABLE KEYS */;
/*!40000 ALTER TABLE `licenciatura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pago`
--

DROP TABLE IF EXISTS `pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pago` (
  `idPago` int NOT NULL AUTO_INCREMENT,
  `fecha` datetime DEFAULT NULL,
  `monto` decimal(10,2) DEFAULT NULL,
  `estatus` enum('pendiente','pagado','cancelado') DEFAULT NULL,
  `folio` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idPago`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pago`
--

LOCK TABLES `pago` WRITE;
/*!40000 ALTER TABLE `pago` DISABLE KEYS */;
/*!40000 ALTER TABLE `pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `periodo_escolar`
--

DROP TABLE IF EXISTS `periodo_escolar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `periodo_escolar` (
  `idPeriodo` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(15) DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  PRIMARY KEY (`idPeriodo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `periodo_escolar`
--

LOCK TABLES `periodo_escolar` WRITE;
/*!40000 ALTER TABLE `periodo_escolar` DISABLE KEYS */;
/*!40000 ALTER TABLE `periodo_escolar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prestamo`
--

DROP TABLE IF EXISTS `prestamo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prestamo` (
  `idPrestamo` int NOT NULL AUTO_INCREMENT,
  `idAlumno` int DEFAULT NULL,
  `idLibroFisico` int DEFAULT NULL,
  `fecha_salida` datetime DEFAULT NULL,
  `fecha_devolucion` datetime DEFAULT NULL,
  `estatus` enum('activo','devuelto','retrasado') DEFAULT NULL,
  PRIMARY KEY (`idPrestamo`),
  KEY `idAlumno` (`idAlumno`),
  KEY `idLibroFisico` (`idLibroFisico`),
  CONSTRAINT `prestamo_ibfk_1` FOREIGN KEY (`idAlumno`) REFERENCES `alumno` (`idAlumno`),
  CONSTRAINT `prestamo_ibfk_2` FOREIGN KEY (`idLibroFisico`) REFERENCES `libro_fisico` (`idLibroFisico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestamo`
--

LOCK TABLES `prestamo` WRITE;
/*!40000 ALTER TABLE `prestamo` DISABLE KEYS */;
/*!40000 ALTER TABLE `prestamo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `semestre`
--

DROP TABLE IF EXISTS `semestre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `semestre` (
  `idSemestre` int NOT NULL AUTO_INCREMENT,
  `numero` tinyint NOT NULL,
  PRIMARY KEY (`idSemestre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `semestre`
--

LOCK TABLES `semestre` WRITE;
/*!40000 ALTER TABLE `semestre` DISABLE KEYS */;
/*!40000 ALTER TABLE `semestre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `rol` enum('admin','alumno') NOT NULL,
  PRIMARY KEY (`idUsuario`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-04 18:08:23
