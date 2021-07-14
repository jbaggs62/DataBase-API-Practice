from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_DB'] = 'vaccineDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)