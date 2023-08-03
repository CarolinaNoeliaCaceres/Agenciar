from Pages.Base_page import BasePage
from selenium.webdriver.common.by import By
import unittest

class LoginPage(BasePage):

    btn_ingresar=By.XPATH,"//button/span[contains(text(),'Ingresar')]"
    box_usuario= By.ID,'mat-input-0'
    box_Password = By.ID, 'mat-input-1'
    botonLogin=By.XPATH,"//button[@class='mat-focus-indicator agencia-mat-btn login-btn btn-block mat-flat-button mat-button-base']"
    icon_ojo=By.XPATH,"//i[@class='material-icons password-icon ng-tns-c78-21']"

    def click_btn_ingresar(self):
        self.click(self.btn_ingresar)

    def cargar_box_usuario(self,text):
        self.send_key(self.box_usuario,text)

    def cargar_box_Password(self,text):
        self.send_key(self.box_Password,text)

    def click_BotonLogin(self):
        self.click(self.botonLogin)
