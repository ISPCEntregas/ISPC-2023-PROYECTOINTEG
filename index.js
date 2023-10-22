// Función para obtener usuarios del almacenamiento local
function getUsersFromLocalStorage() {
    const usersJson = localStorage.getItem('users');
    return usersJson ? JSON.parse(usersJson) : [];
}

// Función para guardar usuarios en el almacenamiento local
function saveUsersToLocalStorage(users) {
    localStorage.setItem('users', JSON.stringify(users));
}


let users = getUsersFromLocalStorage();

document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const loginUsername = document.getElementById('login-username').value;
    const loginPassword = document.getElementById('login-password').value;

    const user = users.find(u => u.username === loginUsername && u.password === loginPassword);

    if (user) {
        document.getElementById('login-message').textContent = '¡Login exitoso! Bienvenido, ' + user.username + '!';
        setTimeout(function() {
            window.location.href = 'index.html'; 
        }, 2000);
    } else {
        document.getElementById('login-message').textContent = 'Nombre de usuario o contraseña incorrectos.';
    }
});

document.getElementById('register-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const registerUsername = document.getElementById('register-username').value;
    const registerPassword = document.getElementById('register-password').value;

    const firstName = document.getElementById('first-name').value;
    const lastName = document.getElementById('last-name').value;
    const dni = document.getElementById('dni').value;

    let valid = true;

    if (users.some(u => u.username === registerUsername)) {
        document.getElementById('register-message').textContent = 'El nombre de usuario ya está en uso.';
        valid = false;
    }

    if (dni < 1000000 || dni > 99999999) {
        document.getElementById('register-message').textContent = 'DNI inválido. Debe tener entre 7 y 8 dígitos.';
        valid = false;
    }

    if (valid) {
        users.push({
            username: registerUsername,
            password: registerPassword,
            firstName: firstName,
            lastName: lastName,
            dni: dni
        });

        saveUsersToLocalStorage(users);
        document.getElementById('register-message').textContent = 'Registro exitoso. ¡Bienvenido, ' + registerUsername + '!';
        
  
        const registerForm = document.getElementById('register-form');
        registerForm.classList.add('hidden');
    }
});


document.getElementById('toggle-button').addEventListener('click', function() {
    const registerForm = document.getElementById('register-form');
    registerForm.classList.remove('hidden');
    document.getElementById('register-message').textContent = '';
});
