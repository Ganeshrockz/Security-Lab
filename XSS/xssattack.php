<?php
if(isset($_POST['sub']))
{
$name = $_POST['name'];
echo "You entered ".$name;
}
?>
<!DOCTYPE html>
<html>
<head>
<title>XSS</title>
</head>
<body>
<form method = "post">
<label>Enter Name</label>
<br>
<input type="text" name="name">
<button type="submit" name="sub">Submit</button>
</form>
</body>
</html>
