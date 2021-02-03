<?php

// Получаем данные из формы
$name = $_POST['name'];
$email = $_POST['email'];
$theme = $_POST['theme'];
$message = $_POST['message'];

// Преобразовываем символы
$name = htmlspecialchars($name);
$email = htmlspecialchars($email);
$theme = htmlspecialchars($theme);
$message = htmlspecialchars($message);

// Декодируем url
$name = urldecode($name);
$email = urldecode($email);
$theme = urldecode($theme);
$message = urldecode($message);

// Удаляем проблемы с начала и конца строки
$name = trim($name);
$email = trim($email);
$theme = trim($theme);
$message = trim($message);

 mail("anastasia.gisina@inbox.ru", $theme, $message,"From: example2@mail.ru \r\n");
?>