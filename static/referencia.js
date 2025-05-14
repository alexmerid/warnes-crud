// Editar referencia
function editReferencia(id, distrito, descripcion) {
    document.getElementById('edit_id').value = id;
    document.getElementById('edit_distrito').value = distrito;
    document.getElementById('edit_descripcion').value = descripcion;
}

// Validar formularios
document.addEventListener('DOMContentLoaded', function () {
    const addForm = document.querySelector('#addModal form');
    const editForm = document.querySelector('#editModal form');
    const addErrorDiv = document.getElementById('addError');
    const editErrorDiv = document.getElementById('editError');


    if (addForm) {
        addForm.addEventListener('submit', function (e) {
            const id = addForm.querySelector('input[name="id"]').value;
            const distrito = addForm.querySelector('input[name="distrito"]').value.trim();
            const descripcion = addForm.querySelector('input[name="descripcion"]').value.trim();

            let error = '';
            if (!/^\d+$/.test(id) || parseInt(id) < 0) {
                error = "El ID debe ser mayor o igual a 0.";
            } else if (distrito !== '' && (!/^\d+$/.test(distrito) || parseInt(distrito) <= 0)) {
                error = "El Distrito debe estar vacío o ser un número mayor a cero.";
            } else if (descripcion === '') {
                error = "La Descripción no puede estar vacía.";
            }

            if (error) {
                e.preventDefault();
                addErrorDiv.textContent = error;
                addErrorDiv.classList.remove('d-none');
            } else {
                addErrorDiv.classList.add('d-none');
            }
        });
    }

    if (editForm) {
        editForm.addEventListener('submit', function (e) {
            const distrito = editForm.querySelector('input[name="distrito"]').value.trim();
            const descripcion = editForm.querySelector('input[name="descripcion"]').value.trim();

            let error = '';
            if (distrito !== '' && (!/^\d+$/.test(distrito) || parseInt(distrito) <= 0)) {
                error = "El Distrito debe estar vacío o ser un número mayor a cero.";
            } else if (descripcion === '') {
                error = "La Descripción no puede estar vacía.";
            }

            if (error) {
                e.preventDefault();
                editErrorDiv.textContent = error;
                editErrorDiv.classList.remove('d-none');
            } else {
                editErrorDiv.classList.add('d-none');
            }
        });
    }
});