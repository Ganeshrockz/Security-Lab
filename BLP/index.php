<?php
session_start();
$_SESSION['user']="";
$con = mysqli_connect('127.0.0.1','root','');
if( !$con )
{
echo "Not Connected to Server";
}
if(!mysqli_select_db($con ,"blp"))
{
echo "Not Connected to DB";
}
if( isset( $_POST['sub']) )
{
$name= $_POST['uname'];
$pass= $_POST['pass'];
$query = "SELECT * FROM users WHERE uname = '$name' AND password = '$pass'";
$rec = mysqli_query( $con, $query );
if (!$rec)
{
echo "Query Error";
}
$flag=0;
if( mysqli_num_rows($rec) == 0)
{
echo "Invalid login";
$flag=1;
header("refresh=1;Location: http://localhost/BLP/index.php");
}
if($flag==0)
{
$_SESSION['user'] = $name;
header("Location: http://localhost/BLP/dashboard.php");
}
}
?>

<!DOCTYPE html>
<html>
<head>
<title>BLP</title>
</head>
<body>
<form method="post" action="#">
<label>Username</label>
<input type="text" name="uname" id="uname">
<br>
<label>Password</label>
<input type="password" name="pass" id="pass">
<br>
<button name="sub">Login</button>
</form>
</body>
</html>
