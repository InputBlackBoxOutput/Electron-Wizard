from flask import Flask, render_template, url_for
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


# Not working : Not getting access to form data !!!!!!!!
@app.route("/ex", methods=['GET', 'POST'])
def ex():
    form = R()
    if form.validate_on_submit():
    	result = form.r.data
    	return render_template('ex.html',result=result)
    return render_template('ex.html', form=form)

if __name__ == '__main__':
	app.run(debug =True)

	 
