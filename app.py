# Electron Wizard webapp
from flask import Flask, render_template, url_for, flash, request, redirect
import forms
# import compute

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '4d12bc03c6bdcc7a945a55d1316490fa'

#------------------------------------------------------------------------------------------
# Basic routes

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", title="Home") 


@app.route("/about")
def about():
	return render_template("about.html", title="About")

# Error Page
@app.route('/error')
def error():
    return render_template('error.html',title='Error Occured')    

# 
@app.route('/fun')
def fun():
    return redirect('https://dino-chrome.com') 

#------------------------------------------------------------------------------------------
# Calculator routes

@app.route("/Ohms_Law", methods=['GET', 'POST'])
def Ohms_Law():
    form = forms.Ohm()
    
    if form.validate_on_submit():
        result = form.R.data
        return render_template('Ohms_Law.html', form=form, result=result)
    else:
        return render_template('Ohms_Law.html', form=form)

    if form.error:
        print('Error Occured')
        return redirect(url_for('error'))


@app.route("/Resistor_Series_Parallel", methods=['GET', 'POST'])
def Resistor_Series_Parallel():
    form = forms.R_Comb()
    
    if form.validate_on_submit():
        result = form.Rone.data + form.Rtwo.data
        return render_template('Resistor_Series_Parallel.html', form=form, result=result)
    else:
        return render_template('Resistor_Series_Parallel.html', form=form)

    if form.error:
        print('Error Occured')
        return redirect(url_for('error'))

@app.route("/Resistor_Colour_Code", methods=['GET', 'POST'])
def Resistor_Colour_Code():
    return render_template('Resistor_Colour_Code.html')
    # form = forms.R()
    
    # if form.validate_on_submit():
    #     result = 'In development'
    #     return render_template('Resistor_Colour_Code.html', form=form, result=result)
    # else:
    #     return render_template('Resistor_Colour_Code.html', form=form)

    # if form.error:
    #     print('Error Occured')
    #     return redirect(url_for('error'))


@app.route("/SMD_Code", methods=['GET', 'POST'])
def SMD_Code():
    return render_template('SMD_Code.html')
    # form = forms.SMD()
    
    # if form.validate_on_submit():
    #     result = 'In development'
    #     return render_template('SMD_Code.html', form=form, result=result)
    # else:
    #     return render_template('SMD_Code.html', form=form)

    # if form.error:
    #     print('Error Occured')
    #     return redirect(url_for('error'))

#------------------------------------------------------------------------------------------
if __name__ == '__main__':
	app.run(debug =True)
 
