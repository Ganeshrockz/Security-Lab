<?php

function clean($string)
{
return preg_replace('/[^A-Za-z0-9\-]/', '', $string);
}

if(isset($_POST['sub']))
{
$name = $_POST['name'];
$name = clean($name);
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

