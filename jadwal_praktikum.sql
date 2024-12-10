-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 10, 2023 at 03:58 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jadwal_praktikum`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('fc4508e8d078');

-- --------------------------------------------------------

--
-- Table structure for table `jam_matkul`
--

CREATE TABLE `jam_matkul` (
  `id` int(11) NOT NULL,
  `jam` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jam_matkul`
--

INSERT INTO `jam_matkul` (`id`, `jam`) VALUES
(1, '07.30 - 09.00'),
(2, '09.10 - 10.40'),
(3, '10.50 - 12.20'),
(4, '13.00 - 14.30'),
(5, '14.40 - 16.10'),
(6, '16.20 - 17.50'),
(7, '08.15 - 09.45'),
(8, '10.00 - 11.30'),
(9, '13.30 - 15.00'),
(10, '15.10 - 16.40');

-- --------------------------------------------------------

--
-- Table structure for table `jam_matkul_reguler`
--

CREATE TABLE `jam_matkul_reguler` (
  `id` int(11) NOT NULL,
  `hari` varchar(150) NOT NULL,
  `kelas_id` int(11) NOT NULL,
  `jam_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jam_matkul_reguler`
--

INSERT INTO `jam_matkul_reguler` (`id`, `hari`, `kelas_id`, `jam_id`) VALUES
(1, 'senin', 1, 1),
(2, 'senin', 2, 1),
(3, 'senin', 13, 1),
(4, 'senin', 4, 1),
(5, 'senin', 6, 1),
(6, 'senin', 15, 2),
(7, 'senin', 2, 2),
(8, 'senin', 3, 2),
(9, 'senin', 14, 2),
(10, 'senin', 9, 2),
(11, 'senin', 7, 3),
(12, 'senin', 4, 3),
(13, 'senin', 17, 3),
(14, 'senin', 9, 3),
(15, 'senin', 18, 3),
(16, 'senin', 13, 3),
(17, 'senin', 6, 3),
(18, 'senin', 2, 3),
(19, 'senin', 3, 3),
(20, 'senin', 6, 4),
(21, 'senin', 16, 4),
(22, 'senin', 5, 4),
(23, 'senin', 3, 4),
(24, 'senin', 13, 5),
(25, 'senin', 15, 5),
(26, 'senin', 2, 5),
(27, 'selasa', 1, 1),
(28, 'selasa', 16, 1),
(29, 'selasa', 9, 1),
(30, 'selasa', 19, 1),
(31, 'selasa', 17, 1),
(32, 'selasa', 9, 1),
(33, 'selasa', 18, 1),
(34, 'selasa', 2, 2),
(35, 'selasa', 5, 2),
(36, 'selasa', 16, 2),
(37, 'selasa', 16, 2),
(38, 'selasa', 1, 3),
(39, 'selasa', 3, 3),
(40, 'selasa', 20, 3),
(41, 'selasa', 6, 3),
(42, 'selasa', 14, 3),
(43, 'selasa', 8, 4),
(44, 'selasa', 4, 4),
(45, 'selasa', 5, 4),
(46, 'selasa', 7, 5),
(47, 'selasa', 15, 5),
(48, 'selasa', 1, 5),
(49, 'selasa', 4, 5),
(50, 'selasa', 6, 5),
(51, 'rabu', 4, 1),
(52, 'rabu', 16, 1),
(53, 'rabu', 5, 1),
(54, 'rabu', 6, 1),
(55, 'rabu', 7, 1),
(56, 'rabu', 8, 1),
(57, 'rabu', 13, 2),
(58, 'rabu', 8, 2),
(59, 'rabu', 1, 2),
(60, 'rabu', 5, 2),
(61, 'rabu', 8, 3),
(62, 'rabu', 13, 3),
(63, 'rabu', 3, 3),
(64, 'rabu', 18, 3),
(65, 'rabu', 14, 4),
(66, 'rabu', 7, 4),
(67, 'rabu', 6, 4),
(68, 'rabu', 2, 4),
(69, 'rabu', 15, 5),
(70, 'kamis', 16, 1),
(71, 'kamis', 4, 1),
(72, 'kamis', 19, 1),
(73, 'kamis', 3, 1),
(74, 'kamis', 18, 1),
(75, 'kamis', 20, 1),
(76, 'kamis', 5, 2),
(77, 'kamis', 16, 2),
(78, 'kamis', 13, 2),
(79, 'kamis', 15, 2),
(80, 'kamis', 17, 2),
(81, 'kamis', 14, 3),
(82, 'kamis', 9, 3),
(83, 'kamis', 7, 3),
(84, 'kamis', 1, 3),
(85, 'kamis', 2, 3),
(86, 'kamis', 1, 4),
(87, 'kamis', 3, 4),
(88, 'kamis', 5, 4),
(89, 'kamis', 6, 4),
(90, 'kamis', 16, 4),
(91, 'kamis', 4, 4),
(92, 'jumat', 4, 8),
(93, 'jumat', 2, 8),
(94, 'jumat', 3, 8),
(95, 'jumat', 5, 8),
(96, 'jumat', 8, 8),
(97, 'jumat', 1, 9),
(98, 'jumat', 2, 9),
(99, 'jumat', 16, 9),
(100, 'jumat', 8, 9),
(101, 'jumat', 14, 10),
(102, 'jumat', 1, 10),
(103, 'jumat', 2, 10),
(104, 'jumat', 3, 10),
(105, 'jumat', 3, 11),
(106, 'jumat', 1, 11);

-- --------------------------------------------------------

--
-- Table structure for table `kelas_praktikum`
--

CREATE TABLE `kelas_praktikum` (
  `id` int(11) NOT NULL,
  `nama_kelas` varchar(150) NOT NULL,
  `kelas_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kelas_praktikum`
--

INSERT INTO `kelas_praktikum` (`id`, `nama_kelas`, `kelas_id`) VALUES
(1, 'A1', 1),
(2, 'A2', 1),
(3, 'B1', 2),
(4, 'B2', 2),
(5, 'C1', 3),
(6, 'C2', 3),
(7, 'A1', 4),
(8, 'A2', 4),
(9, 'B1', 5),
(10, 'B2', 5),
(11, 'C', 6),
(12, 'A1', 7),
(13, 'A2', 7),
(14, 'B1', 8),
(15, 'Perbaikan', 9),
(16, 'Gabungan', 10),
(17, 'A1', 11),
(18, 'B1', 12),
(19, 'A1', 13),
(20, 'A2', 13),
(21, 'B1', 14),
(22, 'B2', 14),
(23, 'C1', 15),
(24, 'C2', 15),
(25, 'C1', 6),
(26, 'C2', 6);

-- --------------------------------------------------------

--
-- Table structure for table `kelas_reguler`
--

CREATE TABLE `kelas_reguler` (
  `id` int(11) NOT NULL,
  `kelas` varchar(150) NOT NULL,
  `angkatan` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kelas_reguler`
--

INSERT INTO `kelas_reguler` (`id`, `kelas`, `angkatan`) VALUES
(1, 'A', '2022'),
(2, 'B', '2022'),
(3, 'C', '2022'),
(4, 'A', '2021'),
(5, 'B', '2021'),
(6, 'C', '2021'),
(7, 'A', 'Pilihan'),
(8, 'B', 'Pilihan'),
(9, 'Perbaikan', '2019'),
(10, 'Gabungan', '2021'),
(11, 'A', '19/20'),
(12, 'B', '19/20'),
(13, 'A', '2020'),
(14, 'B', '2020'),
(15, 'C', '2020'),
(16, 'Pilihan', 'Pilihan'),
(17, 'Perbaikan', '2018'),
(18, 'Perbaikan', '2020'),
(19, 'Perbaikan', '2017'),
(20, 'Perbaikan', '2021');

-- --------------------------------------------------------

--
-- Table structure for table `matakuliah_praktikum`
--

CREATE TABLE `matakuliah_praktikum` (
  `id` int(11) NOT NULL,
  `matakuliah` varchar(150) NOT NULL,
  `tipe_pc` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `matakuliah_praktikum`
--

INSERT INTO `matakuliah_praktikum` (`id`, `matakuliah`, `tipe_pc`) VALUES
(1, 'Algoritma Pemrograman Dasar', 'Good'),
(2, 'Basis Data', 'Good'),
(3, 'Digital Forensic And Cyber Crime', 'Super'),
(4, 'Framework-based Programming', 'Good'),
(5, 'Kecerdasan Buatan', 'Good'),
(6, 'Komputer Grafik', 'Super'),
(7, 'Organisasi dan Arsitektur Komputer', 'Good'),
(8, 'Pemrograman Web', 'Good'),
(9, 'Struktur Data', 'Good'),
(10, '3D dan Animasi', 'Super');

-- --------------------------------------------------------

--
-- Table structure for table `matkul_praktikum_kelas`
--

CREATE TABLE `matkul_praktikum_kelas` (
  `id` int(11) NOT NULL,
  `matkul_id` int(11) NOT NULL,
  `kelas_praktikum_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `matkul_praktikum_kelas`
--

INSERT INTO `matkul_praktikum_kelas` (`id`, `matkul_id`, `kelas_praktikum_id`) VALUES
(1, 10, 17),
(2, 10, 18),
(3, 1, 1),
(4, 1, 2),
(5, 1, 3),
(6, 1, 4),
(7, 1, 5),
(8, 1, 6),
(9, 2, 7),
(10, 2, 8),
(11, 2, 9),
(12, 2, 10),
(13, 3, 12),
(14, 3, 13),
(15, 3, 14),
(16, 4, 12),
(17, 4, 13),
(18, 5, 19),
(19, 5, 20),
(20, 5, 21),
(21, 5, 22),
(22, 5, 23),
(23, 5, 24),
(24, 5, 9),
(25, 5, 7),
(26, 5, 16),
(27, 6, 19),
(28, 6, 20),
(29, 6, 21),
(30, 6, 22),
(31, 6, 23),
(32, 6, 24),
(33, 7, 7),
(34, 7, 8),
(35, 7, 9),
(36, 7, 10),
(37, 7, 25),
(38, 7, 26),
(39, 8, 15),
(40, 8, 19),
(41, 8, 20),
(42, 8, 21),
(43, 8, 22),
(44, 8, 23),
(45, 8, 24),
(46, 9, 8),
(47, 9, 9),
(48, 9, 10),
(49, 9, 11);

-- --------------------------------------------------------

--
-- Table structure for table `ruangan`
--

CREATE TABLE `ruangan` (
  `id` int(11) NOT NULL,
  `ruangan` varchar(150) NOT NULL,
  `tipe_pc` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ruangan`
--

INSERT INTO `ruangan` (`id`, `ruangan`, `tipe_pc`) VALUES
(1, 'Lab.Multimedia', 'Super'),
(2, 'Lab. Robotik', 'Good'),
(3, 'Lab. Web Engineering', 'Good'),
(4, 'Lab. Network', 'Good'),
(5, 'Lab Komputasi (D208)', 'Good'),
(6, 'Lab Komputasi (D203)', 'Good');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `jam_matkul`
--
ALTER TABLE `jam_matkul`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jam_matkul_reguler`
--
ALTER TABLE `jam_matkul_reguler`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kelas_praktikum`
--
ALTER TABLE `kelas_praktikum`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kelas_id` (`kelas_id`);

--
-- Indexes for table `kelas_reguler`
--
ALTER TABLE `kelas_reguler`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `matakuliah_praktikum`
--
ALTER TABLE `matakuliah_praktikum`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `matkul_praktikum_kelas`
--
ALTER TABLE `matkul_praktikum_kelas`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ruangan`
--
ALTER TABLE `ruangan`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `jam_matkul`
--
ALTER TABLE `jam_matkul`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `jam_matkul_reguler`
--
ALTER TABLE `jam_matkul_reguler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;

--
-- AUTO_INCREMENT for table `kelas_praktikum`
--
ALTER TABLE `kelas_praktikum`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `kelas_reguler`
--
ALTER TABLE `kelas_reguler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `matakuliah_praktikum`
--
ALTER TABLE `matakuliah_praktikum`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `matkul_praktikum_kelas`
--
ALTER TABLE `matkul_praktikum_kelas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `ruangan`
--
ALTER TABLE `ruangan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `kelas_praktikum`
--
ALTER TABLE `kelas_praktikum`
  ADD CONSTRAINT `kelas_praktikum_ibfk_1` FOREIGN KEY (`kelas_id`) REFERENCES `kelas_reguler` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
