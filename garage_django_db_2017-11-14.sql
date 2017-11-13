# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.19)
# Database: garage_django_db
# Generation Time: 2017-11-13 20:30:52 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table auth_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`)
VALUES
	(1,'pbkdf2_sha256$36000$Ex3X2n2gF1tl$I8WIIyULFA4yZHrnB2eb8xW+eTTLt6zJ/p1yS2EYoVQ=','2017-11-13 20:22:45.350446',0,'admin','vaibhav','jain','vaibhavjain671@gmail.com',0,1,'2017-10-25 17:23:47.709792'),
	(2,'pbkdf2_sha256$36000$lm6bROxH9uxl$Ajh/pU46pX0WLUNBC86bV2lf8y+oj668qr8yHq34Vp0=','2017-11-13 20:29:42.542776',1,'vaibhav','Vaibhav','Jain','vaibhavjain671@gmail.com',1,1,'2017-10-25 17:25:41.891970'),
	(3,'pbkdf2_sha256$36000$ee0AqPtXfqHk$qc6Y+2rLFDLEanjJb9XUfDyz4MsI2ZuQlm/cpRv+WEY=','2017-10-27 21:35:40.580884',0,'shubham','Shubham','Jain','itshubhamjain@gmail.com',0,1,'2017-10-27 18:20:11.880737'),
	(4,'pbkdf2_sha256$36000$OyTMpUTtNlp3$kM5yM7yZW/60j/O+V2ItmBEuenvj/aF1IB2LE7aOklw=','2017-10-30 07:56:18.559879',0,'shantanu','Shantanu','Shah','fffff@gmail.com',0,1,'2017-10-30 07:56:18.348512');

/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table vehicles_accounting
# ------------------------------------------------------------

DROP TABLE IF EXISTS `vehicles_accounting`;

CREATE TABLE `vehicles_accounting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gross_profit` int(10) unsigned NOT NULL,
  `sale_bill_no_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vehicles_accounting_sale_bill_no_id_12aaabfb_fk_vehicles_` (`sale_bill_no_id`),
  CONSTRAINT `vehicles_accounting_sale_bill_no_id_12aaabfb_fk_vehicles_` FOREIGN KEY (`sale_bill_no_id`) REFERENCES `vehicles_invoicesale` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `vehicles_accounting` WRITE;
/*!40000 ALTER TABLE `vehicles_accounting` DISABLE KEYS */;

INSERT INTO `vehicles_accounting` (`id`, `gross_profit`, `sale_bill_no_id`)
VALUES
	(1,6000,1),
	(2,4600,2);

/*!40000 ALTER TABLE `vehicles_accounting` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table vehicles_invoicepurchase
# ------------------------------------------------------------

DROP TABLE IF EXISTS `vehicles_invoicepurchase`;

CREATE TABLE `vehicles_invoicepurchase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bill_no` varchar(12) NOT NULL,
  `amount_purchased` int(10) unsigned NOT NULL,
  `expense` int(10) unsigned NOT NULL,
  `valuation_amount` int(10) unsigned NOT NULL,
  `date_time` datetime(6) NOT NULL,
  `party_purchased_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vehicles_invoicepurc_party_purchased_id_f7b22466_fk_vehicles_` (`party_purchased_id`),
  CONSTRAINT `vehicles_invoicepurc_party_purchased_id_f7b22466_fk_vehicles_` FOREIGN KEY (`party_purchased_id`) REFERENCES `vehicles_partydetails` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `vehicles_invoicepurchase` WRITE;
/*!40000 ALTER TABLE `vehicles_invoicepurchase` DISABLE KEYS */;

INSERT INTO `vehicles_invoicepurchase` (`id`, `bill_no`, `amount_purchased`, `expense`, `valuation_amount`, `date_time`, `party_purchased_id`)
VALUES
	(3,'P23OCT170002',25000,1500,35000,'2017-10-22 19:10:16.000000',3),
	(4,'P25OCT170002',17000,1400,25000,'2017-10-24 19:10:49.000000',4),
	(5,'P15SEP170001',13000,1000,23000,'2017-09-14 19:11:29.000000',5),
	(7,'P25OCT170001',17000,500,27000,'2017-10-24 19:12:49.000000',7),
	(8,'P26OCT170001',50000,2000,65000,'2017-10-26 00:25:02.000000',10),
	(12,'P26OCT170002',13400,1000,22000,'2017-10-26 00:25:11.000000',11),
	(13,'P27OCT170001',35000,2000,50000,'2017-10-26 20:43:03.803302',18),
	(14,'P27OCT170001',33500,1500,47000,'2017-10-26 20:54:35.065594',15),
	(15,'P27OCT170001',46000,4000,70000,'2017-10-26 20:54:35.065594',14),
	(16,'P27OCT170001',36000,2000,52000,'2017-10-26 20:54:35.065594',13),
	(17,'P27OCT170001',23000,1300,32000,'2017-10-26 21:04:50.965339',17),
	(19,'P28OCT170001',32300,1200,45000,'2017-10-27 22:13:32.534070',20),
	(22,'P29OCT170001',67000,5000,90000,'2017-10-28 21:21:06.000000',25),
	(23,'P29OCT170001',25000,1400,37000,'2017-10-29 17:33:53.121743',27),
	(24,'P5NOV170001',45000,4000,65000,'2017-11-05 08:02:49.779883',29);

