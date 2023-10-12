
      function cargarZapatillas() {
        $.get('/zapatillas', function (data) {
            const zapatillaList = $('#zapatilla-list');
            zapatillaList.empty(); 

            data.forEach(function (zapatilla) {
                const listItem = $('<li></li>');
                listItem.text(`Nombre: ${zapatilla.nombre}, Marca: ${zapatilla.marca}, Talla: ${zapatilla.talla}, Precio: ${zapatilla.precio}, Categoría: ${zapatilla.categoria}`);
                zapatillaList.append(listItem);
            });
        });
    }

   
    $('#crear-zapatilla-form').submit(function (e) {
        e.preventDefault();

        const nombre = $('#nombre').val();
        const marcaId = parseInt($('#marca_id').val());
        const talla = parseFloat($('#talla').val());
        const precio = parseFloat($('#precio').val());
        const categoriaId = parseInt($('#categoria_id').val());

        const nuevaZapatilla = {
            nombre: nombre,
            marca_id: marcaId,
            talla: talla,
            precio: precio,
            categoria_id: categoriaId
        };

        $.post('/zapatillas', JSON.stringify(nuevaZapatilla), function (data) {
            alert(data);
            cargarZapatillas(); 
        });

      
        $('#nombre').val('');
        $('#marca_id').val('');
        $('#talla').val('');
        $('#precio').val('');
        $('#categoria_id').val('');
    });

 
    cargarZapatillas();