<?php
$date=date("Y/m/d");
$name= array("Bob", "Michael", "Cynthia", "Rasheed", "Mindy", "Susan");
//echo $date;

if($date=="2018/04/12" && $date<="2018/04/17"){
    echo "bob";
}

if($date=="2018/04/18" && $date<="2018/04/24"){
    echo"Michael";
}

if($date=="2018/04/25" && $date<="2018/04/30"){
    echo"Cynthia";
}

if($date=="2018/05/01" && $date<="2018/05/07"){
    echo"Rasheed";
}

if($date=="2018/05/08" && $date<="2018/05/14"){
    echo"Mindy";
}
if($date=="2018/05/15" && $date<="2018/05/21"){
    echo"Susan";
}
?>