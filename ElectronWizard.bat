@ECHO OFF
REM Batch file to set up internal server 

TITLE Electron Wizard 
COLOR 0a

ECHO Electron Wizard
ECHO Developed by Rutuparn Pawar (InputBlackBoxOutput)

ECHO If nothing happened, do the following:
ECHO 1) Open your favorite browser  
ECHO 2) Copy and paste one of the following URLs
ECHO https://localhost:5000/ or https://127.0.0.1:5000/

SET FLASK_APP=app.py
SET FLASK_DEBUG=1
flask run 

REM start chrome https://localhost:5000/

PAUSE
EXIT
