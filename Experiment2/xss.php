<h2>XSS Demo Page</h2>

<form method="GET">
    Enter your name: <input type="text" name="name">
    <button type="submit">Submit</button>
</form>

<?php
if (isset($_GET['name'])) {
    // ❌ Vulnerable to XSS
    echo "<h3>Hello " . $_GET['name'] . "</h3>";
}
?>
