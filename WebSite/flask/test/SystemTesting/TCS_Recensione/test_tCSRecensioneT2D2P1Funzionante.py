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

class TestTCSRecensioneT2D2P1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCSRecensioneT2D2P1(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1265, 1372)
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").click()
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").send_keys("sofiaesposito@gmail.com")
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").click()
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").send_keys("Passsofy1@")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, "svg").click()
    self.driver.find_element(By.LINK_TEXT, "Recensione").click()
    self.driver.find_element(By.ID, "titolo").click()
    self.driver.find_element(By.ID, "titolo").send_keys("Casa molto accogliente")
    self.driver.find_element(By.ID, "descrizione").click()
    self.driver.find_element(By.ID, "descrizione").send_keys("Una casa perfetta, vicino l’università!")
    self.driver.find_element(By.NAME, "voto").click()
    dropdown = self.driver.find_element(By.NAME, "voto")
    dropdown.find_element(By.XPATH, "//option[. = '5']").click()
    self.driver.find_element(By.ID, "mioBottone").click()
  
