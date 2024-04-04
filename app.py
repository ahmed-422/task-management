from flask import Flask, render_template, request, redirect, url_for,session
from flaskext.mysql import MySQL

app = Flask(__name__,static_folder="assets")
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'taskmgnt'

mysql = MySQL()
mysql.init_app(app)
cursor = mysql.get_db().cursor()

@app.route('/')
def index():
    return render_template('index.html' )


if __name__ == '__main__':
    app.run(debug=True)
