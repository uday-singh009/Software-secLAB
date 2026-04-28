<?php
$conn = mysqli_connect("localhost", "root", "", "security_lab");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

echo "DB Connected"; // TEMP TEST
?>
