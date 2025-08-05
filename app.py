from flask import Flask, render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from crud import register_all_cruds

app = Flask(__name__)

# Cargar configuración desde config.py
app.config.from_pyfile('config.py')

# Configuración de la conexión MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# El usuario y password ahora se leen desde config.py
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'warnes'
app.config['MYSQL_CURSORCLASS'] = DictCursor

# Inicializar MySQL
mysql = MySQL()
mysql.init_app(app)


# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')


# Registrar todos los CRUDs
register_all_cruds(app, mysql)

#  Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)  # ,host='0.0.0.0'
