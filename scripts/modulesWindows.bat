REM Batch file to install modules required by Electron-Wizard

@ECHO off
TITLE Installing modules
ECHO Installing modules required by Electron Wizard
ECHO.

pip install flask
pip install flask-wtf

ECHO.
ECHO Finished
PAUSE 