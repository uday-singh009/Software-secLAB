
<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

$conn = mysqli_connect("localhost", "root", "", "simple_login");
$message = "";

if (isset($_POST['submit'])) {
    $username = mysqli_real_escape_string($conn, $_POST['username']);
    $password_input = $_POST['password'];

    // CHECK IF USER EXISTS
    $stmt = mysqli_prepare($conn, "SELECT password_hash, salt FROM users WHERE username = ?");
    mysqli_stmt_bind_param($stmt, "s", $username);
    mysqli_stmt_execute($stmt);
    $result = mysqli_stmt_get_result($stmt);

    if ($user = mysqli_fetch_assoc($result)) {
        // --- LOGIN LOGIC ---
        $stored_hash = $user['password_hash'];
        $stored_salt = $user['salt'];

        // Hash the input using the stored salt
        $check_hash = hash('sha256', $password_input . $stored_salt);

        if ($check_hash === $stored_hash) {
            $message = "ACCESS GRANTED 🔓<br><small>Verified with Salt: $stored_salt</small>";
        } else {
            $message = "INVALID PASSWORD ❌";
        }
    } else {
        // --- REGISTRATION LOGIC (Auto-create if user doesn't exist) ---
        // 1. Generate a unique random salt
        $new_salt = bin2hex(random_bytes(16)); 
        
        // 2. Create the hash (Password + Salt)
        $new_hash = hash('sha256', $password_input . $new_salt);

        $reg_stmt = mysqli_prepare($conn, "INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)");
        mysqli_stmt_bind_param($reg_stmt, "sss", $username, $new_hash, $new_salt);
        
        if (mysqli_stmt_execute($reg_stmt)) {
            $message = "NEW USER REGISTERED ✅<br><small>Salt & Hash stored in DB</small>";
        }
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>AAA Secure Terminal</title>
    <style>
        body { background: black; color: #00ff00; font-family: 'Courier New', monospace; overflow: hidden; }
        canvas { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.4; }
        .card {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            width: 400px; padding: 30px; background: rgba(0, 20, 0, 0.9);
            border: 2px solid #00ff00; border-radius: 10px; text-align: center;
            box-shadow: 0 0 20px #00ff00;
        }
        input {
            width: 100%; padding: 12px; margin: 10px 0;
            background: black; border: 1px solid #00ff00; color: #00ff00;
        }
        input[type="submit"] { background: #00ff00; color: black; font-weight: bold; cursor: pointer; }
        input[type="submit"]:hover { background: #003300; color: #00ff00; }
        .message { margin-top: 20px; padding: 10px; border: 1px dashed #00ff00; font-size: 0.9em; }
        h2 { letter-spacing: 3px; margin-bottom: 20px; }
    </style>
</head>
<body>

<canvas id="matrix"></canvas>

<div class="card">
    <h2>SYSTEM ACCESS</h2>
    <p style="font-size: 10px;">[ ALGORITHM: SHA-256 + MANUAL SALT ]</p>
    
    <form method="POST">
        <input type="text" name="username" placeholder="USERNAME" required>
        <input type="password" name="password" placeholder="PASSWORD" required>
        <input type="submit" name="submit" value="EXECUTE_AUTH">
    </form>

    <?php if($message != ""): ?>
        <div class="message"><?php echo $message; ?></div>
    <?php endif; ?>
</div>

<script>
    const canvas = document.getElementById('matrix');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const letters = "0101010101010101";
    const fontSize = 16;
    const columns = canvas.width / fontSize;
    const drops = Array(Math.floor(columns)).fill(1);

    function draw() {
        ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = "#00ff00";
        ctx.font = fontSize + "px monospace";
        for (let i = 0; i < drops.length; i++) {
            const text = letters.charAt(Math.floor(Math.random() * letters.length));
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
            drops[i]++;
        }
    }
    setInterval(draw, 33);
</script>

</body>
</html>
