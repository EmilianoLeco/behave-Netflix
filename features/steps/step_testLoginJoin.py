from time import sleep

from behave import *
from behave import capture

from Tools.Mapeo_de_textos import dicc


@Step(u'Ingresa el siguiente email: "{STR}"')
def step_impl(context, STR):
    context.home_page.input_By_ID(STR, "id_userLoginId")
    pass


@step(u'Ingresa la siguiente contraseña: "{STR}"')
def step_impl(context, STR):
    context.home_page.input_By_ID(STR, "id_password")
    pass


@step(u'Desmarca el botón de "Recuerdame"')
def step_impl(context):
    context.home_page.click_checkbox("bxid_rememberMe_true")
    pass


@Step(u'Realiza click en "Iniciar Sesión"')
def step_impl(context):
    context.home_page.click_element("//button[@class='btn login-button btn-submit btn-small']")
    pass


@then(u'Valida mensaje de error: "{MSG}"')
def step_impl(context, MSG):
    context.home_page.text_and_button_validation((MSG, dicc[MSG]))
    pass


@Step(u'Valida boton "Recuerdame" seleccionado')
def step_impl(context):
    if context.home_page.status_checkbox("bxid_rememberMe_true"):
        print('Checkbox is selected')
        #context.home_page.log_allure_report('Checkbox is selected')
    else:
        #context.home_page.log_allure_report('Sorry, Checkbox is not selected')
        raise Exception("Sorry, Checkbox is not selected")
    pass


@when(u'El usuario ingresa un email en el LandingPage')
def step_impl(context):
    context.email = context.home_page.random_email(7) + "@gmail.com"
    context.home_page.input_By_ID(context.email, "id_email_hero_fuji")
    pass


@when(u'El usuario hace click en "Comenzar"')
def step_impl(context):
    context.home_page.click_element("//div[@class='our-story-card hero-card hero_fuji vlv']//span[text()='Comenzar']")
    pass


@then(u'Es dirigido a la pagina de registro')
def step_impl(context):
    context.home_page.text_and_button_validation(
        ("Completa la configuración de tu cuenta", "//h1[text()='Completa la configuración de tu cuenta']"))
    pass


