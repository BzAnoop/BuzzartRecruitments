-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: buzzart_req
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `address` (
  `uid` varchar(50) DEFAULT NULL,
  `address1` text,
  `address2` text,
  `address3` text,
  `pincode` int DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `pa_address1` text,
  `pa_address2` text,
  `pa_address3` text,
  `pa_pincode` int DEFAULT NULL,
  `pa_country` varchar(100) DEFAULT NULL,
  `pa_state` varchar(100) DEFAULT NULL,
  `pa_city` varchar(100) DEFAULT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `id_2` (`id`),
  KEY `fk` (`uid`),
  CONSTRAINT `fk` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES ('Sachin','191-1/5 Shivaji Nagar','Bhopal','Bhopal',4626666,'IN','MP','Bhopal',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1),('azam','199-A Shuvaji Nagar','Bhopal','yyyy',462888,'IN','MP','Bhopal',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2);
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answers`
--

DROP TABLE IF EXISTS `answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answers` (
  `qid` bigint DEFAULT NULL,
  `id` int NOT NULL,
  `ans1` text,
  `ans2` text,
  `ans3` text,
  `ans4` text,
  `status` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answers`
--

LOCK TABLES `answers` WRITE;
/*!40000 ALTER TABLE `answers` DISABLE KEYS */;
INSERT INTO `answers` VALUES (1,1,'16','32','64','None of these above',1),(2,2,'English','PHP','C','All of the above',1),(3,3,'.py','.python','.p','None of these',1),(4,4,'Key','Brackets','Indentation','None of these',1),(5,5,'512, 64, 512','512, 512, 512','64, 512, 64','64, 64, 64',1),(6,6,'{4,5}','{6}','Error as unsupported operand type for set data type','Error as the duplicate item 6 is present in both sets',1),(7,7,'{5,6,7,8,10,11}','{7,8}','Error as unsupported operand type of set data type','{5,6,10,11}',1),(8,8,'( )','[ ]','{ }','set()',1),(9,9,'[1, 3, 5, 7, 8]','[1, 7, 8]','[1, 2, 4, 7, 8]','error',1),(10,10,'list1.addEnd(5)','list1.addLast(5)','list1.append(5)','list1.add(5)',1),(11,11,'A: \"Lydia Hallie\", \"Lydia Hallie\"','B: \" Lydia Hallie\", \" Lydia Hallie\" (\"[13x whitespace]Lydia Hallie\", \"[2x whitespace]Lydia Hallie\")','C: \" Lydia Hallie\", \"Lydia Hallie\" (\"[1x whitespace]Lydia Hallie\", \"Lydia Hallie\")','D: \"Lydia Hallie\", \"Lyd\",',1),(12,12,'A: running index.js, running sum.js, 3','B: running sum.js, running index.js, 3','C: running sum.js, 3, running index.js','D: running index.js, undefined, running sum.js',1),(13,13,'The rigidity of the delivery date','The degree of sociability required for the project','High frustration caused by personal, business, or technological factors that causes friction among team members','The difficulty of the problem to be solved',1),(14,14,'speculation, collaboration, learning','analysis, design, coding',' requirements gathering, adaptive cycle planning, iterative development','all of the mentioned',1),(15,15,'a) Box having dotted bottom outline, solid right outline, double top outline and dashed left outline','b) Box having dotted bottom outline, solid left outline, double top outline and dashed left outline','c) Box having dotted top outline, solid right outline, double bottom outline and dashed left outline','d) Box having dotted top outline, solid left outline, double bottom outline and dashed right outline',1),(16,16,'.panel','.container','.box','.jumbotron',1),(17,17,'.img-circle','.image-circle','.image-rounded','.img-rounded',1),(18,18,'Box having dotted bottom outline, solid right outline, double top outline and dashed left outline','Box having dotted bottom outline, solid left outline, double top outline and dashed left outline','Box having dotted top outline, solid right outline, double bottom outline and dashed left outline',' Box having dotted top outline, solid left outline, double bottom outline and dashed right outline',1),(19,19,' color: red, text-decoration: underline works','only font-style: italic works','color: red, text-decoration: underline and font-style: italic all works',' text-decoration: underline and font-style: italic works',1),(20,20,' Downloading','Checking','Idle','Fallback',1);
/*!40000 ALTER TABLE `answers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answersheet`
--

DROP TABLE IF EXISTS `answersheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answersheet` (`id` bigint NOT NULL,`uid` bigint,`qid` bigint,`cr_ans` int,`ch_ans` int,`ans1` text,`ans2` text,`ans3` text,`ans4` text,`alottime` int,`remtime` int,`submitstatus` tinyint(1),`result` tinyint(1),`marks` int, PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answersheet`
--

LOCK TABLES `answersheet` WRITE;
/*!40000 ALTER TABLE `answersheet` DISABLE KEYS */;
/*!40000 ALTER TABLE `answersheet` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add address',7,'add_address'),(26,'Can change address',7,'change_address'),(27,'Can delete address',7,'delete_address'),(28,'Can view address',7,'view_address'),(29,'Can add answers',8,'add_answers'),(30,'Can change answers',8,'change_answers'),(31,'Can delete answers',8,'delete_answers'),(32,'Can view answers',8,'view_answers'),(33,'Can add experience',9,'add_experience'),(34,'Can change experience',9,'change_experience'),(35,'Can delete experience',9,'delete_experience'),(36,'Can view experience',9,'view_experience'),(37,'Can add qualifications',10,'add_qualifications'),(38,'Can change qualifications',10,'change_qualifications'),(39,'Can delete qualifications',10,'delete_qualifications'),(40,'Can view qualifications',10,'view_qualifications'),(41,'Can add question',11,'add_question'),(42,'Can change question',11,'change_question'),(43,'Can delete question',11,'delete_question'),(44,'Can view question',11,'view_question'),(45,'Can add skills',12,'add_skills'),(46,'Can change skills',12,'change_skills'),(47,'Can delete skills',12,'delete_skills'),(48,'Can view skills',12,'view_skills'),(49,'Can add users',13,'add_users'),(50,'Can change users',13,'change_users'),(51,'Can delete users',13,'delete_users'),(52,'Can view users',13,'view_users');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$390000$9oCNORRja1BVHAaDeMAztG$YZZJX4DGG2efjBvtVq22QgalL8ID0RzirsS02TpRDpQ=','2022-09-25 17:31:08.829039',1,'buzzart','','','',1,1,'2022-09-25 16:20:43.238129');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-09-25 18:01:48.312223','Sachin','Users object (Sachin)',2,'[{\"changed\": {\"fields\": [\"Link\"]}}]',13,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'Recruit','address'),(8,'Recruit','answers'),(9,'Recruit','experience'),(10,'Recruit','qualifications'),(11,'Recruit','question'),(12,'Recruit','skills'),(13,'Recruit','users'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-09-20 14:11:01.161970'),(2,'auth','0001_initial','2022-09-20 14:11:02.104847'),(3,'admin','0001_initial','2022-09-20 14:11:02.325545'),(4,'admin','0002_logentry_remove_auto_add','2022-09-20 14:11:02.337545'),(5,'admin','0003_logentry_add_action_flag_choices','2022-09-20 14:11:02.359549'),(6,'contenttypes','0002_remove_content_type_name','2022-09-20 14:11:02.507549'),(7,'auth','0002_alter_permission_name_max_length','2022-09-20 14:11:02.605579'),(8,'auth','0003_alter_user_email_max_length','2022-09-20 14:11:02.637545'),(9,'auth','0004_alter_user_username_opts','2022-09-20 14:11:02.666549'),(10,'auth','0005_alter_user_last_login_null','2022-09-20 14:11:02.796555'),(11,'auth','0006_require_contenttypes_0002','2022-09-20 14:11:02.804547'),(12,'auth','0007_alter_validators_add_error_messages','2022-09-20 14:11:02.819549'),(13,'auth','0008_alter_user_username_max_length','2022-09-20 14:11:02.933546'),(14,'auth','0009_alter_user_last_name_max_length','2022-09-20 14:11:03.015545'),(15,'auth','0010_alter_group_name_max_length','2022-09-20 14:11:03.051548'),(16,'auth','0011_update_proxy_permissions','2022-09-20 14:11:03.066545'),(17,'auth','0012_alter_user_first_name_max_length','2022-09-20 14:11:03.169544'),(18,'sessions','0001_initial','2022-09-20 14:11:03.220551'),(19,'Recruit','0001_initial','2022-09-21 16:33:44.662896');
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
INSERT INTO `django_session` VALUES ('23mox9hkdpf9ok9esf3lspz9qoxz9pcp','eyJfc2Vzc2lvbl9leHBpcnkiOjAsImxhc3RfYWN0aXZpdHkiOjE2fQ:1oeukm:eqBvG48dRXn8GJLwN5UM7oVNmuSXLzvLOCE94BobO8M','2022-10-16 08:55:16.701679'),('3glrqubd0l6sl5orhkihk70cv2071iwd','eyJfc2Vzc2lvbl9leHBpcnkiOjB9:1oevFy:iWZGmhVXKywBSPTctXEAqxme2UWLYQEObMUPZAhqq10','2022-10-16 09:27:30.164722'),('5bamedwgj740pl6ihml3vvnkivp5jzm6','eyJVc2VySUQiOiJTYWNoaW4iLCJfc2Vzc2lvbl9leHBpcnkiOjB9:1odQJz:wOq54kz1TJzHd3fwCQVvKGfQ6kuzRxr4Qdl5rZW7kes','2022-10-12 06:13:27.910756'),('7e7ua8lm337jlug7csyknuosi5luxf6y','eyJfc2Vzc2lvbl9leHBpcnkiOjB9:1oewhz:52UvnblQMsStIzAHBJf8rHAGRtShRN7-MKbSlMDns_I','2022-10-16 11:00:31.015035'),('a5ypvh5ty3mtezr4ychsiqyhm0f7i20f','eyJVc2VySUQiOiJTYWNoaW4iLCJfc2Vzc2lvbl9leHBpcnkiOjB9:1odQMB:RfMJ6XImM0EQXmF73B1V4r8blxXYb5_0DIwc7vHa4ww','2022-10-12 06:15:43.520876'),('ds14f4711u9ddetx7ibxnqjyuvmsb4ku','eyJsYXN0X2FjdGl2aXR5IjoyOCwiVXNlcklEIjoiU2FjaGluIiwiX3Nlc3Npb25fZXhwaXJ5IjowfQ:1oevC4:h5_xQNHEvEkVgqbRbE_76zhssahQemOAjeyRNAA7b4w','2022-10-16 09:23:28.426016'),('et7yudus7uf4mteifwxrwp7wxbx5m68a','eyJfc2Vzc2lvbl9leHBpcnkiOjAsIlVzZXJJRCI6IlNhY2hpbiJ9:1oeXzE:mJ0lldGKe0iWBOKNYI96wCNrccxedyoV80LGCjh8xUg','2022-10-15 08:36:40.759966'),('hq2nwfqzowoswyg75icv91geqjsa7y33','eyJsYXN0X2FjdGl2aXR5IjozOH0:1of2je:27ConD3J-tmF9O7Mf_gddYp8ZyA1sPaIiabLx60pMOI','2022-10-16 17:26:38.732521'),('lh18y9sl7fezn1x9jqvgw75o0239cjfb','eyJsYXN0X2FjdGl2aXR5Ijo2LCJVc2VySUQiOiJTYWNoaW4iLCJfc2Vzc2lvbl9leHBpcnkiOjAsInRlc3QiOnRydWV9:1ofDfW:6nDYcY5yMBbDCqrKFvuweIMVJ5LBQKvVHVfIR0RkMP0','2022-10-17 05:07:06.062113'),('looeqk88s6hapoqv0leov7vb9nk77zze','eyJfc2Vzc2lvbl9leHBpcnkiOjAsImxhc3RfYWN0aXZpdHkiOjE4LCJVc2VySUQiOiJTYWNoaW4ifQ:1oev74:BemtmI9ZKOU8M1GVPjwEpAoGSQ8bEB9tOGPk0WFIhq4','2022-10-16 09:18:18.029894'),('muu7hwy9s4a2yj09d85wcj0p9rrnvk00','eyJVc2VySUQiOiJTYWNoaW4iLCJfc2Vzc2lvbl9leHBpcnkiOjB9:1oetrr:fXd9p0rg75EoWVmZUAU574kahZUyPPUWXZbCgqPSuac','2022-10-16 07:58:31.773994'),('nz3jegity0n7ajolsrjuld0thtu7vd0u','eyJsYXN0X2FjdGl2aXR5IjowLCJVc2VySUQiOiJTYWNoaW4iLCJfc2Vzc2lvbl9leHBpcnkiOjB9:1oeucm:yLl_tf0clTCNsGvH04REZiPs3puw0UZ_uYlhIK8TVlA','2022-10-16 08:47:00.855710'),('or92o2lqmup1sgnvae07i0z0dl0celcs','eyJVc2VySUQiOiJTYWNoaW4iLCJfc2Vzc2lvbl9leHBpcnkiOjB9:1oeZQI:1_gvtjihuQfcBHs00YwdFmPvE9Jd6R8GN5SW4TwwnA8','2022-10-15 10:08:42.958017'),('ot9oghbmcb9dnvm24dkh9qwn2ypatk38','eyJsYXN0X2FjdGl2aXR5IjoxNiwiVXNlcklEIjoiU2FjaGluIiwiX3Nlc3Npb25fZXhwaXJ5IjowfQ:1oeub6:nkb36knJW5NcwAFKAT-Os7PHbN9rfgkfmo_BV7TSxFE','2022-10-16 08:45:16.802819'),('vzsmw229kknedn7e1ygxwtb15878a092','eyJsYXN0X2FjdGl2aXR5IjoyNywiVXNlcklEIjoiU2FjaGluIiwiX3Nlc3Npb25fZXhwaXJ5IjowfQ:1oeuf9:Rlmk-LZwobYRbQ8qWoUwC7Aez82b1YwhPMQ3pKLAYTQ','2022-10-16 08:49:27.754558'),('y6zh7560vquhlqtb9oedqqjp35xriza8','eyJsYXN0X2FjdGl2aXR5Ijo1MywiVXNlcklEIjoiU2FjaGluIiwiX3Nlc3Npb25fZXhwaXJ5IjowfQ:1oewp7:I0u1KljfGuh--d3wXcjWbPgGs6UlTG2zHoOmMBgOvd8','2022-10-16 11:07:53.497811'),('z8bi966gr0n3brz9ze56flhukmwptd93','eyJfc2Vzc2lvbl9leHBpcnkiOjAsInRlc3QiOmZhbHNlLCJsYXN0X2FjdGl2aXR5Ijo5fQ:1of2ED:NCVHnqo0mjonKcQLofCFiVuzYN8xNjp6Ca7B5IoBxKA','2022-10-16 16:54:09.676742');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experience`
--

DROP TABLE IF EXISTS `experience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experience` (
  `uid` varchar(50) DEFAULT NULL,
  `title` text,
  `company` text,
  `years` int DEFAULT NULL,
  `months` int DEFAULT NULL,
  `from_date` int DEFAULT NULL,
  `to_date` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `id_2` (`id`),
  KEY `fk2` (`uid`),
  CONSTRAINT `fk2` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experience`
--

LOCK TABLES `experience` WRITE;
/*!40000 ALTER TABLE `experience` DISABLE KEYS */;
/*!40000 ALTER TABLE `experience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qualifications`
--

DROP TABLE IF EXISTS `qualifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qualifications` (
  `uid` varchar(50) DEFAULT NULL,
  `qualification` text,
  `qualification_status` varchar(50) DEFAULT NULL,
  `university_name` text,
  `institute_name` text,
  `from_date` date DEFAULT NULL,
  `to_date` date DEFAULT NULL,
  `percentage` int DEFAULT NULL,
  `grade` varchar(2) DEFAULT NULL,
  `year` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `id_2` (`id`),
  KEY `fk3` (`uid`),
  CONSTRAINT `fk3` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qualifications`
--

LOCK TABLES `qualifications` WRITE;
/*!40000 ALTER TABLE `qualifications` DISABLE KEYS */;
/*!40000 ALTER TABLE `qualifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `qid` bigint NOT NULL,
  `que` text,
  `subject` varchar(100) DEFAULT NULL,
  `level` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  `cr_ans` int DEFAULT NULL,
  PRIMARY KEY (`qid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,'What is the maximum possible length of an identifier?','PYTHON',1,1,4),(2,'In which language is Python written?','PYTHON',1,1,3),(3,'Which one of the following is the correct extension of the Python file?','PYTHON',1,1,1),(4,'What do we use to define a block of code in Python language?','PYTHON',1,1,3),(5,'What are the values of the following Python expressions?\r\n\r\n 2**(3**2)\r\n (2**3)**2\r\n 2**3**2','PYTHON',2,1,1),(6,'What will be the output of the following Python code?\n\n>>> a={4,5,6}\n>>> b={2,8,6}\n>>> a-b','PYTHON',2,1,1),(7,'What will be the output of the following Python code?\n\n>>> a={5,6,7,8}\n>>> b={7,8,10,11}\n>>> a^b','PYTHON',2,1,4),(8,'Which of the following statements is used to create an empty set in Python?','PYTHON',3,1,4),(9,' What will be the value of ?result? in following Python program?\r\n\r\nlist1 = [1,2,3,4]\r\nlist2 = [2,4,5,6]\r\nlist3 = [2,6,7,8]\r\nresult = list()\r\nresult.extend(i for i in list1 if i not in (list2+list3) and i not in result)\r\nresult.extend(i for i in list2 if i not in (list1+list3) and i not in result)\r\nresult.extend(i for i in list3 if i not in (list1+list2) and i not in result)','PYTHON',3,1,1),(10,'To add a new element to a list we use which Python command?','PYTHON',3,1,3);
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skills`
--

DROP TABLE IF EXISTS `skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skills` (
  `uid` varchar(50) DEFAULT NULL,
  `skill_name` text,
  `skill_type` int DEFAULT NULL,
  `skill_level` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `id_2` (`id`),
  KEY `fk1` (`uid`),
  CONSTRAINT `fk1` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills`
--

LOCK TABLES `skills` WRITE;
/*!40000 ALTER TABLE `skills` DISABLE KEYS */;
/*!40000 ALTER TABLE `skills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `uid` varchar(50) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `mobile` int DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `status` int DEFAULT NULL,
  `t_experience` bigint DEFAULT NULL,
  `previous_org` varchar(100) DEFAULT NULL,
  `link` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('azam','Azam','Khan',898998,'azam@gmail.com','azam123','1997-06-26',NULL,2,'ABC Ltd.',0),('Sachin','Sachin','Sharma',928828271,'sachin@gmail.com','Sachinmehta','1995-06-23',NULL,5,'Sofcon',1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-03  7:32:53
