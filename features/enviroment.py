import allure

def after_step(context,step):
    allure.attach(context.page.browser.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)