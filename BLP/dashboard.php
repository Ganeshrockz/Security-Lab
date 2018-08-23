<?php
session_start();
$con = mysqli_connect('127.0.0.1','root','');
if( !$con )
{
echo "Not Connected to Server";
}
if(!mysqli_select_db($con ,"blp"))
{
echo "Not Connected to DB";
}
$fileRead=0;
$fileWrite=0;
if( isset( $_POST['sub']) )
{
$fname= $_POST['fname'];
$mode= $_POST['mode'];
$query = "SELECT * FROM file WHERE name = '$fname'";
$rec = mysqli_query( $con, $query );
if (!$rec)
{
echo "Query Error";
}
while( $rec1 = mysqli_fetch_assoc($rec) )
{
$fileAccessLevel = $rec1['level'];
}
$currentUser = $_SESSION['user'];
$query = "SELECT * FROM access WHERE uname='$currentUser'";
$rec = mysqli_query( $con , $query);
if (!$rec)
{
echo "Query Error";
}
while ( $rec1 = mysqli_fetch_assoc($rec) )
{
$userAccessLevel = $rec1['level'];
}
if($mode == 'r')
{
if($fileAccessLevel > $userAccessLevel)
{
echo "<script>alert('User cannot read the file')</script>";
}
else
{
$fileName = "files/".$fname;
$myfile = fopen($fileName, "r") or die("Unable to open file!");
$fileContents =  fread($myfile,filesize($fileName));
fclose($myfile);
$fileRead=1;
}
}
else
{
if($fileAccessLevel < $userAccessLevel)
{
echo "<script> alert('User cannot write the file')</script>";
}
else
{
//File write code
$fileContents = $_POST['fileContent'];
$fileName = "files/".$fname;
$query = "bash sample.bash".$fileName." ".$fileContents;
$queryReturnValue = shell_exec($query);
$fileWrite=1;
}
}
}
?>

<!DOCTYPE html>
<html>
<head>
<title>BLP</title>
</head>
<body>
<h2>List of files</h2>
<ol>
<li>a.txt</li>
<li>b.txt</li>
<li>c.txt</li>
</ol>
<form method="post" action="#">
<label>Enter File Name</label>
<input type="text" name="fname" id="fname" required>
<br>
<label>Enter Mode(r or w)</label>
<input type="text" name="mode" id="mode" required>
<br>
<label> Enter text to be written(w mode)</label>
<textarea name="fileContent" id="fileContent" rows="4" cols="50">
</textarea>
<br>
<button name="sub">Access</button>
</form>
<br>
<a href="http://localhost/BLP/index.php">Logout</a>
<?php
if($fileRead == 1)
{
echo "<h1>FileContents</h1>";
echo "<br>";
echo $fileContents;
}
else if($fileWrite == 1)
{
echo "<h1>File Successfully Written</h1>";
}
?>
</body>
</html>