/*!40000 ALTER TABLE `vehicles_invoicepurchase` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table vehicles_invoicesale
# ------------------------------------------------------------

DROP TABLE IF EXISTS `vehicles_invoicesale`;

CREATE TABLE `vehicles_invoicesale` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bill_no` varchar(12) NOT NULL,
  `amount_sold` int(10) unsigned NOT NULL,
  `date_time` datetime(6) NOT NULL,
  `party_sold_id` int(11) NOT NULL,
  `purchase_bill_no_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vehicles_invoicesale_purchase_bill_no_id_e4ddb0d6_fk_vehicles_` (`purchase_bill_no_id`),
  KEY `vehicles_invoicesale_party_sold_id_29036049_fk_vehicles_` (`party_sold_id`),
  CONSTRAINT `vehicles_invoicesale_party_sold_id_29036049_fk_vehicles_` FOREIGN KEY (`party_sold_id`) REFERENCES `vehicles_partydetails` (`id`),
  CONSTRAINT `vehicles_invoicesale_purchase_bill_no_id_e4ddb0d6_fk_vehicles_` FOREIGN KEY (`purchase_bill_no_id`) REFERENCES `vehicles_invoicepurchase` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `vehicles_invoicesale` WRITE;
/*!40000 ALTER TABLE `vehicles_invoicesale` DISABLE KEYS */;

INSERT INTO `vehicles_invoicesale` (`id`, `bill_no`, `amount_sold`, `date_time`, `party_sold_id`, `purchase_bill_no_id`)
VALUES
	(1,'S25OCT170001',20000,'2017-10-25 18:31:11.000000',8,5),
	(2,'S25OCT170002',23000,'2017-10-25 20:52:16.000000',9,4),
	(3,'S27OCT170001',65000,'2017-10-26 18:35:59.000000',12,8),
	(4,'S29OCT170001',85000,'2017-10-28 21:27:32.000000',26,22),
	(5,'S29OCT170001',35000,'2017-10-29 18:06:35.000000',28,23);

/*!40000 ALTER TABLE `vehicles_invoicesale` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table vehicles_partydetails
# ------------------------------------------------------------

DROP TABLE IF EXISTS `vehicles_partydetails`;

CREATE TABLE `vehicles_partydetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(15) NOT NULL,
  `aadhar_no` varchar(12) NOT NULL,
  `phone_no` varchar(10) NOT NULL,
  `email` varchar(140) NOT NULL,
  `address` varchar(200) NOT NULL,
  `is_buyer` tinyint(1) NOT NULL,
  `is_seller` tinyint(1) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `vehicle_detail_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vehicles_partydetails_slug_f9458ac0` (`slug`),
  KEY `vehicles_partydetail_vehicle_detail_id_784c126f_fk_vehicles_` (`vehicle_detail_id`),
  CONSTRAINT `vehicles_partydetail_vehicle_detail_id_784c126f_fk_vehicles_` FOREIGN KEY (`vehicle_detail_id`) REFERENCES `vehicles_vehicledetails` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `vehicles_partydetails` WRITE;
/*!40000 ALTER TABLE `vehicles_partydetails` DISABLE KEYS */;

