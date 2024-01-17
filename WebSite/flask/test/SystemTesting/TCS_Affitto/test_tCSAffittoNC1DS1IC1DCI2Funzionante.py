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

class TestTCSAffittoNC1DS1IC1DCI2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCSAffittoNC1DS1IC1DCI2(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1265, 1372)
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").click()
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").send_keys("annayellow@gmail.com")
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").click()
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").click()
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").send_keys("yellowAnnPass!456")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    self.driver.find_element(By.ID, "search").click()
    self.driver.find_element(By.ID, "search").send_keys("Milano")
    self.driver.find_element(By.ID, "nutton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(9) .img-fluid").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    self.driver.find_element(By.ID, "lastCheckInDate").click()
    self.driver.find_element(By.ID, "lastCheckInDate").send_keys("2025-02-22")
    self.driver.find_element(By.CSS_SELECTOR, ".card-body").click()
    self.driver.find_element(By.ID, "button1").click()
    assert self.driver.switch_to.alert.text == "La data di check-in non può essere successiva alla data di check-out."
  
