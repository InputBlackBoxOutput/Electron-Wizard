@ECHO OFF
ECHO Starting Electron Wizard 
ECHO Please open your browser and point it to this URL: https://localhost:5000/

set FLASK_DEBUG=1
flask run

PAUSE
EXIT