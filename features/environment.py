import allure
from behave.model_core import Status

def before_scenario(context, scenario):
    context.nombre='TEST'
def after_step(context,step):
    if step.status != 'failed':
        allure.attach(context.page.browser.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)