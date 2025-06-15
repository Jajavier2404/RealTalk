<!-- frontend/templates/login.php -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form id="loginForm">
        <input type="text" name="email" placeholder="Correo"><br>
        <input type="password" name="password" placeholder="Contraseña"><br>
        <button type="submit">Ingresar</button>
    </form>

    <script>
        const form = document.getElementById('loginForm');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            const data = {
                email: formData.get('email'),
                password: formData.get('password')
            };

            const response = await fetch('http://localhost:5000/', {
                method: 'GET'
            });
            const result = await response.json();
            alert("Respuesta de Flask: " + result.mensaje);
        });
    </script>
</body>
</html>
