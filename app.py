from flask import Flask,render_template,request,session,url_for,redirect,logging
from DB import Articale
from forms import RigesterForm
from db.DataBase import connection
from db.DataAPI import add_user
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
		return redirect(url_for("home"))
	return render_template("register.html",form=form)

if __name__ == "__main__":
	app.run(debug=True)
        
