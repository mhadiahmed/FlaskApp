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