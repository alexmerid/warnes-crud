// Editar luminaria
function editLuminaria(id, tipo, potencia) {
    document.getElementById('edit_id').value = id;
    document.getElementById('edit_tipo').value = tipo;
    document.getElementById('edit_potencia').value = potencia;
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
            const tipo = addForm.querySelector('input[name="tipo"]').value.trim();
            const potencia = addForm.querySelector('input[name="potencia"]').value.trim();

            let error = '';
            if (!/^\d+$/.test(id) || parseInt(id) < 0) {
                error = "El ID debe ser mayor o igual a 0.";
            } else if (tipo === '') {
                error = "El campo 'Tipo' no puede estar vacío.";
            } else if (potencia !== '' && (!/^\d+$/.test(potencia) || parseInt(potencia) <= 0)) {
                error = "La potencia debe estar vacía o ser un número mayor a cero.";
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
            const tipo = editForm.querySelector('input[name="tipo"]').value.trim();
            const potencia = editForm.querySelector('input[name="potencia"]').value.trim();

            let error = '';
            if (tipo === '') {
                error = "El campo 'Tipo' no puede estar vacío.";
            } else if (potencia !== '' && (!/^\d+$/.test(potencia) || parseInt(potencia) <= 0)) {
                error = "La Potencia debe estar vacía o ser un número mayor a cero.";
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