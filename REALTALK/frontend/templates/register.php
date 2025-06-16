<?php
session_start();

// Si ya está logueado, redirigir al chat
if (isset($_SESSION['user_id'])) {
    header('Location: chat.php');
    exit();
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crear cuenta - AML</title>
    <link rel="stylesheet" href="../public/css/register.css">
</head>
<body>
    <div class="auth-container">
        <div class="auth-card">
            <!-- Sección izquierda con imagen -->
            <div class="auth-image-section">
                <div class="auth-brand">
                    <h1>AML</h1>
                </div>
                <button class="back-to-website" onclick="window.location.href='/'">
                    ← Back to website
                </button>
                
                <div class="auth-image-content">
                    <div class="mountain-landscape"></div>
                    <div class="auth-tagline">
                        <h2>Capturing Moments,<br>Creating Memories</h2>
                    </div>
                    <div class="pagination-dots">
                        <span class="dot"></span>
                        <span class="dot"></span>
                        <span class="dot active"></span>
                    </div>
                </div>
            </div>

            <!-- Sección derecha con formulario -->
            <div class="auth-form-section">
                <div class="auth-form-container">
                    <h2>Create an account</h2>
                    <p class="auth-subtitle">
                        Already have an account? 
                        <a href="login.php" class="auth-link">Log in</a>
                    </p>

                    <form id="registerForm" class="auth-form">
                        <div class="form-group">
                            <input type="text" id="nombre_usuario" name="nombre_usuario" placeholder="Username" required>
                        </div>
                        
                        <div class="form-group">
                            <input type="email" id="correo" name="correo" placeholder="Email" required>
                        </div>
                        
                        <div class="form-group password-group">
                            <input type="password" id="clave_hash" name="clave_hash" placeholder="Enter your password" required>
                            <button type="button" class="password-toggle" onclick="togglePassword()">
                                <span class="eye-icon">👁</span>
                            </button>
                        </div>

                        <div class="form-group checkbox-group">
                            <input type="checkbox" id="terms" name="terms" required>
                            <label for="terms">
                                I agree to the <a href="#" class="terms-link">Terms & Conditions</a>
                            </label>
                        </div>

                        <button type="submit" class="auth-button">Create account</button>

                        <div class="auth-divider">
                            <span>Or register with</span>
                        </div>

                        <div class="social-buttons">
                            <button type="button" class="social-button google-button">
                                <img src="../public/img/google-icon.svg" alt="Google" class="social-icon">
                                Google
                            </button>
                            <button type="button" class="social-button apple-button">
                                <img src="../public/img/apple-icon.svg" alt="Apple" class="social-icon">
                                Apple
                            </button>
                        </div>
                    </form>

                    <!-- Área de mensajes de error/éxito -->
                    <div id="message" class="message" style="display: none;"></div>
                </div>
            </div>
        </div>
    </div>

    <script src="../public/js/register.js"></script>
</body>
</html>