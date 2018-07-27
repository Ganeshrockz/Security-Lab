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
$query = "SELECT * FROM creds WHERE Username = '$name' AND Password = '$pass'";
$rec = mysqli_query( $con, $query );
if (!$rec)
{
echo "Query Error";
}
$flag=0;
if( mysqli_num_rows($rec) == 0)
{
echo "No records";
$flag=1;
}
if($flag==0)
{
echo "<b>Name</b>";
echo " ";
echo "<b>Age</b>";
echo "<br>";
while( $record = mysqli_fetch_assoc($rec) )
{
echo $record['Username'];
echo " ";
echo $record['Age'];
echo "<br>";
}
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
