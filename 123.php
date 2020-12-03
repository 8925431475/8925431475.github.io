<?php

$userid=$_POST['id'];
$usern=$_POST['name1'];
$dob=$_POST['date1'];
$town1=$_POST['town1'];

if(!empty($userid)||!empty($usern)||!empty($dob)||!empty($town1))
{
    $host="localhost";

    $dbusername="root";

    $dbpass="";

    $dbname="mystyle";

    $con= new mysqli($host, $dbusername,$dbpass,$dbname);

    if(mysqli_connect_error()){

        die('connection error ('.mysqli_connect_errno() .') '. mysqli_connect_error());
    }

    else{

        $outcome1="INSERT Into userd(userid,username,userdob,hometown)values(?,?,?,?)";

        $stm=$con->prepare($outcome1);

        $stm->bind_param("isss",$userid,$usern,$dob,$town1);
        $stm->execute();

        echo " New record inserted successfully";

    }

    $stm->close();
    $con->close();

    die();

}

?>