-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 01, 2025 at 05:20 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gestion_usuarios`
--

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `email`, `password`, `fecha_creacion`) VALUES
(1, 'John Doe', 'johndoe@example.com', 'securepassword123', '2025-03-31 04:48:27'),
(2, 'gustavo', 'gus@gmail.com', '$2b$12$NatKcvMIQINYMgbsqF0x6.SreBB6gWgQrxDxOF444EkGA5TVKb4ue', '2025-03-31 08:13:44'),
(3, 'Pedro', 'pedro@gmail.com', '$2b$12$y8e8qr6PGw/6Jn0X8e6imekn8bQXBlNaVIYqAmylBrjOpEHUlU2zK', '2025-04-01 00:49:46'),
(4, 'Juan', 'juan@hotmail.com', '$2b$12$Dl/qVShmwOHTjz1/fg/cTOv.gKVAJe7JSZzhXnHe6VUqFsbTs0sDa', '2025-04-01 00:59:58'),
(5, 'Vale', 'vale@gmail.com', '$2b$12$l1xabsWWJ3n5ffhoZQwS6OpIgZYdubO6irVATTiHiFSm5YDz9zg3S', '2025-04-01 01:04:06'),
(6, 'Roli', 'roli@gmail.com', '$2b$12$xFUcmfDCUO256FGvoygSH.SVkfOL7k9uV2.Y3kWmfkbAqCx7rj3xi', '2025-04-01 01:06:10'),
(7, 'Adriano', 'adriano@gmail.com', '$2b$12$6k4J7VlDAAcHZn5RTUoMbunxv3O4ol/EvMdO8eXTZ.0feMqwKUwym', '2025-04-01 01:07:16'),
(8, 'Nelson', 'nelson@gmail.com', '$2b$12$Af2zqFuC2XLQQ.ztAudHhu2pAi5Wc5Ahxl.4GX5aR.S5wx6Cu4ufy', '2025-04-01 01:27:07'),
(10, 'Andres', 'andres@gmail.com', '$2b$12$Rc868VNu9vVbRnb03xnIfuIKccqBNYZBiAY9DaGt/pQARlrGq4AW6', '2025-04-01 01:58:22'),
(11, 'Javier', 'javier@htomail.com', '$2b$12$f2/dWzW1/EFYpOZKLrJsk.CM0CXO.4PC9Qph/ZH/jivGFu0t8e0Pq', '2025-04-01 02:11:04');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
