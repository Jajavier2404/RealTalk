// register.js - Lógica de formulario registro ajustada para BD

document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('registerForm');
    const messageDiv = document.getElementById('message');

    // Manejar envío del formulario
    registerForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Deshabilitar botón durante el proceso
        const submitButton = registerForm.querySelector('button[type="submit"]');
        const originalText = submitButton.textContent;
        submitButton.disabled = true;
        submitButton.textContent = 'Creating account...';
        
        // Recopilar datos del formulario
        const formData = new FormData(registerForm);
        const data = {
            nombre_usuario: formData.get('nombre_usuario').trim(),
            correo: formData.get('correo').trim(),
            clave_hash: formData.get('clave_hash'), // Se hasheará en el backend
            terms: formData.get('terms') === 'on'
        };

        // ⭐ AGREGAR CONSOLE.LOG PARA VER LOS DATOS QUE SE ENVÍAN
        console.log('=== DATOS DEL FORMULARIO ===');
        console.log('JSON que se enviará:', JSON.stringify(data, null, 2));
        console.log('=============================');

        try {
            // Validaciones del lado del cliente
            if (!validateForm(data)) {
                return;
            }

            console.log('✅ Validación pasada, enviando al servidor...');

            // Enviar petición al backend
            const response = await fetch('../../backend/api/register.php', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            console.log('📡 Respuesta del servidor (status):', response.status);
            
            const result = await response.json();

            console.log('📥 Respuesta del servidor (data):', result);

            if (response.ok && result.success) {
                showMessage('Account created successfully! Redirecting to login...', 'success');
                
                // Redirigir al login después de 2 segundos
                setTimeout(() => {
                    window.location.href = 'login.php';
                }, 2000);
                
            } else {
                showMessage(result.message || 'Registration failed. Please try again.', 'error');
            }

        } catch (error) {
            console.error('❌ Error de registro:', error);
            showMessage('Connection error. Please check your internet connection and try again.', 'error');
        } finally {
            // Rehabilitar botón
            submitButton.disabled = false;
            submitButton.textContent = originalText;
        }
    });

    // Validación en tiempo real
    setupRealTimeValidation();
});

// Función para validar el formulario
function validateForm(data) {
    const errors = [];

    console.log('🔍 Iniciando validación del formulario...');

    // Validar nombre de usuario
    if (data.nombre_usuario.length < 3) {
        errors.push('Username must be at least 3 characters long');
    }

    if (data.nombre_usuario.length > 50) {
        errors.push('Username must be less than 50 characters');
    }

    // Validar que el nombre de usuario solo contenga caracteres válidos
    const usernameRegex = /^[a-zA-Z0-9_.-]+$/;
    if (!usernameRegex.test(data.nombre_usuario)) {
        errors.push('Username can only contain letters, numbers, underscore, period and hyphen');
    }

    // Validar email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(data.correo)) {
        errors.push('Please enter a valid email address');
    }

    if (data.correo.length > 100) {
        errors.push('Email must be less than 100 characters');
    }

    // Validar contraseña
    if (data.clave_hash.length < 8) {
        errors.push('Password must be at least 8 characters long');
    }

    if (!/(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/.test(data.clave_hash)) {
        errors.push('Password must contain at least one uppercase letter, one lowercase letter, and one number');
    }

    // Validar términos y condiciones
    if (!data.terms) {
        errors.push('You must agree to the Terms & Conditions');
    }

    if (errors.length > 0) {
        console.log('❌ Errores de validación:', errors);
        showMessage(errors.join('<br>'), 'error');
        return false;
    }

    console.log('✅ Validación exitosa');
    return true;
}

// Configurar validación en tiempo real
function setupRealTimeValidation() {
    const inputs = document.querySelectorAll('#registerForm input');
    
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateField(this);
        });

        input.addEventListener('input', function() {
            // Limpiar errores previos cuando el usuario empiece a escribir
            this.classList.remove('error');
            if (this.nextElementSibling && this.nextElementSibling.classList.contains('field-error')) {
                this.nextElementSibling.remove();
            }
        });
    });
}

// Validar campo individual
function validateField(field) {
    const value = field.value.trim();
    let isValid = true;
    let errorMessage = '';

    switch (field.name) {
        case 'nombre_usuario':
            if (value.length < 3) {
                isValid = false;
                errorMessage = 'Username must be at least 3 characters';
            } else if (value.length > 50) {
                isValid = false;
                errorMessage = 'Username must be less than 50 characters';
            } else if (!/^[a-zA-Z0-9_.-]+$/.test(value)) {
                isValid = false;
                errorMessage = 'Username can only contain letters, numbers, _ . -';
            }
            break;

        case 'correo':
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                isValid = false;
                errorMessage = 'Please enter a valid email address';
            } else if (value.length > 100) {
                isValid = false;
                errorMessage = 'Email must be less than 100 characters';
            }
            break;

        case 'clave_hash':
            if (value.length < 8) {
                isValid = false;
                errorMessage = 'Password must be at least 8 characters';
            } else if (!/(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/.test(value)) {
                isValid = false;
                errorMessage = 'Password must contain uppercase, lowercase, and number';
            }
            break;
    }

    // Mostrar/ocultar error en el campo
    if (!isValid) {
        showFieldError(field, errorMessage);
    } else {
        clearFieldError(field);
    }

    return isValid;
}

// Mostrar error en campo específico
function showFieldError(field, message) {
    field.classList.add('error');
    
    // Remover error anterior si existe
    if (field.nextElementSibling && field.nextElementSibling.classList.contains('field-error')) {
        field.nextElementSibling.remove();
    }
    
    // Agregar nuevo mensaje de error
    const errorDiv = document.createElement('div');
    errorDiv.className = 'field-error';
    errorDiv.textContent = message;
    field.parentNode.insertBefore(errorDiv, field.nextSibling);
}

// Limpiar error de campo
function clearFieldError(field) {
    field.classList.remove('error');
    if (field.nextElementSibling && field.nextElementSibling.classList.contains('field-error')) {
        field.nextElementSibling.remove();
    }
}

// Mostrar mensaje general
function showMessage(message, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.innerHTML = message;
    messageDiv.className = `message ${type}`;
    messageDiv.style.display = 'block';

    // Auto-ocultar después de 5 segundos
    setTimeout(() => {
        messageDiv.style.display = 'none';
    }, 5000);
}

// Toggle password visibility
function togglePassword() {
    const passwordInput = document.getElementById('clave_hash');
    const eyeIcon = document.querySelector('.eye-icon');
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        eyeIcon.textContent = '🙈';
    } else {
        passwordInput.type = 'password';
        eyeIcon.textContent = '👁';
    }
}

// Manejar botones de redes sociales
document.addEventListener('DOMContentLoaded', function() {
    const googleButton = document.querySelector('.google-button');
    const appleButton = document.querySelector('.apple-button');

    googleButton?.addEventListener('click', function() {
        showMessage('Google registration is not yet available', 'info');
        // Aquí implementarías la integración con Google OAuth
    });

    appleButton?.addEventListener('click', function() {
        showMessage('Apple registration is not yet available', 'info');
        // Aquí implementarías la integración con Apple Sign-In
    });
});