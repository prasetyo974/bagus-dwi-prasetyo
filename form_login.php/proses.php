<?php
$username = $_GET['usrnm'];
$password = $_GET['pwd'];
$userType = $_GET['userType'];

if($userType=="admin" && $username=="useradmin"){
    if($password=="123"){
        echo "selamat datang admin";
        exit();
    }else{
        echo "password anda salah";
    }
}elseif($userType=="finance" && $username=="userfinance"){
    if ($password=="1234"){
        echo "selamat datang user finance";
        exit();
    }else{
        echo "password anda salah";
    }
}elseif($userType=="logistik" && $username=="userlogistik"){
    if ($password=="12345"){
        echo "selamat datang user logistik";
        exit();
        }else{
            echo "password anda salah";
        }   
}else{
    echo "username anda salah";
}

?>