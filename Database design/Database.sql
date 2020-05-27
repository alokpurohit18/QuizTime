-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: kbc
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `follow`
--

DROP TABLE IF EXISTS `follow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `follow` (
  `rnumber` int NOT NULL,
  `gnumber` int NOT NULL,
  `game_year` int DEFAULT NULL,
  PRIMARY KEY (`rnumber`,`gnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `follow`
--

LOCK TABLES `follow` WRITE;
/*!40000 ALTER TABLE `follow` DISABLE KEYS */;
/*!40000 ALTER TABLE `follow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game` (
  `gnumber` int NOT NULL,
  `username` varchar(20) DEFAULT NULL,
  `amount_won` int DEFAULT NULL,
  `quit` char(1) DEFAULT NULL,
  `friend1` varchar(50) NOT NULL,
  `friend2` varchar(50) NOT NULL,
  `friend3` varchar(50) NOT NULL,
  PRIMARY KEY (`gnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game`
--

LOCK TABLES `game` WRITE;
/*!40000 ALTER TABLE `game` DISABLE KEYS */;
INSERT INTO `game` VALUES (0,NULL,NULL,NULL,'friend1','friend2','friend3');
/*!40000 ALTER TABLE `game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gets`
--

DROP TABLE IF EXISTS `gets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gets` (
  `username` varchar(20) NOT NULL,
  `qnumber` int NOT NULL,
  PRIMARY KEY (`username`,`qnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gets`
--

LOCK TABLES `gets` WRITE;
/*!40000 ALTER TABLE `gets` DISABLE KEYS */;
/*!40000 ALTER TABLE `gets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lifeline`
--

DROP TABLE IF EXISTS `lifeline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lifeline` (
  `lnumber` int NOT NULL,
  `lname` varchar(50) NOT NULL,
  `ldescription` varchar(200) NOT NULL,
  PRIMARY KEY (`lnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lifeline`
--

LOCK TABLES `lifeline` WRITE;
/*!40000 ALTER TABLE `lifeline` DISABLE KEYS */;
INSERT INTO `lifeline` VALUES (1,'AUDIENCE POLL','The Audience gets 30 seconds to answer the same question by choosing an option on their touchpad. Combined results of all the audiences are then displayed to the contestant.'),(2,'PHONE A FRIEND','The contestant chooses any one of his 3 pre-defined friends for help on the current question. They are then called and the contestant  has 30 seconds to ask them for help on the current question.'),(3,'EXPERT ADVICE','Our expert today is Mrs. Kavya Dixit. She is a Senior Editor and Journalist at Times Of India, Mumbai. Conestant will have 30 seconds to ask the expert for help on the current question.'),(4,'FIFTY-FIFTY','Two wrong options will be erased for the current question. Contestant will then have 30 seconds to answer the question or quit the game.');
/*!40000 ALTER TABLE `lifeline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `age` int NOT NULL,
  `name` varchar(20) NOT NULL,
  `gender` char(1) NOT NULL,
  `highest_score` int DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `qnumber` int NOT NULL,
  `denomination` int NOT NULL,
  `description` varchar(200) NOT NULL,
  `category` varchar(20) NOT NULL,
  `option_a` varchar(100) NOT NULL,
  `option_b` varchar(100) NOT NULL,
  `option_c` varchar(100) NOT NULL,
  `option_d` varchar(100) NOT NULL,
  `correct` char(1) NOT NULL,
  PRIMARY KEY (`qnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,5000,'Which of these is a board game which can normally be played by only two opponents at a time?','G.K','Snakes and Ladders','Chess','Ludo','Monopoly','b'),(2,5000,'Which of these foods would complete the name of these three common dishes: Kadhai _______, Shahi _______, and Matar ______?','G.K','Dahi','Paneer','Ghee','Khoya','b'),(3,5000,'Which of these is the title of a 2018 Hindi film featuring Rani Mukerji? ','Films','Khaansi','Khujli','Sardi','Hichki','d'),(4,5000,'Samukha, Vighnaharta and Ekadanta are other names for which Hindu god?','Social Studies','Brahma','Krishna','Rama','Ganesha','d'),(5,5000,'Which of these actresses became known as the \"Hawa-Hawai\" girl?','Films','Sridevi','Hema Malini','Rekha','Madhuri Dixit','a'),(6,10000,'Who is the highest goalscorer of all time in the UEFA Champions League?','Sports','Messi','Ronaldo','Raul','Benzema','b'),(7,10000,'Which is the 3rd letter in the Greek Alphabet?','Science','Delta','Gamma','Beta','Alpha ','b'),(8,10000,'Which is the smallest state in India?','Social Studies','Sikkim','Goa','Jharkhand','Mizoram','b'),(9,10000,'Which famous car companies slogan is \"Das Auto\" ?','G.K','Volkswagen','Audi','BMW','Mercedes','a'),(10,10000,'Which of these measures is the shortest in length?','Science','Half mile','Half foot','Half yard','Half metre','b'),(11,20000,'Which of these is wrongly matched?','Social Studies','Charminar - Hyderabad','India Gate - Mumbai','Hawa Mahal - Jaipur','Victoria Memorial - Kolkata','b'),(12,20000,'Qantas Airways is national airline for which country?','G.K','Hong Kong','Singapore','Australia','Bahrain','c'),(13,20000,'F1 current leader is?','Sports','Hamilton','Bottas','Vettel','Leclerc','a'),(14,20000,'Which is the most used social media site in the world?','G.K','Instagram','Facebook','YouTube','WhatsApp','b'),(15,20000,'Which of these is the name of a type of women\'s clothing?','G.K','Padmini','Man Bai','Jodha','Anarkali','d'),(16,40000,'Who was the player of the series in the 2019 Cricket World Cup?','Sports','Roy','Archer','Root','Stokes','d'),(17,40000,'Common cold, polio and AIDS are diseases caused by which of these organisms? ','Science','Bacteria','Virus','Protozoa','Fungus','b'),(18,40000,'Which of these is a secondary colour?','G.K','Orange','Grey','Yellow','Black','a'),(19,40000,'Which personality has the most Instagram followers in the world?','Films','Kim Kardashian','Ariana Grande','Cristiano Ronaldo','Dwayne Johnson','c'),(20,40000,'Which out of these ceremonies is performed before marriage ?','G.K','God Bharai','Sagai','Munh Dikhai','Mehndi','b'),(21,80000,'Who won the Men\'s Singles US Open 2019?','Sports','Nadal','Federer','Wawrinka','Medvedev','a'),(22,80000,'Which Indian language other than Hindi is most widely spoken in the World?','Social Studies','Tamil','Telegu ','Bengali','Punjabi','c'),(23,80000,'Which is the 6th planet in the solar system?','Science','Jupiter ','Saturn','Uranus','Neptune','b'),(24,80000,'Who was the second Prime Minister of India?','Social Studies','Lal Bahadur Shastri','Indira Gandhi','Morarji Desai','Gulzarilal Nanda','a'),(25,80000,'In Which century were the first two battles of Panipat fought?','Social Studies','15th','16th','18th','17th','b'),(26,160000,'The official language of Lakshadweep is?','Social Studies','Tamil','Hindi','Malayalam','Telegu','c'),(27,160000,'Which is the 2nd tallest peak in the world?','Social Studies','K2','Kanchenjunga','Lhotse','Nanga Parbat','a'),(28,160000,'Who is the only cricketer to score a quadruple century (400) in international cricket?','Sports','Sachin Tendulkar','Brian Lara','Ricky Ponting','Mahela Jayawardene ','b'),(29,160000,'Which of these is NOT one of the seven islands of Mumbai?','Social Studies','Colaba','Byculla','Parel','Mahim','b'),(30,160000,'Bahubali festival is related to?','G.K','Hinduism','Buddhism','Islam','Jainism','d'),(31,320000,'What is the capital of Iceland?','Social Studies','Stockholm','Reykjavik','Helsinki','Copenhagen','b'),(32,320000,'What do the number of spokes on the Indian flag stand for?','Social Studies','No. of states in the country','No. of hours in the day','No. of days in the week','No. of official languages spoken','b'),(33,320000,'Who was the last Mughal Emperor?','Social Studies','Aurangzeb','Jahangir','Bahadur Shah Zafar','Akbar Shah 2','c'),(34,320000,'Who was the last Indian to win Olympic Gold?','Sports','Leander Paes','Abhinav Bindra','Vijender Singh','PV Sindhu ','b'),(35,320000,'Which film personality was awarded the 2018 Dadasaheb Phalke Award posthumously?','Films','Shashi Kapoor','Om Puri','Vinod Khanna','Lekh Tandon','c'),(36,640000,'Good Friday is observed to commemorate the event of:','Social Studies','Birth of Jesus ','Birth of St Peter','Crucification of Jesus ','Rebirth of Jesus','c'),(37,640000,'Which Railway Station in Mumbai is statistically the busiest station?','G.K','Andheri','CST','Dadar','Thane','d'),(38,640000,'Which is the biggest cricket ground (capacity)?','Sports','MCG, Melbourne','Eden Gardens, Kolkata','Lord\'s, London','Motera, Ahmedabad','d'),(39,640000,'Which of these is NOT a flightless bird?','G.K','Emu','Ostrich','Flamingo','Kiwi','c'),(40,640000,'The twenty-seven daughters of Daksha collectively known as the Nakshatras, are the Wives of which god?','G.K','Surya','Chandra','Mangal','Budha','b'),(41,1250000,'What is the capital of New York State?','Social Studies','New York City','Buffalo','Albany','Dallas','c'),(42,1250000,'What is the currency of South Africa?','G.K','Pesos','Koruna','Rands','Francs','c'),(43,1250000,'Which country was formerly known as Ceylon?','Social Studies','South Africa','Sri Lanka','Netherlands','Egypt','b'),(44,1250000,'Nerissa was a character in which of Shakespeare\'s plays?','G.K','Romeo and Juliet','As you Like It ','Julius Caesar','Merchant of Venice','d'),(45,1250000,'Who wrote the Saraswati Vandana \"Var de Veenavaadini var de\"?','G.K','Jaishankar Prasad','Sumitranandan Pant','Ramdhari Singh \'Dinkar\'','Suryakant Tripathi \'Nirala\'','d'),(46,2500000,'In which city is the 2nd largest football stadium located?','Sports','Barcelona','London','Kolkata','Pyongyang','c'),(47,2500000,'Which number does Roman Numeral M represent?','Science','100','500','1000','10000','c'),(48,2500000,'Which of these countries is completely contained inside another country?','Social Studies','Vatican ','Liechtenstein ','Luxembourg ','Bolivia','a'),(49,2500000,'Which of these is not a Pythagorean Triplet?','Science','29,420,421','37, 684, 685','33, 56,65','36, 323, 324','d'),(50,2500000,'Which of these festivals, also known as Milad un Nabi, is celebrated to mark the birth of Prophet Mohammad?','Social Studies','Muharram','Chaand Raat','Shabe Barat','Mawlid','d'),(51,5000000,'Which state in India has the most international airports?','Social Studies','Kerala','Maharashtra ','Tamil Nadu','West Bengal','a'),(52,5000000,'Which place in the world recieves the highest rainfall?','Social Studies','Cherrapunji, India ','Tutunendo, Colombia ','Mawsynram, India','Cropp River: New Zealand','c'),(53,5000000,'Who is the longest serving Chief Minister of any state?','Social Studies','Jyoti Basu','Pawan Kumar Chamling ','Gegong Apang','M Karunanidhi','b'),(54,5000000,'Which is the longest train route in India?','Social Studies','Jammu Tawi - Kanyakumari','Dibrugarh - Kanyakumari ','  Mangalore - Jammu Tawi','Thiruvananthapuram- Guwahati','b'),(55,5000000,'In April 2018 which Indian tennis legend created a Davis Cup record for most wins in doubles events?','Sports','Yuki Bhambri','Leander Paes','Mahesh Bhupathi','Rohan Bopannah','b'),(56,10000000,'Which year did NMIMS become a deemed to be University?','G.K','1997','2009','2003','1989','c'),(57,10000000,'What is the shape of the pupil of a goat\'s eye?','Science','Rectangular','V-shaped','Circular','Crescent-shaped','a'),(58,10000000,'Which of these football clubs is not from West Bengal?','Sports','Mohun Bagan','East Bengal','Dempo Sports Club','Mohammedan Sporting','c'),(59,10000000,'Which gemstone is created on the inside of living, shelled molluscus like Oysters?','Science','Pearls','Diamonds','Emerald','Topaz','a'),(60,10000000,'Who is the author of the Bengali novel “Noukadubi”, which has been adapted into movies at various times?','G.K','Sarat Chandra Chattopadhyay','Rabindranath Tagore','Samaresh Babu','Sunil Gangopadhyay','b'),(61,50000000,'Who is the architect of the ‘India Gate’?','Social Studies','Henry Irwin','Herbert Baker','Edwin Lutyens','William Emerson','c'),(62,50000000,'Whose birthday is annually observed in India as National Statistics Day on 29 June?','G.K','S N Bose','P C Mahalanobis','Meghnad Saha','J C Bose','b'),(63,50000000,'Who were the title sponsors of the ICC Cricket World Cup when it was hosted outside England for the first time?','Sports','Benson & Hedges','Reliance','Wills','Pepsi','b'),(64,50000000,'Which organization is the birthplace of World Wide Web?','G.K','CERN','Sun Microsystems','IUPAP','University of Cambridge','a'),(65,50000000,'In which of these years were the famous battles of Panipat not fought?','Social Studies','1761','1556','1526','1757','d');
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rule`
--

DROP TABLE IF EXISTS `rule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rule` (
  `rnumber` int NOT NULL,
  `rdescription` varchar(200) NOT NULL,
  PRIMARY KEY (`rnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rule`
--

LOCK TABLES `rule` WRITE;
/*!40000 ALTER TABLE `rule` DISABLE KEYS */;
INSERT INTO `rule` VALUES (1,'THERE ARE A TOTAL OF 13 QUESTIONS LEADING UPTO 5 CRORE.'),(2,'THERE AT 3 CHECKPOINTS IN BETWEEN, ONE AT INR 10,000 , ANOTHER AT INR 3,20,000 AND LAST AT 1 CRORE.'),(3,'YOU WILL HAVE 4 LIFELINES - AUDIENCE POLL, 50/50 , PHONE A FRIEND AND EXPERT ADVICE.'),(4,' EACH OF THESE LIFELINES CAN BE USED ONCE DURING THE GAME.'),(5,'IF YOU ANSWER A QUESTION IS WRONG, YOU WILL FALL DOWN TO THE LAST CHECKPOINT.'),(6,'YOU CAN QUIT AT ANY POINT OF TIME. YOU WILL WIN THE MONEY CORRESPONDING TO THE LAST CORRCTLY ANSWERED QUESTION.');
/*!40000 ALTER TABLE `rule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `used`
--

DROP TABLE IF EXISTS `used`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `used` (
  `lnumber` int NOT NULL,
  `gnumber` int NOT NULL,
  PRIMARY KEY (`lnumber`,`gnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `used`
--

LOCK TABLES `used` WRITE;
/*!40000 ALTER TABLE `used` DISABLE KEYS */;
/*!40000 ALTER TABLE `used` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uses`
--

DROP TABLE IF EXISTS `uses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uses` (
  `qnumber` int NOT NULL,
  `gnumber` int NOT NULL,
  PRIMARY KEY (`qnumber`,`gnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uses`
--

LOCK TABLES `uses` WRITE;
/*!40000 ALTER TABLE `uses` DISABLE KEYS */;
/*!40000 ALTER TABLE `uses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-24 20:06:04
