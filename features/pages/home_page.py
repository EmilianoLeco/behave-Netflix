import re
from time import sleep
import allure
from allure_commons._allure import Attach
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, \
    WebDriverException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from features.driver.browser import Browser
import sys

sys.tracebacklimit = 3

import random
import string


# Home Page Actions
class HomePage(Browser):

    # Navego a la URL del Escenario
    def navigate(self, address):
        self.driver.get(address)

    def type_element(self, element):
        global locator_element
        if element[0] == "/":
            locator_element = By.XPATH
        else:
            locator_element = By.ID

        return locator_element

    # FUNCIÓN QUE ESPERA CIERTA CANTIDAD DE TIEMPO HASTA QUE SEA VISIBLE UN ELEMENTO
    # SOLO REQUIERE EL ELEMENTO
    def timeout_element(self, visible_element, timeout=30, poll_frequency=3):
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
            wait.until(EC.element_to_be_clickable((self.type_element(visible_element), visible_element)))
            wait.until(EC.visibility_of_element_located((self.type_element(visible_element), visible_element)))
            status = True
        except TimeoutException:
            print("\nElemento no visible luego de {} seconds".format(timeout))

            status = False
        except Exception as e:
            self.checkpoints("\nAn Exception Ocurred: {0}".format(e))
            allure.attach(self.driver.get_screenshot_as_png(), name="Not found Element",
                          attachment_type=allure.attachment_type.PNG)
            status = "ERROR"
        return status

    def click_element(self, locator):
        # Espera un tiempo determinado hasta que el elemento sea visible
        self.timeout_element(locator, timeout=10)
        try:
            #
            self.driver.find_element(self.type_element(locator), locator).click()
        except ElementClickInterceptedException:
            raise Exception("Elemento no habilitado")
        except WebDriverException:
            raise Exception("No fue posible hacer click en el elemento esperado")

    def input_By_ID(self, text, *locator):
        self.timeout_element(*locator, timeout=20)
        self.driver.find_element_by_id(*locator).clear()
        self.driver.find_element_by_id(*locator).send_keys(text)

    def click_element_By_ID(self, *locator):
        self.driver.find_element_by_id(*locator).click()

    def click_element_By_CSS(self, *locator):
        self.driver.find_element_by_css_selector(*locator).click()

    def select_element_By_ID(self, select, *locator):
        list_select = Select(self.driver.find_element_by_id(*locator))
        if locator[0] == 'days' or locator[0] == 'years':
            list_select.select_by_visible_text('{}  '.format(select))
        else:
            list_select.select_by_visible_text(select)

    def click_checkbox(self, locator):
        self.driver.find_element(self.type_element(locator), locator).send_keys(Keys.SPACE)

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def select_element(self, select_option, locator):
        lista = Select(self.driver.find_element(self.type_element(locator), locator))
        lista.select_by_visible_text(select_option)

    def get_page_title(self):
        return self.driver.title

    # VALIDA TEXTO, locator: puede ser un elemento directo o una variable DE "Mapeo_de_textos.py" que es una tupla
    # compuesta por ("texto", "id\xpath")
    def text_and_button_validation(self, locator, boton=False, timeout=60):
        # flag = self.timeout_element(locator_title)
        sleep(2)
        # Espera un tiempo determinado hasta que el elemento sea visible
        self.timeout_element(locator[1], timeout)

        # Extraigo el texto de un elemento
        get_text = self.driver.find_element(self.type_element(locator[1]), locator[1]).text

        # Valido la comparacion de textos
        if locator[0] == get_text:
            if boton:
                print("\n Boton Visible: {}".format(get_text))
                self.checkpoints("\n Boton Visible: {}".format(get_text), type=AttachmentType.TEXT)
            else:
                print("\n Texto Correcto: {}".format(get_text))
                self.checkpoints("\n Texto Correcto: {}".format(get_text), type=AttachmentType.TEXT)
        else:
            if boton:
                print("\n Boton no habilitado, se esperaba: {} y se obtuvo: {}".format(locator[0], get_text))
                self.checkpoints("\n Boton no habilitado, se esperaba: {} y se obtuvo: {}".format(locator[0], get_text), type=AttachmentType.TEXT)
            else:
                print("\n Texto Incorrecto, se esperaba: {} y se obtuvo: {}".format(locator[0], get_text))
                self.checkpoints("\n Texto Incorrecto, se esperaba: {} y se obtuvo: {}".format(locator[0], get_text), type=AttachmentType.TEXT)
            raise Exception("\n No habilitado, se esperaba: {} y se obtuvo: {}".format(locator[0], get_text))

    # Adjuntar msj o print
    def checkpoints(self, validation, name_defect="Checkpoint", type=AttachmentType.TEXT):
        #allure.attach(validation, name=name_defect)
        Attach.__call__(self, body=validation, name=name_defect, attachment_type=type)
        print(validation)

    def move_page(self, locator):
        if "page_down" == locator:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            locate_item = self.driver.find_element(self.type_element(locator), locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", locate_item)

    def zoom_page(self, level_zoom):
        self.driver.execute_script("document.body.style.zoom='{}';".format(level_zoom))

    def get_text(self, element_text):
        # Espero hasta que el elemento sea visible
        self.timeout_element(element_text)
        # Devuelvo el txt del elemento
        return self.driver.find_element(self.type_element(element_text), element_text).text

    def get_element(self, element_text):
        return self.driver.find_element(self.type_element(element_text), element_text)

    # Estado de elemento
    def enable_element(self, element):
        global state
        try:
            state = self.driver.find_element(self.type_element(element), element).is_enabled()
        except NoSuchElementException:
            print("No visible - habilitado")
            state = False
        finally:
            return state

    def status_checkbox(self, locator):
        global state
        try:
            state = self.driver.find_element(self.type_element(locator), locator).is_selected()
        except NoSuchElementException:
            print("No visible - habilitado")
            state = False
        finally:
            return state

    def log_allure_report(self, text):
        allure.attach(text, name="Validation text:",
                      attachment_type=allure.attachment_type.TEXT)

    def get_screenshot_png(self):
        return self.driver.get_screenshot_as_png()

    def random_email(self, len):
        return ''.join(random.choice(string.ascii_letters) for x in range(len))
