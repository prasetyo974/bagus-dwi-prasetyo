<?php
$suhu=20;//variabel
if($suhu>30 && $suhu<100){
    $hasil= "Cuaca Panas";
}elseif($suhu<30 && $suhu>0){
    $hasil= "Cuaca Dingin"; 
}else{
    $hasil="Cuca Extrem";
}
echo $hasil;
?>