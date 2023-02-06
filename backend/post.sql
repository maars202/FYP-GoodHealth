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


CREATE TABLE `Post` (
     `id` INT AUTO_INCREMENT NOT NULL,
    `title` varchar(50) DEFAULT NULL,
    `content` varchar(50) DEFAULT NULL,
     primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

CREATE TABLE `Comment` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `content` varchar(50) DEFAULT NULL,
    `post_id` int NOT NULL,
    primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for table `Awards`
--
-- changing it to a key variable that is refereceable
ALTER TABLE `Comment`
  ADD KEY `post_id` (`post_id`);


ALTER TABLE `Comment`
  ADD CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `Personal_Details` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;


INSERT INTO `Post` (`title`, `content`)  VALUES
("hellooooo", "this is the content");

INSERT INTO `Comment` (`content`, `post_id`)  VALUES
("hellooooo comment", 1);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
