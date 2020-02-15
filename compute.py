# Electron Wizard webapp 
# 
# @file  : compute.py
# @brief : Provides computation
# @author: Rutuparn Pawar (InputBlackBoxOutput)
# @date_created : 21 August, 2019
#

#Funtion on Ohms Law V=IR
def ohmsLaw(R,V,I):    
    if R and V  and I:
        return 'All parameters specified! No parameter to be calculated'

    if not V and not I:
        return 'Specify voltage or current'
    if not R and not I:
        return 'Specify resistance or current'
    if not R and not V :
        return 'Specify resistance or voltage'


    if not R and not V and not I:
        return 'Please specify atleast 2 parameters.'

    if R:
        if V:
            return f"Current = {V/R} A"
        if I:
            return f"Voltage = {I*R} V"
    else:
    	return f"Resistance = {V/I} ohm" 	

#Function to calculate equivalent resistance of 2 resistors in series or parallel

def resCombntion(parallel,R1,R2):
    if parallel == 'P':
        return f'Equivalent Resistance {((R1*R2)/(R1+R2))} ohm'
    else:
        return f'Equivalent Resistance = {R1+R2} ohm'
        
#Function to calculate power dissipated across a resistor

def resPwr(R,V=None,I=None):
    if V is None and I is None:
        return 'Please specify voltage or current.'
    else:
        if V is not None:
            return (V**2)/R
        else:
            return (I**2)*R

#Funtion to calculate resistance of a resistor using colour code
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

        return f"{R} +- {Tolerance}% ohm"
    
    except KeyError:
        return 'No such resistor exits'
    
    except:
        return 'Error occured!'   

#Funtion to calculate value of a SMD components using markings
def valSMD(mark, compnt):
    val = mark // 10
    mult = mark % 10
    
    if compnt == 'R':
        return f'{val *(10**(mult))} ohm'
    elif compnt == 'C':
        return f'{val *(10**(mult-12))} F'    
    elif compnt == 'I':
        return f'{val *(10**(mult-6))} H'
    else:
        return 'Error occcured while computing!'
    

# Funtion to perform calculations for voltage divider
def voltageDivider(R1,R2,Vin,Vout,Rload):
    if R1 and R2:
        voltageDividerV(R1,R2,Vin,Vout,Rload)
    elif Vin and Vout:
        voltage_divider_R(Vin,Vout,R1,R2,Rload)
    else:
        return 'Error occcured while computing'


# Funtion to calculate output voltage for a voltage divider    
def voltageDividerV(R1,R2,Vin=None,Vout=None,Rload=None):
    if Rload is not None and R2 is not None:
        R2 = (R2*Rload)/(R2+Rload)
    
    if Vin is None and Vout is None:
        return 'Specify input or output voltage'
    
    if Vout is None:
        V=(R2/(R1+R2))*Vin
    else:
        V=((R1+R2)/R2)*Vout

    return f'{V} V'
    

#Funtion to calculate output voltage for a voltage divider    
def voltage_divider_R(Vin,Vout,R1=None,R2=None,Rload=None):
    if Vout < Vin :
        V_ratio = Vout/Vin
    else:
        return 'Output voltage cannot be greater than input voltage'
    
    if R1 is None and R2 is None:
        return 'Specify value of any one resistor'
    
    if Rload is not None and R2 is not None:
        R2 = (R2*Rload)/(R2+Rload)
            
    if R2 is None:
            R = (V_ratio/(1-V_ratio))*R1
    else:
            R = ((1-V_ratio)/V_ratio)*R2
        
    return f'{R} ohm'
    

#Function to calculate resistance of resitor used as current limiter for Light Emitting Diode (LED)
def currentLimiter(Vsrc,Iled,Clr):
    
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
        return f'Current limiting resistor value = {value} ohm'


# -----------------------------------------------------------------------------------------------------
# Helper Functions (Not implemented yet!)

# Function to remove SI Unit from input

# def SI_Unit_Input_Processing(value,unit_char='U'):
    
#     SI_Unit_prefixes={'p':-12,'n':-9,'u':-6,'m':-3,'U':0,'k':3,'M':6,'G':9}
#     actual_value = value* (10**SI_Unit_prefixes[unit_char])
    
#     return actual_value

# #Funtion to add SI units to output
# def SI_Unit_Output_Processing(value):
    
#     SI_Unit_prefixes={-12:'p',-9:'n',-6:'u',-3:'m',0:'U',3:'k',6:'M',9:'G'}
    
#     power=int(0)
               
#     if(value > 999):
#         while(value>999):
#             value = value/10
#             power = power+1
    
#     if(0 < value < 1):
#         while(0<value<1):
#             value = value*10
#             power = power-1
          
    
#     print(power)
#     print(value)
    
#     if power not in SI_Unit_prefixes.keys():
#         if(power > 0): 
#             for i in [0,3,6,9]:
#                 print("i="+str(i))
#                 if(power < i):
#                     upper_diff = (i+3) - power
#                     lower_diff = power - i
#                     if(upper_diff > lower_diff):
#                         power = power - lower_diff
#                         value = value * (10**lower_diff)
#                         break
#                     else:
#                         power = power + upper_diff
#                         value = value / (10**upper_diff)
#                         break
#         else:
#             for i in [0,-3,-6,-9]:
#                 print("i="+str(i))
#                 if(power > i):
#                     upper_diff = abs((i+3) - power)
#                     lower_diff = abs(power - i)
#                     if(upper_diff > lower_diff):
#                         power = power + lower_diff
#                         value = value / (10**lower_diff)
#                         break
#                     else:
#                         power = power - upper_diff
#                         value = value * (10**upper_diff)
#                         break

         
            
#     print(power)
#     print(value)
#     if(power in SI_Unit_prefixes.keys()):
#         unit_char = SI_Unit_prefixes[power]
#     return (value, unit_char)      

# SI_Unit_Output_Processing(0.0111)

# -------------------------------------------------------------------------------------------------
#Function to find nearest value of resistor avaiable  

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