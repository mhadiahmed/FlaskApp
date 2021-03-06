from db.DataBase import connection
from pymysql import escape_string as clean
from passlib.hash import sha256_crypt
# use passlib or hashlib
# global variable

# conn,db = connection()

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

def update_user(name,username,email,id):
	# get data & clean it 
	
	c_name = clean(name)
	c_username = clean(username)
	c_email = clean(email) 
	c_id = clean(id)

	# create connection

	conn,db = connection()

	# execute query

	query = db.execute("UPDATE users SET name=%s,username=%s,email=%s WHERE id = %s",(c_name,c_username,c_email,c_id))
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

	query = db.execute('SELECT * FROM articale WHERE approve=1 ORDER BY id DESC')

	data = db.fetchall()

	return query,data


def show_unapproved_articale():
	conn,db = connection()

	query = db.execute('SELECT * FROM articale WHERE approve=0 ORDER BY id DESC')

	data = db.fetchall()

	return query,data


def show_users():
	conn,db = connection()

	query = db.execute('SELECT * FROM users ')

	data = db.fetchall()

	return query,data


def get_latest_users():
	conn,db = connection()

	query = db.execute('SELECT * FROM users ORDER BY id DESC LIMIT 3')

	data = db.fetchall()

	return query,data

def get_latest_articale():
	conn,db = connection()

	query = db.execute('SELECT * FROM articale WHERE approve=0 ORDER BY id DESC LIMIT 3')

	data = db.fetchall()

	return query,data

def get_usersby_id(id):
	c_id = clean(id)
	conn,db = connection()

	query = db.execute('SELECT * FROM users WHERE id=%s',[c_id])

	data = db.fetchone()

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


def delete(id,username):
	c_id = clean(id)
	c_username = clean(username)
	conn,db = connection()

	query = db.execute('DELETE FROM articale WHERE id = %s AND author = %s',(c_id,c_username))

	conn.commit()

	db.close


def delete_user(id):
	c_id = clean(id)
	conn,db = connection()

	query = db.execute('DELETE FROM users WHERE id = %s',(c_id))

	conn.commit()

	db.close


def admin_delete(id):
	c_id = clean(id)
	conn,db = connection()

	query = db.execute('DELETE FROM articale WHERE id = %s ',[c_id])

	conn.commit()

	db.close


def approve(id):
	c_id = clean(id)
	conn,db = connection()

	query = db.execute('UPDATE articale SET approve=1 WHERE id = %s',[c_id])

	conn.commit()

	db.close