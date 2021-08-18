from behave import *
from time import sleep


@given('El usuario navega a la página: "{URL}"')
def step_impl(context, URL):
    context.home_page.navigate('{}'.format(URL))
    pass


