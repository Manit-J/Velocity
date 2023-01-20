-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: velocity
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `citenary`
--

DROP TABLE IF EXISTS `citenary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citenary` (
  `SNo` int(11) DEFAULT NULL,
  `DOA` date DEFAULT NULL,
  `No_Of_Days` int(11) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `sights` varchar(5000) DEFAULT NULL,
  `place_of_stay` varchar(5000) DEFAULT NULL,
  `transport` varchar(50) DEFAULT NULL,
  `cost` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citenary`
--

LOCK TABLES `citenary` WRITE;
/*!40000 ALTER TABLE `citenary` DISABLE KEYS */;
/*!40000 ALTER TABLE `citenary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cities` (
  `city` varchar(50) DEFAULT NULL,
  `city_id` varchar(50) NOT NULL,
  `vcost_per_day` int(11) DEFAULT NULL,
  PRIMARY KEY (`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES ('Mumbai','v01',4421),('Delhi','v02',2463),('Ahemdabad','v03',3456),('Chennai','v04',2344),('Jaipur','v05',1045),('Pune','v06',4023),('Patna','v07',1289),('Agra','v08',2345),('Ranchi','v09',2445),('Raipur','v10',2321),('Velocity Addition','v11',7000),('Velocity Add 2','v12',3908);
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotels`
--

DROP TABLE IF EXISTS `hotels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hotels` (
  `city_id` varchar(50) DEFAULT NULL,
  `hotel` varchar(50) DEFAULT NULL,
  `stay_cost` int(11) DEFAULT NULL,
  `hotel_id` varchar(50) NOT NULL,
  PRIMARY KEY (`hotel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotels`
--

LOCK TABLES `hotels` WRITE;
/*!40000 ALTER TABLE `hotels` DISABLE KEYS */;
INSERT INTO `hotels` VALUES ('v01','Taj Hotel',4000,'h1'),('v04','Taj Club House',4000,'h10'),('v04','ITC Grand Chola',4000,'h11'),('v04','Trident Chennai',4000,'h12'),('v05','Shahpura House',4000,'h13'),('v05','Moustache Hotel',4000,'h14'),('v05','Umaid Bhawan-Heritage Style Hotel',4000,'h15'),('v06','Conrad Pune Koregaon Park by Hilton',4000,'h16'),('v06','The Orchid Hotel Hinjewadi Pune',4000,'h17'),('v06','Hyatt Pune',4000,'h18'),('v07','The Lotus Valley Inn',4000,'h19'),('v01','Trident Nariman Point',4000,'h2'),('v07','The  Amalfi Grand',4000,'h20'),('v07','The  Aalcajars Inn',4000,'h21'),('v08','Taj Hotel and Convention Centre Agra',4000,'h22'),('v08','The Coral Court Homestay',4000,'h23'),('v09','Radisson Blu Hotel',4000,'h25'),('v09','Le lac Sarovar Portico',4000,'h26'),('v09','Hotel Arham Inn',4000,'h27'),('v10','The Silver Ferns',4000,'h28'),('v10','The Lemon Green Inn',4000,'h29'),('v01','The Oberoi Mumbai',4000,'h3'),('v10','The Counrty Inn And Suite by Radisson',4000,'h30'),('v02','Taj Palace',4000,'h4'),('v02','Radisson Blu Plaza',4000,'h5'),('v02','The Leela Palace',4000,'h6'),('v03','Hyatt Regency',4000,'h7'),('v03','Hotel Alka Inn',4000,'h8'),('v03','Novotel Ahemdabad',4000,'h9');
/*!40000 ALTER TABLE `hotels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itenary`
--

DROP TABLE IF EXISTS `itenary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itenary` (
  `SNo` int(11) NOT NULL,
  `DOA` date DEFAULT NULL,
  `No_Of_Days` int(11) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `Sights` varchar(5000) DEFAULT NULL,
  `place_of_stay` varchar(5000) DEFAULT NULL,
  `transport` varchar(50) DEFAULT NULL,
  `cost` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itenary`
--

LOCK TABLES `itenary` WRITE;
/*!40000 ALTER TABLE `itenary` DISABLE KEYS */;
/*!40000 ALTER TABLE `itenary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sights`
--

DROP TABLE IF EXISTS `sights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sights` (
  `city_id` varchar(50) DEFAULT NULL,
  `sight` varchar(50) DEFAULT NULL,
  `sight_id` varchar(50) NOT NULL,
  PRIMARY KEY (`sight_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sights`
--

LOCK TABLES `sights` WRITE;
/*!40000 ALTER TABLE `sights` DISABLE KEYS */;
INSERT INTO `sights` VALUES ('v01','Gateway of India','s1'),('v04','Marina Beach','s10'),('v04','MGR Film City','s11'),('v04','Arignar Anna Zoological Park','s12'),('v05','Chaukidaani','s13'),('v05','Amber Fort','s14'),('v05','City Palace','s15'),('v06','Aga Khan Palace','s16'),('v06','Shaniwar Wada','s17'),('v06','Vetal Tekdi','s18'),('v07','Gandhi Ghat','s19'),('v01','Elephanta Caves','s2'),('v07','Patna Sahib Gurudwara','s20'),('v07','Srikrishna Science Centre','s21'),('v08','Taj Mahal','s22'),('v08','Fatehpur Sikhri','s23'),('v08','Agra Fort','s24'),('v09','Dasham Falls','s25'),('v09','Jonha Falls','s26'),('v09','Velocity update','s27'),('v10','Ghatarani Waterfalls','s28'),('v10','Nandan Van Zoo And Safari','s29'),('v01','Marine Drive','s3'),('v10','Swami Vivekanand Sarovar','s30'),('v02','India Gate','s4'),('v02','Qutub Minar','s5'),('v02','Lotus Temple','s6'),('v03','Swaminarayan Temple','s7'),('v03','Sabarmati Ashram','s8');
/*!40000 ALTER TABLE `sights` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcost`
--

DROP TABLE IF EXISTS `tcost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tcost` (
  `city_id` varchar(50) NOT NULL,
  `ptickets` int(11) DEFAULT NULL,
  `ttickets` int(11) DEFAULT NULL,
  PRIMARY KEY (`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcost`
--

LOCK TABLES `tcost` WRITE;
/*!40000 ALTER TABLE `tcost` DISABLE KEYS */;
INSERT INTO `tcost` VALUES ('v01',4403,2641),('v02',4503,2741),('v03',5612,1941),('v04',5612,1941),('v05',5612,1941),('v06',5612,1941),('v07',5612,1941),('v08',5612,1941),('v09',5612,1941),('v10',5612,1941);
/*!40000 ALTER TABLE `tcost` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-20 22:18:11
