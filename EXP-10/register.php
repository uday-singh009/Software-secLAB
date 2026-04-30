<?php
$conn = mysqli_connect("localhost", "root", "", "test");
if(!$conn){
	http_response_code(500);
	echo "Database connection error";
	exit;
}

// Simple protection: require a secret to allow registration (change before use)
$REG_SECRET = 'CHANGE_ME';
$provided = isset($_POST['secret']) ? $_POST['secret'] : '';
if($provided !== $REG_SECRET){
	http_response_code(403);
	echo "Registration disabled.";
	exit;
}

$username = isset($_POST['username']) ? trim($_POST['username']) : '';
$password = isset($_POST['password']) ? $_POST['password'] : '';

if($username === '' || $password === ''){
	echo "Missing username or password";
	exit;
}

if(strlen($username) > 100 || strlen($password) > 200){
	echo "Invalid input";
	exit;
}

$hash = password_hash($password, PASSWORD_BCRYPT);

$stmt = $conn->prepare("SELECT id FROM users WHERE username = ?");
$stmt->bind_param("s", $username);
$stmt->execute();
$res = $stmt->get_result();
if($res->fetch_assoc()){
	echo "User already exists";
	exit;
}

$stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
$stmt->bind_param("ss", $username, $hash);
if($stmt->execute()){
	echo "User registered with hashed password!";
} else {
	http_response_code(500);
	echo "Registration failed";
}
?>