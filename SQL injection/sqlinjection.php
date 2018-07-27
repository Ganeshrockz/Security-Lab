<?php

$con = mysqli_connect('127.0.0.1','root','');

if( !$con )
{
echo "Not Connected to Server";
}
if(!mysqli_select_db($con ,"userdetails"))
{
echo "Not Connected to DB";
}

if( isset( $_POST['submit']) )
{
$name= $_POST['username'];
$pass= $_POST['password'];
$rec = $con->prepare("SELECT Username,Age FROM creds WHERE Username = ?");
$rec->bind_param('s', $name);
$rec->execute();
$rec->bind_result($name,$age);
if (!$rec)
{
echo "Query Error";
}
echo "<b>Name</b>";
echo " ";
echo "<b>Age</b>";
echo "<br>";
while($rec->fetch() )
{
echo($name);
echo " ";
echo $age;
echo "<br>";
}
}
?>
<html>
<head>
<title>Sample Form</title>
</head>
<body>
<form method="post">
<label> Enter Name : </label>
<input name="username" type="text" placeholder="Enter Name">
<br>
<label>Enter Password:</label>
<input name="password" type="password" placeholder="Enter Password">
<br>
<button name="submit" type="submit">Submit</button>
</form>
</body>
</html>
