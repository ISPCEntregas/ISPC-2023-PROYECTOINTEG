function cargarZapatillas() {
    fetch('http://127.0.0.1:5000/zapatillas')
        .then(response => response.json())
        .then(data => {
            const zapatillaList = document.getElementById('zapatilla-list');
            zapatillaList.innerHTML = ''; 

            data.forEach(zapatilla => {
                const listItem = document.createElement('li');
                listItem.textContent = `ID: ${zapatilla.id} Nombre: ${zapatilla.nombre}, Marca: ${zapatilla.marca}, Talla: ${zapatilla.talla}, Precio: ${zapatilla.precio}, Categoría: ${zapatilla.categoria}`;
                zapatillaList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

document.getElementById('crear-zapatilla-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const marcaId = parseInt(document.getElementById('marca_id').value);
    const talla = parseFloat(document.getElementById('talla').value);
    const precio = parseFloat(document.getElementById('precio').value);
    const categoriaId = parseInt(document.getElementById('categoria_id').value);

    const nuevaZapatilla = {
        nombre: nombre,
        marca_id: marcaId,
        talla: talla,
        precio: precio,
        categoria_id: categoriaId
    };

    fetch('http://127.0.0.1:5000/zapatillas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(nuevaZapatilla)
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
        cargarZapatillas();
    })
    .catch(error => {
        console.error('Error:', error);
    });

    document.getElementById('nombre').value = '';
    document.getElementById('marca_id').value = '';
    document.getElementById('talla').value = '';
    document.getElementById('precio').value = '';
    document.getElementById('categoria_id').value = '';
});


function eliminarZapatilla() {
    const zapatillaId = document.getElementById('eliminar-zapatilla-id').value;

    if (zapatillaId) {
        if (confirm(`¿Estás seguro de que deseas eliminar la zapatilla con ID ${zapatillaId}?`)) {
          
            fetch(`http://127.0.0.1:5000/zapatillas/${zapatillaId}`, {
                method: 'DELETE'
            })
            .then(response => response.text())
            .then(data => {
                alert(data);
                cargarZapatillas();
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    } else {
        alert('Por favor, ingresa un ID de zapatilla válido.');
    }
}

document.getElementById('eliminar-zapatilla-form').addEventListener('submit', function (e) {
    e.preventDefault();
    eliminarZapatilla();
});
cargarZapatillas();  
