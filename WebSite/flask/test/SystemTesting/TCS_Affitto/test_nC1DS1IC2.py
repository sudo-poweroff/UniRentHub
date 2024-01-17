# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestNC1DS1IC2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_nC1DS1IC2(self):
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
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").send_keys("yellowAnnPass!456")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    self.driver.find_element(By.ID, "search").click()
    self.driver.find_element(By.ID, "search").send_keys("Milano")
    self.driver.find_element(By.ID, "nutton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(9) .img-fluid").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-3:nth-child(2) > #anno_scadenza").click()
    dropdown = self.driver.find_element(By.CSS_SELECTOR, ".col-md-3:nth-child(2) > #anno_scadenza")
    dropdown.find_element(By.XPATH, "//option[. = '2024']").click()
    self.driver.find_element(By.ID, "anno_scadenza").click()
    dropdown = self.driver.find_element(By.ID, "anno_scadenza")
    dropdown.find_element(By.XPATH, "//option[. = '1']").click()
    self.driver.find_element(By.ID, "cc-cvv").click()
    self.driver.find_element(By.ID, "cc-cvv").send_keys("21")
    self.driver.find_element(By.ID, "confermaPagamentoBtn").click()
    #assert self.driver.switch_to.alert.text == "Il CVV deve essere di almeno 3 cifre."
    try:
      alert_text = self.driver.switch_to.alert.text
      assert alert_text == "Il CVV deve essere di almeno 3 cifre."
    except NoAlertPresentException:
      # Gestisci il caso in cui l'alert non è presente
      print("L'alert non è presente.")
    else:
      # Effettua l'assert su alert_text
      assert alert_text == "Il CVV deve essere di almeno 3 cifre."

