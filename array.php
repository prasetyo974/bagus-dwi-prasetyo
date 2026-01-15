<?php
$arraybuah[0] = 'apple';
$arraybuah[1] = 'orange';
$arraybuah[2] = 'grape';
$arraybuah[3] = 'durian';
$arraybuah[4] = 'banana';
$arraybuah[5] = 'water melon';
//&array numerik -> index angka
$jmldata = count($arraybuah);
echo "<select>";
for ($i=0; $i < $jmldata; $i++){ 
    echo "<option>". $arraybuah [$i]."</option>";
}
echo "</select>". "<br>";

//array asosiatif -> index huruf
$arrayAvenger =[
    [
        "name" => "iron Man",
        "age" => 45,
        "color" => "red",
    ],
    [
        "name" => "capt amerika",
        "age" => 145,
        "color" => "red, blue",
    ],
    [
        "name" => "Hulk",
        "age" => 45,
        "color" => "green",
    ],
];
foreach ($arrayAvenger as $data) {
    echo "Name : ".$data['name'];
    echo " -Age : ".$data['age'];
    echo " -Color : ".$data['color']. "<br>";
}
?>


