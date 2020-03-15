@ECHO OFF
REM Batch file to set up internal server and show home page on default browser

TITLE Electron Wizard 

ECHO Electron Wizard
ECHO Developed by Rutuparn Pawar (InputBlackBoxOutput)
ECHO.

ECHO If nothing happened, do the following:
ECHO 1) Open your favorite browser  
ECHO 2) Copy and paste one of the following URLs
ECHO https://localhost:5000/ or https://127.0.0.1:5000/
ECHO.

REM SET FLASK_APP=app.py 
REM SET FLASK_DEBUG=1
REM flask run

python app.py 

PAUSE
EXIT
