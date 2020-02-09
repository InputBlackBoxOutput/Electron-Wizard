from flask import Flask,render_template
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '4d12bc03c6bdcc7a945a55d1316490fa'

#Home Page
@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", title="Home") 

#About Page
@app.route("/about")
def about():
	return render_template("about.html", title="About")

#Series/parallel equivalent resistor calculator
@app.route("/SrlPrllRes", method=['GET','POST'])
def calculator_one():
	form = SrlPrllRes()
	return render_template("about.html", title='Calculator', form=form)

if __name__ == '__main__':
	app.run(debug =True)

	 
