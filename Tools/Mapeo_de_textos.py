"""
    MAPEO DE MSJ DE ERROR - TEXTOS Y TITULOS QUE SE VISUALIZAN EN LA PAGINA

            Consta de una tupla formada por (texto esperado, elemento para reconocer el texto)
"""

# Textos y Mensajes del Backoffice

MSJ_DELETE_USER = ("¿Está seguro?", "//div[@id='content']/h1")

dicc = {"Inicia sesión": "//h1",
        "Iniciar sesión con Facebook": "//span[@class='fbBtnText']",
        "No podemos encontrar una cuenta con esta dirección de email. Reinténtalo o crea una cuenta nueva.": "//div[@class='ui-message-contents']"}
