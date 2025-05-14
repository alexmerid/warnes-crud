def init_luminaria_routes(app, mysql):
    from flask import render_template, request, redirect, url_for

    # Crud Luminaria
    @app.route('/luminaria')
    def crud_luminaria():
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM luminaria")
        luminarias = cursor.fetchall()
        cursor.close()
        return render_template('luminaria.html', luminarias=luminarias)

    # Agregar Luminaria
    @app.route('/luminaria/agregar', methods=['POST'])
    def agregar_luminaria():
        id_lum = request.form['id']
        tipo = request.form['tipo']
        potencia = request.form['potencia']
        potencia = int(potencia) if potencia else None
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO luminaria (id, tipo, potencia) VALUES (%s, %s,%s)", (id_lum, tipo, potencia))
        conn.commit()
        cursor.close()
        return redirect(url_for('crud_luminaria'))

    # Eliminar luminaria
    @app.route('/luminaria/borrar/<int:id>')
    def borrar_luminaria(id):
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM luminaria WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        return redirect(url_for('crud_luminaria'))

    # Editar luminaria
    @app.route('/luminaria/editar', methods=['POST'])
    def editar_luminaria():
        id_lum = request.form['id']
        tipo = request.form['tipo']
        potencia = request.form['potencia']
        potencia = int(potencia) if potencia else None
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE luminaria SET tipo = %s, potencia = %s WHERE id = %s", (tipo, potencia, id_lum))
        conn.commit()
        cursor.close()
        return redirect(url_for('crud_luminaria'))
