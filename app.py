# Electron Wizard webapp
from flask import Flask, render_template, url_for, flash, request, redirect
import forms
# import compute

app = Flask(__name__)
app.config.from_object(__name__)
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


@app.route("/ex", methods=['GET', 'POST'])
def ex():
    form = forms.R_Comb()
    
    if form.validate_on_submit():
        result = int(form.Rone.data) + int(form.Rtwo.data)
        return render_template('ex.html', form=form, result=result)
    else:
        return render_template('ex.html', form=form)

    if form.error:
        print('Error Occured')
        return redirect(url_for('error'))

@app.route('/error')
def error():
    return render_template('error.html',title='Error Occured')    

@app.route('/fun')
def fun():
    return redirect('https://dino-chrome.com') 

if __name__ == '__main__':
	app.run(debug =True)
 
