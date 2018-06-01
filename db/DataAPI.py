from db.DataBase import connection
from pymysql import escape_string as clean
from passlib.hash import sha256_crypt
# use passlib or hashlib

def add_user(name,username,email,password):
	# get data & clean it 
	
	c_name = clean(name)
	c_username = clean(username)
	c_email = clean(email) 
	c_password = sha256_crypt.encrypt(clean(password))

	# create connection

	conn,db = connection()

	# execute query

	query = db.execute("INSERT INTO users (name,username,email,password,admin) VALUES (%s,%s,%s,%s,0)",(c_name,c_username,c_email,c_password))
	# save change
	conn.commit()
	# close connection
	db.close()



def check_user(username):
	c_username = clean(username)
	# create connection
	conn,db = connection()

	# execute query

	query = db.execute('SELECT * FROM users WHERE username = %s',[c_username])

	#fetch data

	data = db.fetchone()

	return query,data

def Add_Articale(title,user,content):
	c_title = clean(title)
	c_content = clean(content)

	conn,db = connection()

	query = db.execute('INSERT INTO articale (title,author,content,approve) VALUES (%s,%s,%s,0)',(c_title,user,c_content))

	conn.commit()

	db.close()

def show_articale():
	conn,db = connection()

	query = db.execute('SELECT * FROM articale WHERE approve=0 ORDER BY id DESC')

	data = db.fetchall()

	return query,data


def get_by_id(id):
	c_id = clean(id)
	conn,db = connection()

	query = db.execute('SELECT * FROM articale WHERE id=%s',[c_id])

	data = db.fetchone()

	return query,data


def update(id,title,content):
	c_id = clean(id)
	c_title = clean(title)
	c_content = clean(content)
	conn,db = connection()

	query = db.execute('UPDATE articale SET title=%s, content = %s WHERE id = %s',(c_title,c_content,c_id))

	conn.commit()

	db.close