INSERT INTO `vehicles_partydetails` (`id`, `full_name`, `aadhar_no`, `phone_no`, `email`, `address`, `is_buyer`, `is_seller`, `slug`, `vehicle_detail_id`)
VALUES
	(3,'Gajanand','234567894356','9876567823','gaj@gm.co','Jaipur',0,1,'gajanand-natwar',3),
	(4,'Vivek','345687865432','9876543456','vi@gm.com','Nagpur',0,1,'vivek',4),
	(5,'Omkar','123459876543','9873456798','omkar@gma.co.in','Sinhgad Road',0,1,'omkar',5),
	(7,'Yash Jain','234598765433','8912345609','yash@gmail.com','Akurdi',0,1,'yash-jain',7),
	(8,'Akshay','456798765432','9876534567','aks@gmai.com','Delhi',1,0,'akshay',5),
	(9,'Ajay','423478654321','7654321786','ajay@gma.co.in','Wakad',1,0,'ajay',4),
	(10,'Anurag','542345676543','8976543232','anu@yam.in','Baner',0,1,'anurag',8),
	(11,'Kishore','098763456789','9087653245','kiss@gmail.com','Rajasthan',0,1,'kishore',9),
	(12,'Shantanu','234567890987','8765432345','shanshah@gmail.com','Firodiya',1,0,'shantanu',8),
	(13,'Tejas Jain','345678990876','9087654324','teju@gmail.com','Bhandarkar Road',0,1,'tejas-jain',11),
	(14,'Pratik Mehta','987653456789','7987654324','pratik@ymail.com','Solapur',0,1,'pratik-mehta',12),
	(15,'Akshat','897345673245','9333987654','akshat@gmail.com','Gokhale Nagar',0,1,'akshat',10),
	(17,'Sumit Mittal','345678976543','9876532456','sumit@hgd.com','Bibwevadi',0,1,'sumit-mittal',14),
	(18,'Aarav','678321657894','7893245677','aar@wm.com','Kothrus',0,1,'aarav',15),
	(20,'Nitin Doshi','546784356785','7865423456','nitindoshi768@gmail.com','Jodhpur',0,1,'nitin-doshi',17),
	(25,'Roshan Bothara','345678765345','9876523456','both@gmail.com','Yawatmal, Nagpur',0,1,'roshan-bothara',18),
	(26,'Vaibhav Jain','123487654234','8976523456','vaibhavjain671@gmail.com','Panipat',1,0,'vaibhav-jain',18),
	(27,'Sanjeet','234598765432','9087652345','afg@c.om','HND',0,1,'sanjeet',19),
	(28,'Sayyam','456876523456','8976324567','dha@ga.com','NA',1,0,'sayyam',19),
	(29,'Jeetendra','123123123','2342432342','both@gmail.com','dfafd',0,1,'jeetendra',20);

/*!40000 ALTER TABLE `vehicles_partydetails` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table vehicles_vehicledetails
# ------------------------------------------------------------

DROP TABLE IF EXISTS `vehicles_vehicledetails`;

CREATE TABLE `vehicles_vehicledetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manufacturer` varchar(50) NOT NULL,
  `model_name` varchar(50) NOT NULL,
  `model_year` int(10) unsigned NOT NULL,
  `registration_no` varchar(15) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `is_sold` tinyint(1) NOT NULL,
  `chassis_no` varchar(15) NOT NULL,
  `color` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vehicles_vehicledetails_slug_5b51b101` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `vehicles_vehicledetails` WRITE;
/*!40000 ALTER TABLE `vehicles_vehicledetails` DISABLE KEYS */;

INSERT INTO `vehicles_vehicledetails` (`id`, `manufacturer`, `model_name`, `model_year`, `registration_no`, `slug`, `is_sold`, `chassis_no`, `color`)
VALUES
	(3,'Honda','Activa 4G 120cc',2010,'HP 12 AF 1234','activa-4g',0,'987651234567892','White'),
	(4,'Honda','Activa 3G',2014,'MH 12 CZ 1421','activa-3g',1,'098765412345675','Red'),
	(5,'TVS','Victor',2012,'MH 12 AD 1654','victor',1,'098345612345098','Purple Blu'),
	(7,'TVS','Jupiter',2016,'KA 12 NA 2322','jupiter',0,'459876234982345','Navy Blue'),
	(8,'Yamaha','R15',2014,'MH 10 DE 4000','r15',1,'756433457865435','Dark Blue'),
	(9,'Honda','CB Shine',2014,'MH 14 DD 2342','cb-shine',0,'987653456789323','Black'),
	(10,'Suzuki','Gixxer',2015,'MH 14 AA 7821','gixxer',0,'987654356789098','Orange'),
	(11,'Bajaj','Pulsar 200CC',2015,'HR 12 AD 5767','pulsar-200cc',0,'897654324567898','Black'),
	(12,'Bullet','Bullet 350CC',2015,'MH 34 AE 1245','bullet-350cc',0,'987652345678909','Silver'),
	(14,'Suzuki','Access',2014,'KA 34 SA 0123','access',0,'234567809876543','White'),
	(15,'Honda','Unicorn',2015,'MH 23 ED 2345','unicorn',0,'435678989765433','Grey'),
	(17,'Suzuki','Hemlot',2013,'HR 98 AR 1234','hemlot',0,'987623546789034','White'),
	(18,'Bullet','Bullet 350CC',2012,'GJ 23 AF 6712','bullet-350cc-n5gd',1,'345678934567834','Red'),
	(19,'Honda','Qwert',2015,'HR 06 AB 1241','qwert',1,'234567876543123','White'),
	(20,'Royal Enfield','Thunderbird 350',2011,'mh 12 gm 8016','thunderbird-350',0,'123213','Silver');

/*!40000 ALTER TABLE `vehicles_vehicledetails` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
