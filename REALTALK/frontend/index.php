<!-- frontend/index.php -->
<?php
    // Simula si el usuario está logueado (en el futuro se usará sesión real)
    $usuario = "Brosky";
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Inicio - Proyecto</title>
</head>
<body>
    <h1>Bienvenido, <?php echo $usuario; ?> 😎</h1>
    <p><a href="templates/login.php">Ir al login</a></p>
    <p><a href="templates/register.php">Ir al registro</a></p>
</body>
</html>
