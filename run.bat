echo off

REM Prueba de ejecucion con creacion de reporte

behave "features"
TIMEOUT /T 3 /NOBREAK
echo python -m behave2cucumber -i Reports/behave.json -o Reports/cucumber.json
python -m behave2cucumber -i Reports/behave.json -o Reports/cucumber.json
TIMEOUT /T 3 /NOBREAK
node Tools/index.js