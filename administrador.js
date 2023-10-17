function cargarZapatillas() {
    fetch('http://127.0.0.1:5000/zapatillas')
        .then(response => response.json())
        .then(data => {
            const zapatillaList = document.getElementById('zapatilla-list');
            zapatillaList.innerHTML = '';  // Limpiar la lista

            data.forEach(zapatilla => {
                const listItem = document.createElement('li');
                listItem.textContent = `Nombre: ${zapatilla.nombre}, Marca: ${zapatilla.marca}, Talla: ${zapatilla.talla}, Precio: ${zapatilla.precio}, Categoría: ${zapatilla.categoria}`;
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

cargarZapatillas();  // Cargar la lista inicial
