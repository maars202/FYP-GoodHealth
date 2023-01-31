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
-- Database: `SingHealth`
--
drop database if exists `SingHealth`;
CREATE DATABASE IF NOT EXISTS `SingHealth` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `SingHealth`;

-- --------------------------------------------------------

--
-- Table structure for table `Awards`
--

CREATE TABLE `Awards` (
  `Award_ID` varchar(50) NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Award_Category` varchar(50) NOT NULL,
  `Name_of_Award` varchar(50) NOT NULL,
  `FY_of_Award_Received` varchar(50) NOT NULL,
  `Date_of_Award_Received` date NOT NULL,
  `Project_ID_Ref` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `ExamHistory`
--

CREATE TABLE `ExamHistory` (
  `Exam_ID` varchar(50) NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Name_of_Exam` varchar(50) NOT NULL,
  `Date_of_Attempts` varchar(50) NOT NULL,
  `Exam_Status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Grants`
--

CREATE TABLE `Grants` (
  `Grant_ID` varchar(50) NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Name_of_Grant` varchar(50) NOT NULL,
  `Project_Title` varchar(50) NOT NULL,
  `Project_ID` varchar(50) NOT NULL,
  `Grant_End_Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Involvement`
--

CREATE TABLE `Involvement` (
  `Involvement_No` int(50) NOT NULL,
  `Involvement_Type` varchar(50) NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Event` varchar(50) NOT NULL,
  `Role` varchar(50) NOT NULL,
  `Start_Date` date NOT NULL,
  `End_Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `PersonalDetails`
--

CREATE TABLE `PersonalDetails` (
  `Employee_ID` varchar(50) NOT NULL,
  `MCR_No` varchar(50) NOT NULL,
  `Staff_Name` varchar(50) NOT NULL,
  `Designation` varchar(50) NOT NULL,
  `Programme` varchar(50) NOT NULL,
  `Year_of_Training` varchar(50) NOT NULL,
  `Academic_Year` int(50) NOT NULL,
  `Department` varchar(50) NOT NULL,
  `Institution` varchar(50) NOT NULL,
  `Academic_Clinical_Programme` varchar(50) NOT NULL,
  `Employment_Status` varchar(50) NOT NULL,
  `Nationality` varchar(50) NOT NULL,
  `Date_of_Birth` date NOT NULL,
  `Gender` varchar(50) NOT NULL,
  `Registration_Type` varchar(50) NOT NULL,
  `House_Blk_No` varchar(50) NOT NULL,
  `Street` varchar(50) NOT NULL,
  `Building_Name` varchar(50) NOT NULL,
  `Unit_No` varchar(50) NOT NULL,
  `Postal_Code` varchar(50) NOT NULL,
  `Contact_No_Work` varchar(50) NOT NULL,
  `Contact_No_Personal` varchar(50) NOT NULL,
  `Email_Official` varchar(50) NOT NULL,
  `Email_Personal` varchar(50) NOT NULL,
  `BCLS_Expiry_Date` date NOT NULL,
  `ACLS_Expiry_Date` date NOT NULL,
  `Covid_19_Vaccination_Status` varchar(50) NOT NULL,
  `Date_of_First_Dose` date NOT NULL,
  `Date_of_Second_Dose` date NOT NULL,
  `Vaccination_Remarks` varchar(50) NOT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `PostingHistory`
--

CREATE TABLE `PostingHistory` (
  `Posting ID` varchar(50) NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
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
  `Employee_ID` varchar(50) NOT NULL,
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
  `Employee_ID` varchar(50) NOT NULL,
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
  `Employee_ID` varchar(50) NOT NULL,
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
  `Employee_ID` varchar(50) NOT NULL,
  `Name of Exam` varchar(50) NOT NULL,
  `LOA/PIP` varchar(50) NOT NULL,
  `Start Date` date NOT NULL,
  `End Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `PersonalDetails` (`Employee_ID`, `MCR_No`, `Staff_Name`, `Designation`, 
`Programme`, `Year_of_Training`, `Academic_Year`, `Department`, 
`Institution`, `Academic_Clinical_Programme`, `Employment_Status`, `Nationality`,
`Date_of_Birth`, `Gender`, `Registration_Type`, `House_Blk_No`,
`Street`, `Building_Name`, `Unit_No`, `Postal_Code`,
`Contact_No_Work`, `Contact_No_Personal`,`Email_Official`,`Email_Personal`,
`BCLS_Expiry_Date`, `ACLS_Expiry_Date`,`Covid_19_Vaccination_Status`,`Date_of_First_Dose`,
`Date_of_Second_Dose`, `Vaccination_Remarks`

) VALUES
('one111', "1A", 'lim', 'doctor', 
'cardiology', "2010", 2010, 'cardiology',
'institution', 'academic clinical programme', 'employementstatus', 'nationality',
'2008-11-11', 'Female', 'Registration_Type1','House_Blk_No',
'Street1', 'Building_Name1', 'Unit_No1', 'Postal_Code',
'Contact_No_Work1', 'Contact_No_Personal1', 'Email_Official1', 'Email_Personal1',
'2008-11-11', '2008-11-11', 'Covid_19_Vaccination_Status1', '2008-11-11',
'2008-11-11', 'Vaccination_Remarks'
),
('MOM12390', 'M11367A', 'Daniel Tyler', 'Senior Resident', 'Gastroenterology', 
'SR2', '2022', 'Residency', 'MOHH', 'Medicine', 'Active', 'Singaporean', '1989-11-11', 
'Male', 'Full', '', '11A Tanglin Hill', '', '', '248000', '92343980', '91391470', 
'daniel.tyler@mohh.com.sg', '', '1919-07-20', '1919-04-29', 'Yes', '21-03-30', '2021-04-20', '');

INSERT INTO `Awards` (`Award_ID`, `Employee_ID`, `Award_Category`, 
`Name_of_Award`, `FY_of_Award_Received`, 
`Date_of_Award_Received`, `Project_ID_Ref`
) VALUES
('awardid1', 'one111', 'awardcat1', 'awardname1', 'fy of awardname1', '2008-11-11', 'projectidref1'
);


INSERT INTO `ExamHistory` (`Exam_ID`, `Employee_ID`, `Name_of_Exam`, 
`Date_of_Attempts`, `Exam_Status`
) VALUES
('examid1', 'one111', 'examname1', 'exam1date', 'exam dates 1 2 3'
);

INSERT INTO `Grants` (`Grant_ID`, `Employee_ID`, `Name_of_Grant`, 
`Project_Title`, `Project_ID`, `Grant_End_Date`
) VALUES
('grantid1', 'one111', 'grantname1', 'projecttitle1', 'projectid1', '2008-11-11'
);

INSERT INTO `Involvement` (`Involvement_No`, `Involvement_Type`, `Employee_ID`, `Event`, 
`Role`, `Start_Date`, `End_Date`
) VALUES
('involvementno1', 'type1', 'one111', 'event1', 'role1', '2008-11-11', '2008-11-11'
);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Awards`
--
ALTER TABLE `Awards`
  ADD PRIMARY KEY (`Award_ID`),
  ADD KEY `Employee_ID` (`Employee_ID`);

--
-- Indexes for table `ExamHistory`
--
ALTER TABLE `ExamHistory`
  ADD PRIMARY KEY (`Exam_ID`),
  ADD KEY `Employee_ID` (`Employee_ID`);

--
-- Indexes for table `Grants`
--
ALTER TABLE `Grants`
  ADD PRIMARY KEY (`Grant_ID`,`Name_of_Grant`),
  ADD KEY `Employee_ID` (`Employee_ID`);

--
-- Indexes for table `Involvement`
--
ALTER TABLE `Involvement`
  ADD PRIMARY KEY (`Involvement_No`),
  ADD KEY `Employee_ID` (`Employee_ID`);

--
-- Indexes for table `PersonalDetails`
--
ALTER TABLE `PersonalDetails`
  ADD PRIMARY KEY (`Employee_ID`);

--
-- Indexes for table `PostingHistory`
--
ALTER TABLE `PostingHistory`
  ADD PRIMARY KEY (`Posting ID`),
  ADD KEY `Employee_ID` (`Employee_ID`);

--
-- Indexes for table `Presentations`
--
ALTER TABLE `Presentations`
  ADD PRIMARY KEY (`Presentation ID`),
  ADD KEY `Employee_ID` (`Employee_ID`);

--
-- Indexes for table `Projects`
--
ALTER TABLE `Projects`
  ADD PRIMARY KEY (`Project ID`),
  ADD KEY `Employee_ID` (`Employee_ID`);

--
-- Indexes for table `Publications`
--
ALTER TABLE `Publications`
  ADD PRIMARY KEY (`Publication ID`),
  ADD KEY `Employee_ID` (`Employee_ID`);

--
-- Indexes for table `TrgExtRemHistory`
--
ALTER TABLE `TrgExtRemHistory`
  ADD PRIMARY KEY (`Trg Ext. Rem ID`),
  ADD KEY `Employee_ID` (`Employee_ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Awards`
--
ALTER TABLE `Awards`
  ADD CONSTRAINT `awards_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `PersonalDetails` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ExamHistory`
--
ALTER TABLE `ExamHistory`
  ADD CONSTRAINT `examhistory_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `PersonalDetails` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Grants`
--
ALTER TABLE `Grants`
  ADD CONSTRAINT `grants_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `PersonalDetails` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Involvement`
--
ALTER TABLE `Involvement`
  ADD CONSTRAINT `involvement_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `PersonalDetails` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `PostingHistory`
--
ALTER TABLE `PostingHistory`
  ADD CONSTRAINT `postinghistory_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `PersonalDetails` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Presentations`
--
ALTER TABLE `Presentations`
  ADD CONSTRAINT `presentations_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `PersonalDetails` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Projects`
--
ALTER TABLE `Projects`
  ADD CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `PersonalDetails` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Publications`
--
ALTER TABLE `Publications`
  ADD CONSTRAINT `publications_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `PersonalDetails` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `TrgExtRemHistory`
--
ALTER TABLE `TrgExtRemHistory`
  ADD CONSTRAINT `trgextremhistory_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `PersonalDetails` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


