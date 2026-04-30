<?php
$conn = mysqli_connect("localhost", "root", "", "test");
if(!$conn){
    http_response_code(500);
    echo "Database connection error";
    exit;
}

$ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
$failedFile = __DIR__ . '/failed_logins.json';
$now = time();
$limit = 5; // attempts
$window = 600; // seconds window to count attempts
$lockout = 900; // lockout seconds if exceeded

$failed = [];
if(file_exists($failedFile)){
    $raw = file_get_contents($failedFile);
    $failed = json_decode($raw, true) ?: [];
}

// prune old attempts
if(!empty($failed[$ip])){
    $failed[$ip] = array_filter($failed[$ip], function($t) use ($now, $window){
        return ($t > $now - $window);
    });
    if(count($failed[$ip]) >= $limit){
        $last = end($failed[$ip]);
        if($last > $now - $lockout){
            http_response_code(429);
            echo "Too many login attempts. Try again later.";
            exit;
        }
    }
}

$username = isset($_POST['username']) ? trim($_POST['username']) : '';
$password = isset($_POST['password']) ? $_POST['password'] : '';

if($username === '' || $password === ''){
    echo "<h2>Missing username or password</h2>";
    exit;
}

if(strlen($username) > 100 || strlen($password) > 200){
    echo "<h2>Invalid input</h2>";
    exit;
}

$stmt = $conn->prepare("SELECT id, username, password FROM users WHERE username = ?");
if(!$stmt){
    echo "<h2>Server error</h2>";
    exit;
}
$stmt->bind_param("s", $username);
$stmt->execute();
$result = $stmt->get_result();

if($row = $result->fetch_assoc()){
    if(password_verify($password, $row['password'])){
        // success -> clear failed attempts for IP
        if(isset($failed[$ip])){ unset($failed[$ip]); file_put_contents($failedFile, json_encode($failed)); }
        echo "<h2>Login Successful</h2>";
    } else {
        // record failed attempt
        $failed[$ip][] = $now;
        file_put_contents($failedFile, json_encode($failed));
        echo "<h2>Invalid Password</h2>";
    }
} else {
    // record failed attempt
    $failed[$ip][] = $now;
    file_put_contents($failedFile, json_encode($failed));
    echo "<h2>User Not Found</h2>";
}
?>