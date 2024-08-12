document.addEventListener('DOMContentLoaded', () => {
    // Obtén referencias a los elementos del DOM
    const registerBtn = document.getElementById('register-btn');
    const loginBtn = document.getElementById('login-btn');
    const logoutBtn = document.getElementById('logout-btn');
    const registerForm = document.getElementById('register-form');
    const loginForm = document.getElementById('login-form');
    const forumSection = document.getElementById('forum');
    const registerCancel = document.getElementById('register-cancel');
    const loginCancel = document.getElementById('login-cancel');

    if (!registerBtn || !loginBtn || !logoutBtn || !registerForm || !loginForm || !forumSection || !registerCancel || !loginCancel) {
        console.error('Uno o más elementos del DOM no se encontraron.');
        return;
    }

    // Muestra el formulario de registro
    registerBtn.addEventListener('click', () => {
        registerForm.classList.remove('hidden');
        loginForm.classList.add('hidden');
        forumSection.classList.add('hidden');
    });

    // Muestra el formulario de inicio de sesión
    loginBtn.addEventListener('click', () => {
        loginForm.classList.remove('hidden');
        registerForm.classList.add('hidden');
        forumSection.classList.add('hidden');
    });

    // Oculta el formulario de registro
    registerCancel.addEventListener('click', () => {
        registerForm.classList.add('hidden');
    });

    // Oculta el formulario de inicio de sesión
    loginCancel.addEventListener('click', () => {
        loginForm.classList.add('hidden');
    });

    // Muestra la sección del foro y oculta los formularios si el usuario está conectado
    if (logoutBtn.classList.contains('visible')) {
        forumSection.classList.remove('hidden');
        registerForm.classList.add('hidden');
        loginForm.classList.add('hidden');
    } else {
        forumSection.classList.add('hidden');
    }
});