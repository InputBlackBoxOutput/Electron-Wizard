# Electron Wizard webapp 
# 
# @file  : compute.py
# @brief : Provides computation
# @author: Rutuparn Pawar (InputBlackBoxOutput)
# @date_created : 21 August, 2019
#

# 0
# Funtion on Ohms Law V=IR
def ohmsLaw(R,V,I):    
    if R and V  and I:
        return 'All parameters specified! No parameter to be calculated.'

    if not R and not V and not I:
        return 'Please specify atleast 2 parameters.'

    if not V and not I:
        return 'Specify voltage or current'
    if not R and not I:
        return 'Specify resistance or current'
    if not R and not V :
        return 'Specify resistance or voltage'

    if R:
        if V:
            return f"Current = {prefixPostProcess(V/R)}A "
        if I:
            return f"Voltage = {prefixPostProcess(I*R)}V "
    else:
    	return f"Resistance = {prefixPostProcess(V/I)}ohm" 	

# 1
# Function to calculate equivalent resistance of 2 resistors in series or parallel
def resCombntion(parallel,R1,R2):
    if parallel == 'P':
        return f'Equivalent Resistance {prefixPostProcess(((R1*R2)/(R1+R2)))} ohm'
    else:
        return f'Equivalent Resistance = {prefixPostProcess(R1+R2)} ohm'

# 2
# Funtion to calculate resistance of a resistor using colour code
# Improve by adding resistor series feature
def resClrCode(nbands,Band1,Band2,Band3,Band4,Band5):
    digit = {'Black':0,'Brown':1,'Red':2,'Orange':3,'Yellow':4,'Green':5,'Blue':6,'Violet':7,'Grey':8,'White':9}
    multiplier = {'Black':0,'Brown':1,'Red':2,'Orange':3,'Yellow':4,'Green':5,'Blue':6,'Violet':7,'Grey':8,'White':9,'Gold':0.1,'Silver':0.01}
    tolerance = {'Brown':1,'Red':2,'Green':0.5,'Blue':0.25,'Violet':0.1,'Grey':0.05,'Gold':5,'Silver':10}
   
    try:
        if nbands == '3':
            R = (digit[Band1] * 10 + digit[Band2]) * (10**multiplier[Band3])
            Tolerance = 20

        elif nbands == '4':
            R = (digit[Band1] * 10 + digit[Band2]) * (10**multiplier[Band3])
            Tolerance = tolerance[Band4]
       
        elif nbands == '5':
            R = (digit[Band1] * 100 + digit[Band2] * 10 + digit[Band3]) * (10**multiplier[Band4])
            Tolerance = tolerance[Band5]
        
        else:
            return 'Error occured while computing!'

        return f"{R} +- {Tolerance}%ohm"
    
    except KeyError:
        return 'No such resistor exits'
    
    except:
        return 'Error occured!'   

# 3-0
# Function to check if marking contains tolerance value
def containsTolerance(marking):
    for char in marking:
        if char.isalpha():
            return True
    return False


