from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
# el puerto debe ser int en lugar de string
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'blog'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM entrada")
    posts = cursor.fetchall()
    cursor.close()

    print(posts)

    return render_template('index.html', entradas=posts)


@app.route('/entrada/<int:id>')
def entrada(id):
    
    return render_template('entrada.html', entrada=id)
    
    
app.run()