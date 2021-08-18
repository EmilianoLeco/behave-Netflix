import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os.path import dirname
import os

dirpath = os.path.abspath(os.path.dirname(__file__))
dirname(dirpath)
chromedriver_path_linux = (dirname(dirpath)) + "/driver/chromedriver_linux"
chromedriver_path_windows = (dirname(dirpath)) + "\\driver\\chromedriver.exe"

print(chromedriver_path_linux)
print(chromedriver_path_windows)

# define el SO en el que se estan ejecutando los test
plataforma = sys.platform


class Browser(object):
    if plataforma == "win32":
        chrome_options = Options()
        #chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-user-media-security=true')
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(chromedriver_path_windows, chrome_options=chrome_options)
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-user-media-security=true')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument("--incognito")
        #chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chromedriver_path_linux, options=chrome_options)

    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.quit()

    def delete_cookies(context):
        context.driver.delete_all_cookies()
