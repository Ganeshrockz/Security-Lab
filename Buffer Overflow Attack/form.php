<?php

    if( isset($_POST['submit']) )
    {
        $text = $_POST['text'];

        $query = "./a.out ".$text ;


        $queryReturnValue = system($query,$retval);
        echo "<br>";
        echo $retval; 
    }
?>

<!DOCTYPE html>
<html>
<head>
    <title>BUFFER OVERFLOW</title>
</head>
<body>
    <form method = "post" >
        <label>Enter Text : </label>
        <input type = "text" id="text" name="text">
        <button type="submit" id = "submit" name= "submit">Submit</button>
    </form>
</body>
</html>