# 3
# Funtion to calculate value of a SMD components using markings
def valSMD(mark, compnt, undline):    
    if compnt == 'R':
    	for each in mark:
	    	if each == 'R':
	    		code = mark.split('R')
	    		try:
	    			value = code[0]+'.'+code[1]
	    		except:
	    			value = '0.'+code[1]
	    		return f'{value} ohms'
	    	else:
	    		if undline is True:
	    			return f'0.{mark} ohm'

	    		val =  int(mark) // 10
	    		mult = int(mark) % 10
	    	return f'{prefixPostProcess(val *(10**(mult)))}ohm'

    elif compnt == 'C':
        C_tolerance = {'Z':'+80% & -20%', 'M':'±20%', 'K':'±10%', 'J':'±5%', 'G':'±2%', 'F':'±1%', 'D':'±0.5%', 'C':'±0.25%', 'B':'±0.1%'}

        if containsTolerance(mark):
            try:
                tol = C_tolerance[mark[-1]]
            except:
                return 'Invalid code'

            val  = int(mark[:-1]) // 10
            mult = int(mark[:-1]) % 10
            return f'{prefixPostProcess(val *(10**(mult-12)))}F & Tolerance= {tol}'
        else:           
            val  = int(mark) // 10
            mult = int(mark) % 10
            return f'{prefixPostProcess(val *(10**(mult-12)))}F'    
    
    elif compnt == 'I':
        I_tolerance = {'A':'0.05nH'	, 'B':'0.1nH', 'C':'0.25nH', 'D':'0.5nH', 'E':'0.5%', 'F':'1%', 'G':'2%', 'H':'3%', 'J':'5%', 'K':'10%', 'L':'15%', 'M':'20%', 'V':'25%', 'N':'30%', 'Z':'+80\% & -20\%'}

        if containsTolerance(mark):
            try:
                tol = I_tolerance[mark[-1]]
            except:
                return 'Invalid code'

            val  = int(mark[:-1]) // 10
            mult = int(mark[:-1]) % 10
            return f'{prefixPostProcess(val *(10**(mult-6)))}H & Tolerance= {tol}'
        
        else:
            val  = int(mark) // 10
            mult = int(mark) % 10
            return f'{prefixPostProcess(val *(10**(mult-6)))}H'
    else:
        return 'Something went wrong!'
    

# 4
# Funtion to perform calculations for voltage divider
def voltageDivider(R1,R2,Vin,Vout,Rload=None):

	if not R1 and not R2 and not Vin and not Vout and not Rload:
		return "Please specify parameters"

	if R1 and R2:
		return voltageDividerV(R1,R2,Vin,Vout,Rload)
	elif Vin and Vout:
		return voltageDividerR(Vin,Vout,R1,R2,Rload)
	else:
		return 'Less or wrong parameters entered, please check!'

# 4-1
# Funtion to calculate output voltage for a voltage divider    
def voltageDividerV(R1, R2, Vin, Vout, Rload):
    if Vin is None and Vout is None:
        return 'Specify input or output voltage'

    if Rload is not None and R2 is not None:
        R2 = (R2*Rload)/(R2+Rload)
    
    if Vout is None:
        V=(R2/(R1+R2))*Vin
    else:
        V=((R1+R2)/R2)*Vout

    return f'{prefixPostProcess(V)}V'
    
# 4-2
# Funtion to calculate output voltage for a voltage divider    
def voltageDividerR(Vin, Vout, R1,R2, Rload):
    if R1 is None and R2 is None:
    	return 'Specify value of resistor R1 or R2'
    
    if Vout < Vin :
        V_ratio = Vout/Vin
    else:
        return 'Output voltage cannot be greater than input voltage'
    
    if Rload is not None and R2 is not None:
        R2 = (R2*Rload)/(R2+Rload)
            
    if R2 is None:
            R = (V_ratio/(1-V_ratio))*R1
    else:
            R = ((1-V_ratio)/V_ratio)*R2
        
    return f'{prefixPostProcess(R)}ohm'
    
# 5
# Function to calculate resistance of resitor used as current limiter for Light Emitting Diode (LED)
def currentLimiter(Vsrc, Iled, Clr):
    
    VdropClr={'Red':1.83,'Yellow':2.14, 'Orange':2.06 ,'Blue':3.09, 'Green':2.95, 'Violet':3.38, 'UV':3.75 , 'White':3.4}
    #Note above values are average of max and min Vdrop for each colour
    
    #Since voltage drop varies from 1.8V to 3.3V (average = 2.55V) depending on colour.
    if Clr == 'Ignore colour':
        Vdrop = 2.55
    else:
        Vdrop = VdropClr[Clr]
    
    value = ((float(Vsrc)-Vdrop)/float(Iled))

    if value < 0:
        return 'Please check the values.'
    else:
        return f'Current limiting resistor value = {prefixPostProcess(value)}ohm'

# 6      
# Function to calculate power dissipated across a resistor
def resPwr(R,V=None,I=None):
    if R and V  and I:
        return 'All parameters specified! No parameter to be calculated.'

    if V is None and I is None:
        return 'Please specify voltage or current.'
    else:
        if V is not None:
            return f'Power dissipated = {prefixPostProcess((V**2)/R)}W'
        else:
            return f'Power dissipated = {prefixPostProcess((I**2)*R)}W'

