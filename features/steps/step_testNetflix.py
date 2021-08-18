from time import sleep

from behave import *
from Tools.Mapeo_de_textos import dicc


@when('Espero a que cargue la pagina')
def step_impl(context):
    context.home_page.timeout_element("//h1[@class='our-story-card-title']", timeout=35)
    pass


@Step(u'Valido titulo: "{TITLE}"')
def step_impl(context, TITLE):
    assert context.home_page.get_page_title() == TITLE
    pass


# ---------------------------------------------------------------------------------#

@Step(u'El usuario hace click en Iniciar Sesión')
def step_impl(context):
    context.home_page.click_element("//a[text()='Iniciar sesión']")
    pass


@Step(u'Valido texto: "{TXT}"')
def step_impl(context, TXT):
    context.home_page.text_and_button_validation((TXT, dicc[TXT]))
    pass
