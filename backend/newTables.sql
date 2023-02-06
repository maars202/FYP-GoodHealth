-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Feb 03, 2023 at 10:52 PM
-- Server version: 5.7.34
-- PHP Version: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


-- Database: `SingHealth`


drop database if exists Posts;
CREATE DATABASE IF NOT EXISTS Posts DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE Posts;


CREATE TABLE `Personal_Details` (
  `Employee_ID` varchar(50) NOT NULL,
  `MCR_No` varchar(50) NOT NULL,
  `Staff_Name` varchar(50) NOT NULL,
  `Designation` varchar(50) NOT NULL,
  `Programme` varchar(50) NOT NULL,
  `Year_of_Training` varchar(50) NOT NULL,
  `Academic_Year` varchar(50) NOT NULL,
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
  `BCLS_Expiry_Date` date NULL,
  `ACLS_Expiry_Date` date NULL,
  `Covid_19_Vaccination_Status` varchar(50) NULL,
  `Date_of_First_Dose` date NULL,
  `Date_of_Second_Dose` date NULL,
  `Vaccination_Remarks` varchar(50) NULL,
  `Personal_Details_deleted` boolean DEFAULT false,
  primary key (Employee_ID)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Didactic_Attendance` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `BillingName` varchar(50) NOT NULL,
  `Month` varchar(50) NOT NULL,
  `Total_tracked_sessions` varchar(50) NOT NULL,
  `Number_of_sessions_attended` varchar(50) NOT NULL,
  `Percentage_of_sessions_attended` varchar(50) NOT NULL,
  `MmYyyy` varchar(50) NOT NULL,
  `Posting_Institution` varchar(50) NOT NULL,
  `Posting_Department` varchar(50) NOT NULL,
  `Scheduled_Teachings` varchar(50) NOT NULL,
  `Compliance_or_Not` varchar(50) NOT NULL,
  `Didactic_Attendance_deleted` boolean DEFAULT false,
  primary key (id),
   CONSTRAINT FK_PersonOrder FOREIGN KEY (Employee_ID)
    REFERENCES Personal_Details(Employee_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for table `Awards`
--
ALTER TABLE `Didactic_Attendance`
  ADD KEY `Employee_ID` (`Employee_ID`);


ALTER TABLE `Didactic_Attendance`
  ADD CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `Personal_Details` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE;




INSERT INTO `Personal_Details` (`Employee_ID`, `MCR_No`, `Staff_Name`, `Designation`, `Programme`, `Year_of_Training`, `Academic_Year`, `Department`, `Institution`, `Academic_Clinical_Programme`, `Employment_Status`, `Nationality`, `Date_of_Birth`, `Gender`, `Registration_Type`, `House_Blk_No`, `Street`, `Building_Name`, `Unit_No`, `Postal_Code`, `Contact_No_Work`, `Contact_No_Personal`, `Email_Official`, `Email_Personal`, `BCLS_Expiry_Date`, `ACLS_Expiry_Date`, `Covid_19_Vaccination_Status`, `Date_of_First_Dose`, `Date_of_Second_Dose`, `Vaccination_Remarks`, `Personal_Details_deleted`) VALUES
('MOM05690', 'M88791Z', 'Kang Hyun Bin', 'Senior Resident', 'Gastroenterology', 'SR3', '2022', 'Residency', 'MOHH', 'Medicine', 'Active', 'Singaporean', '1991-12-05', 'Male', 'Full', '', 'Lorong Gambir', '', '', '536000', '', '91515780', 'hyunbin.kang@mohh.com.sg', '', NULL, NULL, 'Yes', '2021-02-09', '2021-03-02', '', 0),
('MOM12390', 'M11367A', 'Daniel Tyler', 'Senior Resident', 'Gastroenterology', 'SR2', '2022', 'Residency', 'MOHH', 'Medicine', 'Active', 'Singaporean', '1989-11-11', 'Male', 'Full', '', '11A Tanglin Hill', '', '', '248000', '92343980', '91391470', 'daniel.tyler@mohh.com.sg', '', '1919-07-20', '1919-04-29', 'Yes', '2021-03-30', '2021-04-20', '', 0),
('one111', '1A', 'lim', 'doctor', 'cardiology', '2010', '2010', 'cardiology', 'institution', 'academic clinical programme', 'employementstatus', 'nationality', '2008-11-11', 'Female', 'Registration_Type1', 'House_Blk_No', 'Street1', 'Building_Name1', 'Unit_No1', 'Postal_Code', 'Contact_No_Work1', 'Contact_No_Personal1', 'Email_Official1', 'Email_Personal1', '2008-11-11', '2008-11-11', 'Covid_19_Vaccination_Status1', '2008-11-11', '2008-11-11', 'Vaccination_Remarks', 0);



INSERT INTO `Didactic_Attendance` (`Employee_ID`, `BillingName`,
  `Month`,
  `Total_tracked_sessions`,
  `Number_of_sessions_attended`,
  `Percentage_of_sessions_attended`,
  `MmYyyy`,
  `Posting_Institution`,
  `Posting_Department`,
  `Scheduled_Teachings`,
  `Compliance_or_Not`)  VALUES
('one111', 'SGHGasEnt', 'July', '14', '14', '100%', '', '', '', '', '');


CREATE TABLE `Case_Log` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Subspecialty` varchar(50) NOT NULL,
  `Type_of_Case_Log` varchar(50) NOT NULL,
  `Date_of_Log` varchar(50) NOT NULL,
  `CPT` varchar(50) NOT NULL,
  `Total` varchar(50) NOT NULL,
  `Performed` varchar(50) NOT NULL,
  `Observed` varchar(50) NOT NULL,
  `Verified` varchar(50) NOT NULL,
  `Certified` varchar(50) NOT NULL,
  `Case_Log_deleted` tinyint(1) DEFAULT '0',
  primary key (id),
  CONSTRAINT FK_PersonOrder2 FOREIGN KEY (Employee_ID)
    REFERENCES Personal_Details(Employee_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `Duty_Hour_Log` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Level` varchar(50) NOT NULL,
  `Submitted` varchar(50) NOT NULL,
  `Submitted_Proportion` varchar(50) NOT NULL,
  `MMYYYY` varchar(50) NOT NULL,
  `Logged_for_month` varchar(50) NOT NULL,
  `Duty_Hour_Log_deleted` boolean DEFAULT false,
  primary key (id),
  CONSTRAINT FK_PersonOrder3 FOREIGN KEY (Employee_ID)
    REFERENCES Personal_Details(Employee_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `Duty_Hour_Log` (`Employee_ID`, `Level`, `Submitted`, 
`Submitted_Proportion`, `MMYYYY`, `Logged_for_month`) VALUES
('MOM12390', '4', '3', '0.5', 'Mar-20', 'Yes'),
('one111', '4', '4', '0.3', 'Mar-20', 'Yes'),
('MOM12390', '4', '0', '0', 'Mar-20', 'Yes'),
('one111', '4', '3', '1', 'Mar-20', 'Yes'),
('one111', '4', '4', '1', 'Mar-20', 'Yes');


CREATE TABLE `Education_History` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Year_of_Graduation` varchar(50) NOT NULL,
  `Date_of_Graduation` varchar(50) NOT NULL,
  `Basic_Qualification` varchar(50) NOT NULL,
  `Medical_School` varchar(50) NOT NULL,
  `Country_of_Graduation` varchar(50) NOT NULL,
  `IM_Residency_Start_Date` varchar(50) NOT NULL,
  `IM_Residency_End_Date` varchar(50) NOT NULL,
  `SR_Residency_Programme` varchar(50) NOT NULL,
  `SR_Residency_Start_Date` varchar(50) NOT NULL,
  `SR_Residency_End_Date` varchar(50) NOT NULL,
  `PG_Year` varchar(50) NOT NULL,
  `Education_History_deleted` tinyint(1) DEFAULT '0',
  primary key (id),
  CONSTRAINT FK_PersonOrder4 FOREIGN KEY (Employee_ID)
    REFERENCES Personal_Details(Employee_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Education_History` (`Employee_ID`,`Year_of_Graduation`,
`Date_of_Graduation`,`Basic_Qualification`,`Medical_School`,
`Country_of_Graduation`,`IM_Residency_Start_Date`,`IM_Residency_End_Date`,
`SR_Residency_Programme`,`SR_Residency_Start_Date`,`SR_Residency_End_Date`,
`PG_Year`) VALUES
('one111', '2001', '2001', 'Basic_Qualification1', 'Medical_School1', 
'Country_of_Graduation1', 'IM_Residency_Start_Date1', 'IM_Residency_End_Date1', 
'SR_Residency_Programme1', 'SR_Residency_Start_Date1', 'SR_Residency_End_Date1', 
'PG_Year1');

CREATE TABLE `Evaluations` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Year_of_Training` varchar(50) NOT NULL,
  `Rotation_Period` varchar(50) NOT NULL,
  `Name_of_Evaluation_Form` varchar(50) NOT NULL,
  `Question_Number` varchar(50) NOT NULL,
  `Score` varchar(50) NOT NULL,
  `Evaluator` varchar(50) NOT NULL,
  `Service` varchar(50) NOT NULL,
  `Answer` varchar(50) NOT NULL,
  `Evaluations_deleted` tinyint(1) DEFAULT '0',
  primary key (id),
  CONSTRAINT FK_PersonOrder5 FOREIGN KEY (Employee_ID)
    REFERENCES Personal_Details(Employee_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Evaluations` (`Employee_ID`,`Year_of_Training`,`Rotation_Period`,
`Name_of_Evaluation_Form`,`Question_Number`,`Score`,`Evaluator`,`Service`,`Answer`) VALUES
('one111','Year_of_Training111','Rotation_Period111','Name_of_Evaluation_Form111',
'Question_Number111','Score111','Evaluator111','Service111','Answer111');

CREATE TABLE `Exam_History` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Name_of_Exam` varchar(50) NOT NULL,
  `Date_of_Attempt` varchar(50) NOT NULL,
  `Exam_Status` varchar(50) NOT NULL,
  `Exam_History_deleted` tinyint(1) DEFAULT '0',
  primary key (id),
  CONSTRAINT FK_PersonOrder6 FOREIGN KEY (Employee_ID)
    REFERENCES Personal_Details(Employee_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Exam_History` (`Employee_ID`,`Name_of_Exam`,`Date_of_Attempt`,
`Exam_Status`,`Exam_History_deleted`) VALUES
('one111','Name_of_Exam111','Date_of_Attempt111','Exam_Status111','Exam_History_deleted111');


CREATE TABLE `Grants` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Name_of_Grant` varchar(50) NOT NULL,
  `Project_Title` varchar(50) NOT NULL,
  `Project_ID` varchar(50) NOT NULL,
  `Grant_End_Date` varchar(50) NOT NULL,
  `Grant_Start_Date` varchar(50) NOT NULL,
  `Grants_deleted` tinyint(1) DEFAULT '0',
  primary key (id),
  CONSTRAINT FK_PersonOrder7 FOREIGN KEY (Employee_ID)
    REFERENCES Personal_Details(Employee_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Grants`
--

INSERT INTO `Grants` (`Employee_ID`, `Name_of_Grant`, `Project_Title`, `Project_ID`, `Grant_End_Date`, `Grant_Start_Date`, `Grants_deleted`) VALUES
('MOM05690', 'grant1', 'project1', '1234', '1/1/2022', '1/2/2022', 0),
('one111', 'grant2', 'project12', '5667', '4/5/2022', '4/6/2022', 0);


CREATE TABLE `IHI` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Completion_of_Emodules` varchar(50) NOT NULL,
  `Date` varchar(50) NOT NULL,
  `IHI_deleted` tinyint(1) DEFAULT '0',
  primary key (id),
  CONSTRAINT FK_PersonOrder8 FOREIGN KEY (Employee_ID)
    REFERENCES Personal_Details(Employee_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `IHI` (`Employee_ID`, `Completion_of_Emodules`, `Date`, `IHI_deleted`) VALUES
('MOM05690', '3', '1/2/2022', 0),
('one111', '4', '1/2/2022', 0);

-- --------------------------------------------------------

--
-- Table structure for table `Involvement`
--

CREATE TABLE `Involvement` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Involvement_Type` varchar(50) NOT NULL,
  `Event` varchar(50) NOT NULL,
  `Role` varchar(50) NOT NULL,
  `Start_Date` varchar(50) NOT NULL,
  `End_Date` varchar(50) NOT NULL,
  `Involvement_deleted` tinyint(1) DEFAULT '0',
  primary key (id),
  CONSTRAINT FK_PersonOrder9 FOREIGN KEY (Employee_ID)
    REFERENCES Personal_Details(Employee_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Involvement` (`Employee_ID`, `Involvement_Type`, `Event`, 
`Role`, `Start_Date`,`End_Date`, `Involvement_deleted`) VALUES
('MOM05690','Involvement_Type111','Event111','Role111','Start_Date111','End_Date111',0),
('one111','Involvement_Type111','Event111','Role111','Start_Date111','End_Date111',0);




CREATE TABLE `Procedure_Log` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Procedure_Name` varchar(50) NOT NULL,
  `Date_of_Completion` varchar(50) NOT NULL,
  `CPT` varchar(50) NOT NULL,
  `Total` varchar(50) NOT NULL,
  `Performed` varchar(50) NOT NULL,
  `Observed` varchar(50) NOT NULL,
  `Verified` varchar(50) NOT NULL,
  `Certified` varchar(50) NOT NULL,
  `Procedure_Log_deleted` int(11) NOT NULL,
  primary key (id),
  CONSTRAINT FK_PersonOrder10 FOREIGN KEY (Employee_ID)
    REFERENCES Personal_Details(Employee_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `Procedure_Log` (`Employee_ID`,`Procedure_Name`,`Date_of_Completion`,`CPT`,`Total`,`Performed`,`Observed`,`Verified`,`Certified`,`Procedure_Log_deleted`) VALUES
('MOM05690','Procedure_Name111','Date_of_Completion111','CPT111','Total111','Performed111','Observed111','Verified111','Certified111',0),
('one111','Procedure_Name222','Date_of_Completion111','CPT111','Total111','Performed111','Observed111','Verified111','Certified111',0);


-- --------------------------------------------------------

--
-- Table structure for table `Projects`
--

CREATE TABLE `Projects` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Project_Type` varchar(50) NOT NULL,
  `Project_Title` varchar(100) NOT NULL,
  `Project_ID` varchar(50) NOT NULL,
  `Start_Date` varchar(50) NOT NULL,
  `End_Date` varchar(50) NOT NULL,
  `Date_of_QI_Certification` varchar(50) DEFAULT NULL,
  `PMID` varchar(50) DEFAULT NULL,
  `Project_deleted` tinyint(1) DEFAULT '0',
  primary key (id),
  CONSTRAINT FK_PersonOrder11 FOREIGN KEY (Employee_ID)
    REFERENCES Personal_Details(Employee_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Projects` (`Employee_ID`,`Project_Type`,`Project_Title`,`Project_ID`,
`Start_Date`,`End_Date`,`Date_of_QI_Certification`,`PMID`,`Project_deleted`) VALUES
('MOM05690','Project_Type111','Project_Title111','Project_ID111','Start_Date111','End_Date111','Date_of_QI_Certification111','PMID111',0),
('one111','Project_Type222','Project_Title111','Project_ID111','Start_Date111','End_Date111','Date_of_QI_Certification111','PMID111',0);



CREATE TABLE `Publications` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Employee_ID` varchar(50) NOT NULL,
  `Publication_Title` varchar(50) NOT NULL,
  `Journal_Title` varchar(50) NOT NULL,
  `PMID` varchar(50) NOT NULL,
  `Publication_Date` varchar(50) NOT NULL,
  `Publication_deleted` tinyint(1) DEFAULT '0',
  primary key (id),
  CONSTRAINT FK_PersonOrder12 FOREIGN KEY (Employee_ID)
    REFERENCES Personal_Details(Employee_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Publications` (`Employee_ID`,`Publication_Title`,`Journal_Title`,`PMID`,`Publication_Date`,`Publication_deleted`) VALUES
('MOM05690','Publication_Title111','Journal_Title111','PMID111','Publication_Date111',0),
('one111','Publication_Title111','Journal_Title111','PMID111','Publication_Date111',0);


CREATE TABLE `TrgExtRemHistory` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Employee_ID` varchar(100) DEFAULT ' ',
  `LOAPIP` varchar(100) DEFAULT NULL,
  `StartDate` varchar(50) DEFAULT NULL,
  `EndDate` varchar(50) DEFAULT NULL,
  `TrgExtRemHistory_deleted` tinyint(1) DEFAULT '0',
  primary key (id),
  CONSTRAINT FK_PersonOrder13 FOREIGN KEY (Employee_ID)
    REFERENCES Personal_Details(Employee_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `TrgExtRemHistory` (`Employee_ID`,`LOAPIP`,`StartDate`,`EndDate`,`TrgExtRemHistory_deleted`) VALUES
('MOM05690','LOAPIP111','StartDate111','EndDate111',0),
('one111','LOAPIP222','StartDate111','EndDate111',0);

-- COMMENTS:
-- only able to insert information for other tables if employee id exists in personal details table -- is that ok
-- so the excel file will be completely reject if the employee id does not match any existing 
-- residents in personal details table

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;