# FxnList = [ohmsLaw, resCombntion, resClrCode, valSMD, voltageDivider, currentLimiter, resPwr]

# -----------------------------------------------------------------------------------------------------
# Helper Functions 

# Function to remove SI Unit from input
def prefixPreProcess(value, prefix):
    prefixes={'p':-12, 'n':-9, 'u':-6, 'm':-3, 'o':0, 'V':0, 'A':0, 'k':3, 'M':6, 'G':9}
    return float(value) * float((10**prefixes[prefix[0]]))


# Function to add SI units to output
def prefixPostProcess(value):
    prefixes = {-12: 'p', -9: 'n', -6: 'u', -3: 'm', 0: '', 3: 'k', 6: 'M', 9: 'G'}
    power = int(0)

    # For large values
    if value > 999:
        while value > 999:
            value = value / 10
            power = power + 1

    # For small values
    if 0 < value < 1:
        while 0 < value < 1:
            value = value * 10
            power = power - 1

    if power not in prefixes.keys():
        if power > 0:
           while power not in [0, 3, 6, 9]:
                value*=10
                power-=1
        else:
            while power not in [0, -3, -6, -9]:
                value/=10
                power+=1;

    # print(power)
    # print(value)

    prefix = 'Error occcured during prefix generation'
    if power in prefixes.keys():
        prefix = prefixes[power]

    return f'{value} {prefix}'

# Use below code for testing
# prefixPostProcess(10)
# prefixPostProcess(3000)
# prefixPostProcess(500500)
# prefixPostProcess(20000000)


# prefixPostProcess(0.1)
# prefixPostProcess(0.001)
# prefixPostProcess(0.00006)
# prefixPostProcess(0.00000008)




# -------------------------------------------------------------------------------------------------
#Function to find nearest value of resistor avaiable  (Not implemented yet!)

# def nearest_resistor(R,E_series):
    
#     # Process R before and after to provide appropriate output
#     E6=[100,150,220,330,470,680]
    
#     E12=E6.copy()
#     E12.extend([120,180,270,390,560,820])
    
#     E24=E12.copy()
#     E24.extend([110,130,160,200,240,300,360,430,510,620,750,910])
    
#     E48=[100,105,110,115,121,127,133,140,147,154,162,169,178,187,196,205,215,226,237,249,261,274,287,301,316,332,348,365,383,402,422,442,464,487,511,536,562,590,619,649,681,715,750,787,825,866,909,953]
    
#     E96=E48.copy()
#     E96.extend( [102,107,113,118,124,130,137,143,150,158,165,174,182,191,200,210,221,232,243,255,267,280,294,309,324,340,357,374,392,412,432,453,475,499,523,549,576,604,634,665,698,732,768,806,845,887,931,976])
    
#     E192=E96.copy()
#     E192.extend([101,104,106,109,111,114,117,120,123,126,129,132,135,138,142,145,149,152,156,160,164,167,172,176,180,184,189,193,198,203,208,213,215,223,229,234,240,246,252,258,264,271,277,284,291,298,305,312,320,328,336,344,352,361,370,379,388,397,407,417,427,437,448,259,470,481,493,505,517,530,542,556,569,583,597,612,626,642,657,673,690,706,723,741,759,777,796,816,835,856,876,898,920,942,965,988])
    
          
#     if E_series == 6:
#         return nearest_resistor_scan(R,E6)
#     elif E_series == 12:
#         return nearest_resistor_scan(R,E12)
#     elif E_series == 24:
#         return nearest_resistor_scan(R,E24)
#     elif E_series == 48:
#         return nearest_resistor_scan(R,E48)
#     elif E_series == 96:
#         return nearest_resistor_scan(R,E96)
#     elif E_series == 192:
#         return nearest_resistor_scan(R,E192)
            
# #Function to help nearest_resistor function 
# def nearest_resistor_scan(R,E):
#     for i in range(0,len(E)):
#         if (E[i] == R):
#             return E[i]
#         if (E[i] > R):
#             if((R-E[i-1]) > (E[i]-R)):
#                 return E[i]
#             else:
#                 return E[i-1]