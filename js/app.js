//url de la API
const url = "http://127.0.0.1:8000/movimientos"

function showForm(){
    document.getElementById("div-form").style.display = "block"
}

function ocultarFormulario(){
    document.getElementById("div-form").style.display = "none"
}

function limpiarFormulario(){
    document.getElementById('id_campo').value = '';
    document.getElementById('concept').value = '';
    document.getElementById('quantity').value = '';
    document.getElementById('fecha').value = ''; 
}


let nuevo = document.getElementById("btnNuevo")
//Se puede hacer con onclick pero se recomienda evitar código js en html
//Para que funcione, hay que pasar la función commo parámetro SIN PARÉNTESIS
nuevo.addEventListener("click", showForm)

let cerrar = document.getElementById("btnCerrar")

cerrar.addEventListener("click", ocultarFormulario)

function mostrarMovimientos(){

    //Seleccionamos el cuerpo de la tabla
    const tbody = document.getElementById('cuerpo-tabla')
    //Petición http GET usando FetchAPI
    fetch(url)
    .then(response => response.json())
    .then(data =>{
        let filas = ''; //Variable para acumular filas de las tablas en html
        data.forEach(element => {
            filas += `             
                <tr>
                    <td>${element.id}</td>
                    <td>${element.concept}</td>
                    <td>${element.quantity}</td>
                    <td>${element.date}</td>
                </tr>`
            
        });

        //Insertar la fila cargada dentro de la tabla
        tbody.innerHTML = filas;
    }).catch(error=> console.log("Error al cargar los datos: ", error))

}

mostrarMovimientos();

function capturarItemLista(){
    //accedo a la tabla completa
    const tabla = document.getElementById('tabla');
    for (let i = 0; i < tabla.rows.length; i++){
        //acceso a recorrido del contenido de tabla por posición con función onclick
        //rows es una propiedad de la etiqueta table, que a su vez, tiene la propiedad onclick
        //onclick es un método que se puede asociar a cualquier elemento
        tabla.rows[i].onclick = function(){
            let id = this.cells[0].innerHTML;
            let concept = this.cells[1].innerHTML;
            let quantity = this.cells[2].innerHTML;
            let date = this.cells[3].innerHTML;
            showForm();
            //cargar dato capturado de fila en los input del formulario
            document.getElementById('id_campo').value = id;
            document.getElementById('concept').value = concept;
            document.getElementById('quantity').value = quantity;
            document.getElementById('fecha').value = date;  
        }
    }
}

let tabla = document.getElementById('tabla');
tabla.addEventListener('click', capturarItemLista);

function borrarMovimiento(){
    let id_value = document.getElementById('id_campo').value
    fetch(`${url}/${id_value}`, {
        method: 'DELETE'
    }).then(response=>{
        if(!response.ok){
            //Si es distinto de 200, que lance una excepción en la consola
            throw new Error(`Error HTTP: ${response.status}`)
        }
        //Que muestre la tabla sin el elemento eliminado
        mostrarMovimientos();

        alert('Registro eliminado correctamente.')

        limpiarFormulario();
        ocultarFormulario();
    }).catch(
        error=>{
            alert('No se ha podido eliminar el movimiento')
            console.log('Detalle error: ', error)
        }
    )
}

function confirmarBorrado(){
    confirmacion = confirm("Estas seguro/a que deseas eliminar el registro");
    if (confirmacion){
        borrarMovimiento();
    }else{
        alert("Operación cancelada.");
    }
}

let borrar = document.getElementById('btnBorrar')
borrar.addEventListener('click', confirmarBorrado)

function actualizarMovimiento(){
    //capturar los datos ingresados en los input
    const date = document.getElementById('fecha').value
    const concept = document.getElementById('concept').value
    const quantity = document.getElementById('quantity').value

    if(concept === ''){
        alert('Debes agregar un concepto');
        return;
    }

    if(quantity == 0 || quantity === ''){
        alert('Debes agregar una cantidad');
        return;
    }
//formato ede aaaa-mm-dd para comparar con la fecha ingresada
    const hoy = new Date().toISOString().split('T')[0];

    if(!date || date > hoy){
        alert('La fecha introducida no es válida');
        return;
    }
    let id_value = document.getElementById('id_campo').value
    if (id_value === ''){
        alert('Debes seleccionar un registro')
        return;
    }

    fetch(`${url}/${id_value}`, {
        method: 'PUT', 
        headers: {
            //Informamos el tipo de dato
            'Content-Type':'application/json'
        },
        body: JSON.stringify(
            {
                date:date,
                concept:concept,
                quantity:Number(quantity)
            }
        )
    }).then(response=>{
                alert("HA LLEGADO LA RESPUESTA DEL PUT");
        if(!response.ok){
            throw new Error(`Error HTTP: ${response.status}`)
        }

        mostrarMovimientos();
        alert('Registro actualizado correctamente.')
    
        //limpiar campos del formulario
        limpiarFormulario();
        ocultarFormulario()
    }).catch(
        error=>{
            alert('No se ha podido actualizar el movimiento')
            console.log('Detalle error: ', error)
        }
    ) 
}

let actualizar = document.getElementById('btnEditar')
actualizar.addEventListener('click', actualizarMovimiento)
