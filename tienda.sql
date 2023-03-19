-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-03-2023 a las 21:27:30
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tienda`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compras`
--

CREATE TABLE `compras` (
  `id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `cedula` varchar(15) NOT NULL,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `celular` varchar(15) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `id_carrito` varchar(50) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_total` int(11) NOT NULL,
  `fecha` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `compras`
--

INSERT INTO `compras` (`id`, `email`, `direccion`, `cedula`, `nombres`, `apellidos`, `celular`, `id_producto`, `id_carrito`, `imagen`, `cantidad`, `precio_total`, `fecha`) VALUES
(14, 'sample@example.com', 'potosi', '123456789', 'Sample', 'Ejemplo', '3121546787', 25, '', 'productos faciales_2023205406.png', 3, 150000, '2023-03-17 10:00:51'),
(15, 'sample@example.com', 'potosi', '123456789', 'Sample', 'Ejemplo', '3121546787', 24, '', 'perfumes_2023162219.png', 3, 300000, '2023-03-17 10:00:51'),
(16, 'sample@example.com', 'Potosi', '123456789', 'Sample', 'Ejemplo', '3121546787', 14, 'cart20230317103027', '2023152612_perfume de maracuya.jpg', 1, 54000, '2023-03-17 10:30:38'),
(17, 'sample@example.com', 'Ipiales', '123456789', 'Sample', 'Ejemplo', '3121546787', 24, 'cart20230317104413', 'perfumes_2023162219.png', 1, 100000, '2023-03-17 10:44:31'),
(18, 'sample@example.com', 'Ipiales', '123456789', 'Sample', 'Ejemplo', '3121546787', 25, 'cart20230317104413', 'productos faciales_2023205406.png', 3, 150000, '2023-03-17 10:44:31'),
(19, 'sample@example.com', 'Ipiales', '123456789', 'Sample', 'Ejemplo', '3121546787', 18, 'cart20230317104749', 'productos cabello_2023161906.png', 1, 22000, '2023-03-17 10:48:06'),
(20, 'sample@example.com', 'Ipiales', '123456789', 'Sample', 'Ejemplo', '3121546787', 13, 'cart20230317104749', 'productos faciales_2023205451.png', 2, 400000, '2023-03-17 10:48:06'),
(21, 'sample@example.com', 'Nariño', '123456789', 'Sample', 'Ejemplo', '3121546787', 24, 'cart20230317111001', 'perfumes_2023162219.png', 2, 200000, '2023-03-17 11:10:28'),
(22, 'sample@example.com', 'Nariño', '123456789', 'Sample', 'Ejemplo', '3121546787', 18, 'cart20230317111001', 'productos cabello_2023161906.png', 2, 44000, '2023-03-17 11:10:28'),
(23, 'sample@example.com', 'nariño', '123456789', 'Sample', 'Ejemplo', '3121546787', 13, 'cart20230317111114', 'productos faciales_2023205451.png', 1, 200000, '2023-03-17 11:11:35'),
(24, 'sample@example.com', 'nariño', '123456789', 'Sample', 'Ejemplo', '3121546787', 24, 'cart20230317111114', 'perfumes_2023162219.png', 3, 300000, '2023-03-17 11:11:35'),
(25, 'sample@example.com', 'ds', '123456789', 'Sample', 'Ejemplo', '3121546787', 14, 'cart20230317111920', '2023152612_perfume de maracuya.jpg', 1, 54000, '2023-03-17 11:19:28'),
(26, 'sample@example.com', 'dad', '123456789', 'Sample', 'Ejemplo', '3121546787', 24, 'cart20230317112129', 'perfumes_2023162219.png', 1, 100000, '2023-03-17 11:21:38'),
(27, 'minombre@gmail.com', 'Carera 12', '123457888', 'Mi nombre', 'Mi apellido', '3178945656', 13, 'cart20230317141329', 'productos faciales_2023205451.png', 1, 200000, '2023-03-17 14:15:02'),
(28, 'minombre@gmail.com', 'Carera 12', '123457888', 'Mi nombre', 'Mi apellido', '3178945656', 24, 'cart20230317141329', 'perfumes_2023162219.png', 1, 100000, '2023-03-17 14:15:02');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `imagen` varchar(255) NOT NULL,
  `tipo` varchar(20) NOT NULL,
  `cantidad` int(2) DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  `precio` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `nombre`, `imagen`, `tipo`, `cantidad`, `descripcion`, `precio`) VALUES
(13, 'crema', 'productos faciales_2023205451.png', 'productos faciales', 40, 'Crema protector solar', 200000),
(14, 'Natura perfume de maracuyá', '2023152612_perfume de maracuya.jpg', 'perfumes', 1, 'Perfume de maracuyá ', 54000),
(18, 'Shampoo de manzanilla (nuevo)', 'productos cabello_2023161906.png', 'productos cabello', 56, 'Shampoo de manzanilla de marca marcel france ', 22000),
(24, 'Perfume para chicos', 'perfumes_2023162219.png', 'perfumes', 28, 'un perfume que impresionará', 100000),
(25, 'Cremita', 'productos faciales_2023205406.png', 'productos faciales', 43, 'Para las arrugas', 50000),
(26, 'Produc1', 'productos cabello_20230317122140.png', 'productos cabello', 48, 'Producto para el cabello', 12000),
(27, 'Producto2', 'productos cabello_20230317122305.png', 'productos cabello', 45, 'Anticaida de cabello', 45000),
(28, 'Producto3', 'productos cabello_20230317122345.png', 'productos cabello', 11, 'Otro producto', 23000),
(29, 'Producto4', 'productos cabello_20230317131017.png', 'productos cabello', 23, 'Asdfghjkl', 12000),
(30, 'Producto5', 'productos cabello_20230317131047.png', 'productos cabello', 54, 'Acond', 32000),
(31, 'Prod 11', 'perfumes_20230317142115.png', 'perfumes', 118, 'Perfumes de chicas', 12),
(32, 'Producto prueba', 'productos faciales_20230317142236.png', 'productos faciales', 0, 'Producto ppara hacer pruebas', 12000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(15) NOT NULL,
  `cedula` varchar(30) NOT NULL,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `celular` varchar(10) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `usuario` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `tipoUsuario` enum('admin','cliente') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `cedula`, `nombres`, `apellidos`, `celular`, `correo`, `usuario`, `password`, `tipoUsuario`) VALUES
(1, '1234567890', 'Administrador', 'General', '3123456789', 'admin@gmail.com', 'admin', 'admin', 'admin'),
(2, '1099567898', 'Primer', 'Cliente', '3124578985', 'primer@mail.com', 'usu1', 'usu1', 'cliente'),
(3, '123456789', 'Sample', 'Ejemplo', '3121546787', 'sample@example.com', 'sample@example.com', 'sample', 'cliente');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_producto` (`id_producto`),
  ADD KEY `email` (`email`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `compras`
--
ALTER TABLE `compras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `compras`
--
ALTER TABLE `compras`
  ADD CONSTRAINT `compras_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
