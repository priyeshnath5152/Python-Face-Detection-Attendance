-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 25, 2021 at 04:06 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Dep` varchar(50) NOT NULL,
  `Course` varchar(50) NOT NULL,
  `Year` varchar(50) NOT NULL,
  `Semester` varchar(50) NOT NULL,
  `Student_Id` varchar(45) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Division` varchar(50) NOT NULL,
  `Rollno` varchar(50) NOT NULL,
  `Gender` varchar(50) NOT NULL,
  `DOB` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Phone` varchar(50) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Teacher` varchar(50) NOT NULL,
  `PhotoSample` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Dep`, `Course`, `Year`, `Semester`, `Student_Id`, `Name`, `Division`, `Rollno`, `Gender`, `DOB`, `Email`, `Phone`, `Address`, `Teacher`, `PhotoSample`) VALUES
('ComputerScience', 'MCA', 'Select Year', 'semester-II', '1', 'Priyesh Tiwari', 'Select Division', '202143', 'Male', '06/10/2021', 'priyesht5152@gmail.com', '7219321131', 'Nalasopara(w)', 'Vikram P', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`Student_Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
