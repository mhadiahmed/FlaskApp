import pymysql

def connection():
	try:
		conn = pymysql.connect(
			host="localhost",
			user="root",
			password="",
			db="flask_crud",
			cursorclass=pymysql.cursors.DictCursor
			)
		db = conn.cursor()
		return conn,db
	except:
		msg = "connection error."

		return msg