import os

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class BasePage:
    browser= None
    _intance =None

    ##Se valida si existe una instancia de la clase, si no existe la crea
    def __new__(cls, *args, **kwargs):
        if not cls._intance:
            cls._intance= object.__new__(cls)
        return cls._intance

    def open(self,browser_name, implicity_wait,url):

        if browser_name.upper()=="CHROME":
            chrome_profile = Options()
            chrome_profile.add_argument('--allow-running-insecure-content')
            chrome_profile.add_argument('--ignore-certificate-errors')
            #chrome_profile.add_argument("--headless")
            #chrome_profile.add_argument("--disable-gpu")

            #chrome_profile.add_argument("--start-maximized")
            chrome_profile.add_argument("--disable-features=VizDisplayCompositor")
            chrome_profile.add_argument("--window-size=1262x822")

            #chrome_profile.add_experimental_option('excludeSwitches', ['enable-logging'])


            #profile = {"download.default_directory": path+'\Descargas',
            #    "download.directory_upgrade": True}
            #chrome_profile.add_experimental_option("prefs", profile)
            #self.browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_profile)
            service = Service(ChromeDriverManager(version="114.0.5735.90").install())

            self.browser = webdriver.Chrome(service=service, options=chrome_profile)

        elif browser_name.upper=="FIREFOX":
            self.browser=webdriver.Firefox()
        else:
            print("Error")
        self.browser.implicitly_wait(implicity_wait)
        self.browser.get(url)

    def click(self, locator, index=0):
        if index >= 0:
            try:
                #WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located(locator))
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))

                elements = self.browser.find_elements(*locator)
                elements[index].click()

            except Exception as error:
                print("Elemento no clickable .Error:" + str(error))
        else:
            print("Index erroneo")

    def listclick(self, locator, index=0):
        if index >= 0:
            try:
                elements = self.browser.find_elements(*locator)
                elements[index].click()

            except Exception as error:
                print("Elemento no encontrado.Error:" + str(error))
        else:
            print("Index erroneo")

    def send_key(self,locator,valor,index=0):
        try:
            if locator is not None:
                WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
                elements = self.browser.find_elements(*locator)
                elements[index].send_keys(valor)

        except Exception as error:
            print("Elemento no encontrado.Error:" + str(error))

    def text(self,locator, index=0):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
            elements = self.browser.find_elements(*locator)
            return elements[index].text

        except Exception as error:
            print("Elemento no encontrado.Error:" + str(error))

    def select_by_visible_text(self, locator, text , index=0):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
            elements = self.browser.find_elements(*locator)
            select = Select(elements[index])
            select.select_by_visible_text(text)

        except Exception as error:
            print("Elemento no encontrado.Error:" + str(error))

    def get_screenshot_as_file(self, screen_folder, file_name):
        if not os.path.exists(screen_folder):
            os.mkdir(screen_folder)
        file_name = os.path.join(screen_folder, file_name)
        self.browser.get_screenshot_as_file(file_name)

    def elemento_visible(self,locator,index=0):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
            elements = self.browser.find_elements(*locator)
            return elements[index].is_displayed()

        except Exception as error:
            return False

    def button_interactuable(self, locator, index=0):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
            elements = self.browser.find_elements(*locator)
            return elements[index].is_enabled()

        except Exception as error:
            print("Elemento no encontrado.Error:" + str(error))

    def obtenerValue(self, locator, index=0):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
            elements = self.browser.find_elements(*locator)
            return elements[index].get_attribute("value")

        except Exception as error:
            print("Elemento no encontrado.Error:" + str(error))

    def obtenerinnerHTML(self, locator, index=0):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
            elements = self.browser.find_elements(*locator)
            return elements[index].get_attribute("innerHTML")

        except Exception as error:
            print("Elemento no encontrado.Error:" + str(error))

    def isElementPresent(self,locator,index=0):
      try:
          WebDriverWait(self.browser,10).until(EC.presence_of_element_located(locator))
          elements = self.browser.find_elements(*locator)
          return elements[index].is_displayed()

      except Exception as error:
        return False

    def setatributo(self,locator,valor,index=0):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
            elements = self.browser.find_elements(*locator)
            elements[index].get_attribute("value",valor)

        except Exception as error:
            return False






