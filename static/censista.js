// Editar censista
function editCensista(id, nombre, usuario, pass) {
    document.getElementById('edit_id').value = id;
    document.getElementById('edit_nombre').value = nombre;
    document.getElementById('edit_usuario').value = usuario;
    document.getElementById('edit_pass').value = pass;
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
            const usuario = addForm.querySelector('input[name="usuario"]').value.trim();

            let error = '';
            if (!/^\d+$/.test(id) || parseInt(id) < 0) {
                error = "El ID debe ser mayor o igual a 0.";
            } else if (usuario === '') {
                error = "El Usuario no puede estar vacío.";
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
            const usuario = editForm.querySelector('input[name="usuario"]').value.trim();

            let error = '';
            if (usuario === '') {
                error = "El Usuario no puede estar vacío.";
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