# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest01():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test01(self):
    self.driver.get("http://localhost:8383/voila/render/index.ipynb")
    self.driver.set_window_size(1280, 720)
    self.driver.save_screenshot("widget01.png")
    time.sleep(5)
    self.driver.execute_script("window.scrollTo(0, 1000)")
    self.driver.save_screenshot("widget02.png")

test = TestTest01()
test.setup_method('Chrome')
test.test_test01()
test.teardown_method('Chrome')

