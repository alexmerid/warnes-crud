def init_censista_routes(app, mysql):
    from flask import render_template, request, redirect, url_for

    # Crud Censista
    @app.route('/censista')
    def crud_censista():
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM censista")
        censistas = cursor.fetchall()
        cursor.close()
        return render_template('censista.html', censistas=censistas)

    # Agregar Censista
    @app.route('/censista/agregar', methods=['POST'])
    def agregar_censista():
        id_cen = request.form['id']
        nombre = request.form['nombre']
        nombre = nombre if nombre else None
        usuario = request.form['usuario']
        passw = request.form['pass']
        passw = passw if passw else None
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO censista (id, nombre, usuario, pass) VALUES (%s, %s, %s, %s)",
                       (id_cen, nombre, usuario, passw))
        conn.commit()
        cursor.close()
        return redirect(url_for('crud_censista'))

    # Eliminar Censista
    @app.route('/censista/borrar/<int:id_cen>')
    def borrar_censista(id_cen):
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM censista WHERE id = %s", (id_cen,))
        conn.commit()
        cursor.close()
        return redirect(url_for('crud_censista'))

    # Editar Censista
    @app.route('/censista/editar', methods=['POST'])
    def editar_censista():
        id_cen = request.form['id']
        nombre = request.form['nombre']
        nombre = nombre if nombre else None
        usuario = request.form['usuario']
        passw = request.form['pass']
        passw = passw if passw else None
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE censista SET nombre = %s, usuario = %s, pass= %s WHERE id = %s",
                       (nombre, usuario, passw, id_cen))
        conn.commit()
        cursor.close()
        return redirect(url_for('crud_censista'))
