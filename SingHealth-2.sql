-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Jan 13, 2023 at 01:34 AM
-- Server version: 5.7.34
-- PHP Version: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
drop database if exists `SingHealth`;
CREATE DATABASE IF NOT EXISTS `SingHealth` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `SingHealth`;
--

-- --------------------------------------------------------

--
-- Table structure for table `Awards`
--

drop database if exists `SingHealth`;
CREATE DATABASE IF NOT EXISTS `SingHealth` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `SingHealth`;

CREATE TABLE `Awards` (
  `Award ID` varchar(50) NOT NULL,
  `Employee ID` varchar(50) NOT NULL,
  `Award Category` varchar(50) NOT NULL,
  `Name of Award` varchar(50) NOT NULL,
  `FY of Award Received` varchar(50) NOT NULL,
  `Date of Award Received` date NOT NULL,
  `Project ID/Ref` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `ExamHistory`
--

CREATE TABLE `ExamHistory` (
  `Exam ID` varchar(50) NOT NULL,
  `Employee ID` varchar(50) NOT NULL,
  `Name of Exam` varchar(50) NOT NULL,
  `Date of Attempt(s)` varchar(50) NOT NULL,
  `Exam Status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Grants`
--

CREATE TABLE `Grants` (
  `Grant ID` varchar(50) NOT NULL,
  `Employee ID` varchar(50) NOT NULL,
  `Name of Grant` varchar(50) NOT NULL,
  `Project Title` varchar(50) NOT NULL,
  `Project ID` varchar(50) NOT NULL,
  `Grant End Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Involvement`
--

CREATE TABLE `Involvement` (
  `Involvement No.` int(50) NOT NULL,
  `Involvement Type` varchar(50) NOT NULL,
  `Employee ID` varchar(50) NOT NULL,
  `Event` varchar(50) NOT NULL,
  `Role` varchar(50) NOT NULL,
  `Start Date` date NOT NULL,
  `End Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `PersonalDetails`
--

CREATE TABLE `PersonalDetails` (
  `Employee ID` varchar(50) NOT NULL,
  `MCR No` int(50) NOT NULL,
  `Staff Name` varchar(50) NOT NULL,
  `Designation` varchar(50) NOT NULL,
  `Department` varchar(50) NOT NULL,
  `Institution` varchar(50) NOT NULL,
  `BCLS Expiry Date` date NOT NULL,
  `ACLS Expiry Date` date NOT NULL,
  `Covid-19 Vaccination Status` varchar(50) NOT NULL,
  `Date of First Dose` date NOT NULL,
  `Date of Second Dose` date NOT NULL,
  `Vaccination Remarks` varchar(50) NOT NULL,
  `Year of Graduation` int(50) NOT NULL,
  `Date of Graduation` date NOT NULL,
  `Basic Qualification` varchar(50) NOT NULL,
  `Medical School` varchar(50) NOT NULL,
  `Country of Graduation` varchar(50) NOT NULL,
  `IM Residency Start Date` date NOT NULL,
  `IM Residency End Date` date NOT NULL,
  `SR Residency Programme` varchar(50) NOT NULL,
  `SR Residency Start Date` date NOT NULL,
  `PG Year` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `PostingHistory`
--

CREATE TABLE `PostingHistory` (
  `Posting ID` varchar(50) NOT NULL,
  `Employee ID` varchar(50) NOT NULL,
  `Designation` varchar(50) NOT NULL,
  `Posting Institution` varchar(50) NOT NULL,
  `Posting Department` varchar(50) NOT NULL,
  `Posting Start Date` date NOT NULL,
  `Posting End Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Presentations`
--

CREATE TABLE `Presentations` (
  `Presentation ID` varchar(50) NOT NULL,
  `Employee ID` varchar(50) NOT NULL,
  `Title` varchar(50) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Project ID` varchar(50) NOT NULL,
  `Name of Conference` varchar(50) NOT NULL,
  `Country` varchar(50) NOT NULL,
  `Presentation Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Projects`
--

CREATE TABLE `Projects` (
  `Project ID` varchar(50) NOT NULL,
  `Employee ID` varchar(50) NOT NULL,
  `Project Type` varchar(50) NOT NULL,
  `Project Title` varchar(50) NOT NULL,
  `Start Date` date NOT NULL,
  `End Date` date NOT NULL,
  `PMID` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Publications`
--

CREATE TABLE `Publications` (
  `Publication ID` varchar(50) NOT NULL,
  `Employee ID` varchar(50) NOT NULL,
  `Title of Publication` varchar(50) NOT NULL,
  `Title of Journal` varchar(50) NOT NULL,
  `PMID` varchar(50) NOT NULL,
  `Publication Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TrgExtRemHistory`
--

CREATE TABLE `TrgExtRemHistory` (
  `Trg Ext. Rem ID` varchar(50) NOT NULL,
  `Employee ID` varchar(50) NOT NULL,
  `Name of Exam` varchar(50) NOT NULL,
  `LOA/PIP` varchar(50) NOT NULL,
  `Start Date` date NOT NULL,
  `End Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Indexes for table `Awards`
--
ALTER TABLE `Awards`
  ADD PRIMARY KEY (`Award ID`),
  ADD KEY `Employee ID` (`Employee ID`);

--
-- Indexes for table `ExamHistory`
--
ALTER TABLE `ExamHistory`
  ADD PRIMARY KEY (`Exam ID`),
  ADD KEY `Employee ID` (`Employee ID`);

--
-- Indexes for table `Grants`
--
ALTER TABLE `Grants`
  ADD PRIMARY KEY (`Grant ID`,`Name of Grant`),
  ADD KEY `Employee ID` (`Employee ID`);

--
-- Indexes for table `Involvement`
--
ALTER TABLE `Involvement`
  ADD PRIMARY KEY (`Involvement No.`),
  ADD KEY `Employee ID` (`Employee ID`);

--
-- Indexes for table `PersonalDetails`
--
ALTER TABLE `PersonalDetails`
  ADD PRIMARY KEY (`Employee ID`);

--
-- Indexes for table `PostingHistory`
--
ALTER TABLE `PostingHistory`
  ADD PRIMARY KEY (`Posting ID`),
  ADD KEY `Employee ID` (`Employee ID`);

--
-- Indexes for table `Presentations`
--
ALTER TABLE `Presentations`
  ADD PRIMARY KEY (`Presentation ID`),
  ADD KEY `Employee ID` (`Employee ID`);

--
-- Indexes for table `Projects`
--
ALTER TABLE `Projects`
  ADD PRIMARY KEY (`Project ID`),
  ADD KEY `Employee ID` (`Employee ID`);

--
-- Indexes for table `Publications`
--
ALTER TABLE `Publications`
  ADD PRIMARY KEY (`Publication ID`),
  ADD KEY `Employee ID` (`Employee ID`);

--
-- Indexes for table `TrgExtRemHistory`
--
ALTER TABLE `TrgExtRemHistory`
  ADD PRIMARY KEY (`Trg Ext. Rem ID`),
  ADD KEY `Employee ID` (`Employee ID`);


--
-- Constraints for dumped tables
--

--
-- Constraints for table `Awards`
--
ALTER TABLE `Awards`
  ADD CONSTRAINT `awards_ibfk_1` FOREIGN KEY (`Employee ID`) REFERENCES `PersonalDetails` (`Employee ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ExamHistory`
--
ALTER TABLE `ExamHistory`
  ADD CONSTRAINT `examhistory_ibfk_1` FOREIGN KEY (`Employee ID`) REFERENCES `PersonalDetails` (`Employee ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Grants`
--
ALTER TABLE `Grants`
  ADD CONSTRAINT `grants_ibfk_1` FOREIGN KEY (`Employee ID`) REFERENCES `PersonalDetails` (`Employee ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Involvement`
--
ALTER TABLE `Involvement`
  ADD CONSTRAINT `involvement_ibfk_1` FOREIGN KEY (`Employee ID`) REFERENCES `PersonalDetails` (`Employee ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `PostingHistory`
--
ALTER TABLE `PostingHistory`
  ADD CONSTRAINT `postinghistory_ibfk_1` FOREIGN KEY (`Employee ID`) REFERENCES `PersonalDetails` (`Employee ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Presentations`
--
ALTER TABLE `Presentations`
  ADD CONSTRAINT `presentations_ibfk_1` FOREIGN KEY (`Employee ID`) REFERENCES `PersonalDetails` (`Employee ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Projects`
--
ALTER TABLE `Projects`
  ADD CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`Employee ID`) REFERENCES `PersonalDetails` (`Employee ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Publications`
--
ALTER TABLE `Publications`
  ADD CONSTRAINT `publications_ibfk_1` FOREIGN KEY (`Employee ID`) REFERENCES `PersonalDetails` (`Employee ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `TrgExtRemHistory`
--
ALTER TABLE `TrgExtRemHistory`
  ADD CONSTRAINT `trgextremhistory_ibfk_1` FOREIGN KEY (`Employee ID`) REFERENCES `PersonalDetails` (`Employee ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
