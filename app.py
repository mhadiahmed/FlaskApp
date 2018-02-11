from flask import Flask,render_template
from DB import Articale
from forms import RegisterForm

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

if __name__ == "__main__":
    app.run(debug=True)
        
