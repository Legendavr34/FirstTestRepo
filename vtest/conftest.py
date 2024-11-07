from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import time

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    service = Service(executable_path=r'C:\chromedriver-win64\chromedriver.exe')
    browser = webdriver.Chrome(service=service,options=options )
    browser.maximize_window()
    browser.implicitly_wait(4)
    yield browser