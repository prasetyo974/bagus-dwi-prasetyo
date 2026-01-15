<?php
$mahasiswa = [
    ["nim" => "2023001", "nama" => "Andi", "nilai" => 85],
    ["nim" => "2023002", "nama" => "Budi", "nilai" => 72],
    ["nim" => "2023003", "nama" => "Citra", "nilai" => 90],
    ["nim" => "2023004", "nama" => "Dewi", "nilai" => 60],
];

$jmlhlulus = 0;
?>

<table width="50%" border="1">
    <tr>
        <td>No</td>
        <td>NIM</td>
        <td>Nama</td>
        <td>Nilai</td>
        <td>Keterangan</td>
    </tr>

    <?php $no = 1; ?>
    <?php 
    foreach ($mahasiswa as $key =>$value) {
        $no = $key+1;
    
        if ($value["nilai"] >= 80) {
            $keterangan = "Lulus";
        } 
        else {
            $keterangan = "Tidak Lulus";
        }
        echo "
        <tr>
            <td>$no</td>
            <td>$value[nim]</td> 
            <td>$value[nama]</td>
            <td>$value[nilai]</td>
            <td>$keterangan</td>
        </tr>
        ";
    }
?>
</table>
