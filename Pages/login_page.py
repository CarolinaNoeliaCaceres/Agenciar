from Pages.Base_page import BasePage
from selenium.webdriver.common.by import By
import unittest

class LoginPage(BasePage):

    btn_ingresar=By.XPATH,"//button/span[contains(text(),'Ingresar')]"
    box_usuario= By.ID,'mat-input-3'
    box_Password = By.ID, 'mat-input-4'
    botonLogin=By.XPATH,"//form[@class='ng-pristine ng-invalid ng-touched']//button[@class='mat-focus-indicator agencia-mat-btn login-btn btn-block mat-flat-button mat-button-base']"
    icon_ojo=By.XPATH,"//i[@class='material-icons password-icon ng-tns-c78-21']"
