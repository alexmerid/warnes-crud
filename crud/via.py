def init_via_routes(app, mysql):
    from flask import render_template, request, redirect, url_for

    # Crud Via
    @app.route('/via')
    def crud_via():
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM via")
        vias = cursor.fetchall()
        cursor.close()
        return render_template('via.html', vias=vias)

    # Agregar Via
    @app.route('/via/agregar', methods=['POST'])
    def agregar_via():
        id_via = request.form['id']
        descripcion = request.form['descripcion']
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO via (id, descripcion) VALUES (%s, %s)",
                       (id_via, descripcion))
        conn.commit()
        cursor.close()
        return redirect(url_for('crud_via'))

    # Eliminar Via
    @app.route('/via/borrar/<int:id_via>')
    def borrar_via(id_via):
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM via WHERE id = %s", (id_via,))
        conn.commit()
        cursor.close()
        return redirect(url_for('crud_via'))

    # Editar Via
    @app.route('/via/editar', methods=['POST'])
    def editar_via():
        id_via = request.form['id']
        descripcion = request.form['descripcion']
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE via SET descripcion = %s WHERE id = %s",
                       (descripcion, id_via))
        conn.commit()
        cursor.close()
        return redirect(url_for('crud_via'))
