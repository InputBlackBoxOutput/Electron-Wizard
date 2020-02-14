# Electron Wizard webapp
#
# @file  : app.py
# @brief : Provides entry-point and framework 
# @author: Rutuparn Pawar (InputBlackBoxOutput)
# @date_created : 7 Feb, 2020

try:
    from flask import Flask, render_template, url_for, flash, request, redirect
    import forms
    import compute
except ImportError:
    print('Error occured while importing modules required by app.py')

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

# Use to redirect to above page in case of error (Not used)
# if form.error:
#     print('Error Occured')
#     return redirect(url_for('error'))


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
        result = compute.ohmsLaw(form.R.data, form.V.data, form.I.data)
        return render_template('Ohms_Law.html', form=form, result=result)
    else:
        return render_template('Ohms_Law.html', form=form)


@app.route("/Resistor_Series_Parallel", methods=['GET', 'POST'])
def Resistor_Series_Parallel():
    form = forms.R_Comb()
    
    if form.validate_on_submit():
        result = compute.resCombntion(form.sp.data, form.Rone.data, form.Rtwo.data)
        # result = form.sp.data + str(form.Rone.data) + str(form.Rtwo.data)
        return render_template('Resistor_Series_Parallel.html', form=form, result=result)
    else:
        return render_template('Resistor_Series_Parallel.html', form=form)

@app.route("/Resistor_Colour_Code", methods=['GET', 'POST'])
def Resistor_Colour_Code():
    form = forms.R()
    
    if form.validate_on_submit():
        result = compute.resClrCode(form.nbands.data, form.colour1.data, form.colour2.data, form.colour3.data, form.colour4.data, form.colour5.data)
        # result = form.nbands.data+form.colour1.data + form.colour2.data + form.colour3.data + form.colour4.data + form.colour5.data
        return render_template('Resistor_Colour_Code.html', form=form, result=result)
    else:
        return render_template('Resistor_Colour_Code.html', form=form)


@app.route("/SMD_Code", methods=['GET', 'POST'])
def SMD_Code():
    form = forms.SMD()

    if form.validate_on_submit():
        result = compute.valSMD(form.code.data, form.compnt.data)
        return render_template('SMD_Code.html', form=form, result=result)
    else:
        return render_template('SMD_Code.html', form=form)

#------------------------------------------------------------------------------------------
if __name__ == '__main__':
	app.run(debug =True)
 
