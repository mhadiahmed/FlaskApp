from flask import Flask,render_template,request,session,url_for,redirect,logging,flash
from DB import Articale
from forms import RigesterForm
from db.DataBase import connection
from db.DataAPI import add_user,check_user
from passlib.hash import sha256_crypt


Articales = Articale()

app = Flask(__name__)



@app.route('/')
def home():
	projectName = "FlaskApp"
	return render_template("home.html",projectName=projectName)


@app.route('/about')
def about():
	projectName = "Test Function"
	return render_template("about.html",projectName=projectName)



@app.route('/articale')
def Areticales():
	return render_template("articales.html",Articales=Articales)


@app.route('/artical/<string:id>')
def Areticale_deatil(id):
	return render_template("articale_deatil.html",id=id)


@app.route('/register',methods=['GET','POST'])
def Register():		
	form = RigesterForm(request.form)
	if request.method == "POST" and form.validate():
		# get data from the form
		name = form.name.data
		username = form.username.data
		email = form.email.data
		password = form.password.data
		# save in data base
		add_user(name,username,email,password)
		session['username'] = username
		session['logged_in'] = True
		flash("Welcome {}".format(username),"success")
		return redirect(url_for("home"))
	return render_template("register.html",form=form)


@app.route('/login',methods=['GET','POST'])
def login():
	# ceck method if it post
	if request.method == "POST":
		# get data from the form
		username = request.form['username']
		password = request.form['password']
		# call our function
		query,data = check_user(username)
		# check query
		if query > 0:
			_password = data['password']
			if sha256_crypt.verify(password,_password):
				session['username'] = username
				session['logged_in'] = True
				flash("Welcome {}".format(username),"success")
				return redirect(url_for('home'))
			else:
				error = "Password or user not Match."
				return render_template('login.html',error=error)
		else:
			error = "Password or user not Match."
			return render_template('login.html',error=error)
	return render_template('login.html')


@app.route('/logout',methods=['GET','POST'])
def logout():
	session.clear()
	flash("See you Later soon..","warning")
	return redirect(url_for("login"))

if __name__ == "__main__":
	app.secret_key = "@%^&(*9867ahsh"
	app.run(debug=True)
        
