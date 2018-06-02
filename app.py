from flask import Flask,render_template,request,session,url_for,redirect,logging,flash
from DB import Articale
from forms import RigesterForm,Add_Articale_form
from db.DataBase import connection
from db.DataAPI import (
	add_user,
	check_user,
	Add_Articale,
	show_articale,
	get_by_id,
	update,
	delete
)
from passlib.hash import sha256_crypt
from functools import wraps

# Articales = Articale()

app = Flask(__name__)

#**************************************************
# Permissions
#**************************************************
def is_admin(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'is_admin' in session:
			return f(*args,**kwargs)
		else:
			return redirect(url_for('home'))
	return wrap



#**************************************************
#Dashboard Pages
#**************************************************
@app.route('/dashboard')
@is_admin
def dashboard():
	return render_template('dashboard.html')


#**************************************************
#Home Pages
#**************************************************
@app.route('/')
def home():
	projectName = "FlaskApp"
	return render_template("home.html",projectName=projectName)


@app.route('/about')
def about():
	projectName = "Test Function"
	return render_template("about.html",projectName=projectName)




#**************************************************
#Articales Pages
# create , edit, deatil , delete
#**************************************************
@app.route('/articale')
def Areticales():
	query,data = show_articale()

	if query > 0:
		Articales = data
		return render_template("articales.html",Articales=Articales)
	else:
		msg = "no data yet .."
		return render_template("articales.html",msg=msg)


@app.route('/create',methods=['GET','POST'])
def Articale_create():
	btnName = "Create"
	form  = Add_Articale_form(request.form)
	if request.method == "POST" and form.validate():
		title = form.title.data 
		content = form.content.data 
		user = session['username']
		Add_Articale(title,user,content)
		flash("Articale is saved..","success")
		return redirect(url_for('Areticales'))
	return render_template('create_articale.html',form=form,btnName=btnName)


@app.route('/edit/<string:id>',methods=['GET','POST'])
def Articale_edit(id):
	btnName = "Edit"
	form  = Add_Articale_form(request.form)
	query ,data = get_by_id(id)
	form.title.data = data['title']
	form.content.data = data['content']

	if request.method == "POST" and form.validate():
		title = request.form['title']
		content = request.form['content']
		update(id,title,content)
		flash("Articale is updated..","success")
		return redirect(url_for('Areticales'))
	return render_template('create_articale.html',form=form,btnName=btnName)


@app.route('/artical/<string:id>')
def Areticale_deatil(id):
	query ,data = get_by_id(id)
	if query > 0:
		artd = data
		return render_template("articale_deatil.html",artd=artd)
	else:
		msg = "no articale with this id."
		return render_template("articale_deatil.html",msg=msg)
	

@app.route('/delete/<string:id>')
def Areticale_delete(id):
	query,data = get_by_id(id)
	username = session['username']
	if data['author'] in username:
		delete(id,username)
		flash("Articale is deleted..","success")
		return redirect(url_for('Areticales'))
	else:
		flash("You don't have permission to do this..","info")
		return redirect(url_for('Areticales'))




#**************************************************
#Users Page
#	Register , Login , logout
#**************************************************

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
				admin = data['admin']
				if admin == 1:
					session['is_admin'] = True

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
	flash("See you Later soon..","info")
	return redirect(url_for("login"))




#**************************************************
#Run the server in local
#**************************************************
if __name__ == "__main__":
	app.secret_key = "@%^&(*9867ahsh"
	app.run(debug=True)