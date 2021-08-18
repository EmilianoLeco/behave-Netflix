# Automatizacion

_Prueba de automatizacion_


### Pre-requisitos

_instalar lo necesario segun el archivo requirements.txt_

```
pip install -r requirements.txt
```

## Ejecutando las pruebas 

_Los Tests se encuentran en la carpeta Behave-Netflix\features_

### Ejecucion desde cmd 

_Nos posicionamos en la carpeta "Behave-Netflix" y ejecutamos la siguiente linea_


### ejecutar todos los escenarios

```    
   behave behave features\0-NETFLIX
```

### Ejecucion con tags

```
   behave --tags="@test01
```
### Ejecucion desde Pycharm 
```
_Es necesario configurar pycharm segun la imagen Config_Run.png_
```

### Ejecucion con Allure 

_Para Realizar reportes con allure es necesario agregar la carpeta que contiene el "allure.bat"
 (allure-commandline-2.10.0\allure-2.10.0\bin) en el path del sistema_
 
_run by allure
```
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features
```
_Lo anterior genero en "allure/results" un json que vamos a usar para hacer el reporte en la carpeta "allure/reports"_

```
allure serve allure\results
allure generate allure/results/ -o allure/reports
```

### Ejecucion con run.bat
```
En la terminal ejecutar: run.bat
```