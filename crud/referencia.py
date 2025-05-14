def init_referencia_routes(app, mysql):
    from flask import render_template, request, redirect, url_for

    # Crud Referencia
    @app.route('/referencia')
    def crud_referencia():
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM referencia")
        referencias = cursor.fetchall()
        cursor.close()
        return render_template('referencia.html', referencias=referencias)

    # Agregar Referencia
    @app.route('/referencia/agregar', methods=['POST'])
    def agregar_referencia():
        id_ref = request.form['id']
        distrito = request.form['distrito']
        distrito = int(distrito) if distrito else None
        descripcion = request.form['descripcion']
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO referencia (id, distrito, descripcion) VALUES (%s, %s,%s)",
                       (id_ref, distrito, descripcion))
        conn.commit()
        cursor.close()
        return redirect(url_for('crud_referencia'))

    # Eliminar Referencia
    @app.route('/referencia/borrar/<int:id_ref>')
    def borrar_referencia(id_ref):
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM referencia WHERE id = %s", (id_ref,))
        conn.commit()
        cursor.close()
        return redirect(url_for('crud_referencia'))

    # Editar Referencia
    @app.route('/referencia/editar', methods=['POST'])
    def editar_referencia():
        id_ref = request.form['id']
        distrito = request.form['distrito']
        distrito = int(distrito) if distrito else None
        descripcion = request.form['descripcion']
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE referencia SET distrito = %s, descripcion = %s WHERE id = %s",
                       (distrito, descripcion, id_ref))
        conn.commit()
        cursor.close()
        return redirect(url_for('crud_referencia'))
