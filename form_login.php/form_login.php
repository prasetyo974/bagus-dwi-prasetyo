<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="proses.php" method="get">
        Username:
        <input type="text" name="usrnm"><br>
        <select name="userType">
            <option value="admin">Admin</option>
            <option value="finance">Finance</option>
            <option value="logistik">logistik</option>
        </select>
        password:
        <input type="password" name="pwd">
        <button name="login" type="submit">log in </button>
        <button type="reset">reset</button>
    </form>
</body>
</html>