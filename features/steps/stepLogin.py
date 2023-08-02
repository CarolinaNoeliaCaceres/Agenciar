from behave import given, when, then
from Pages.login_page import LoginPage
from Pages.menu_page import MenuPage
from hamcrest import assert_that, equal_to, greater_than_or_equal_to,is_not
import allure


@given(u'la url de Agenciar')
def step_impl(context):
    #context.page = LoginPage()
    #context.page.open("CHROME",
    #                  implicity_wait=10, url=context.config.userdata["URL"])
    pass

@given(u'al seleccionar Ingresar e ingresar Usuario y password')
def step_impl(context):
   pass


@when(u'cuando se realiza click en "Ingresar"')
def step_impl(context):
   pass


@then(u'se inicia sesion con exito')
def step_impl(context):
   pass