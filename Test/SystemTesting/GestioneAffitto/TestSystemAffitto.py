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

class TestNC2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_nC2(self):
    delay = 5.0
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1265, 1372)
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").send_keys("sofiaesposito@gmail.com")
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").click()
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").send_keys("Passsofy1@")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    self.driver.find_element(By.ID, "search").click()
    self.driver.find_element(By.ID, "search").send_keys("Salerno")
    self.driver.find_element(By.ID, "nutton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(6) .card-title").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    self.driver.find_element(By.ID, "cc-number").clear()
    self.driver.find_element(By.ID, "cc-number").send_keys("55443213431334 ")
    self.driver.find_element(By.ID, "mese_scadenza").click()
    dropdown = self.driver.find_element(By.ID, "mese_scadenza")
    dropdown.find_element(By.XPATH, "//option[. = '3']").click()
    self.driver.find_element(By.ID, "lastCheckInDate").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card-body").click()
    self.driver.find_element(By.ID, "lastCheckOutDate").click()
    self.driver.find_element(By.ID, "lastCheckOutDate").click()
    self.driver.find_element(By.ID, "lastCheckOutDate").send_keys("2028-11-22")
    self.driver.find_element(By.CSS_SELECTOR, ".list-group > .list-group-item:nth-child(1)").click()
    self.driver.find_element(By.ID, "confermaPagamentoBtn").click()
    assert self.driver.switch_to.alert.text == "Il numero della carta deve essere di almeno 16 cifre."


  def test_nC1DS2(self):
    delay = 5.0
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1265, 1372)
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").send_keys("sofiaesposito@gmail.com")
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").click()
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").send_keys("Passsofy1@")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    self.driver.find_element(By.ID, "search").click()
    self.driver.find_element(By.ID, "search").send_keys("Salerno")
    self.driver.find_element(By.ID, "nutton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(6) .card-title").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    self.driver.find_element(By.ID, "mese_scadenza").click()
    self.driver.find_element(By.ID, "confermaPagamentoBtn").click()
    assert self.driver.switch_to.alert.text == "Carta Scaduta"



  def test_nC1DS1IC2(self):
    delay = 5.0
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1265, 1372)
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").send_keys("sofiaesposito@gmail.com")
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").click()
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").send_keys("Passsofy1@")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    self.driver.find_element(By.ID, "search").click()
    self.driver.find_element(By.ID, "search").send_keys("Salerno")
    self.driver.find_element(By.ID, "nutton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(6) .img-fluid").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    self.driver.find_element(By.ID, "mese_scadenza").click()
    dropdown = self.driver.find_element(By.ID, "mese_scadenza")
    dropdown.find_element(By.XPATH, "//option[. = '3']").click()
    self.driver.find_element(By.ID, "cc-cvv").click()
    self.driver.find_element(By.ID, "cc-cvv").clear()
    self.driver.find_element(By.ID, "cc-cvv").send_keys("2")
    self.driver.find_element(By.ID, "confermaPagamentoBtn").click()
    assert self.driver.switch_to.alert.text == "Il CVV deve essere di almeno 3 cifre."

  def test_nC1DS1IC1DCI2(self):
    delay = 5.0
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1265, 1372)
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").send_keys("sofiaesposito@gmail.com")
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").click()
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").send_keys("Passsofy1@")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    self.driver.find_element(By.ID, "search").click()
    self.driver.find_element(By.ID, "search").send_keys("Salerno")
    self.driver.find_element(By.ID, "nutton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(6) .img-fluid").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    self.driver.find_element(By.ID, "lastCheckInDate").click()
    self.driver.find_element(By.ID, "lastCheckInDate").send_keys("2029-01-22")
    self.driver.find_element(By.CSS_SELECTOR, ".card-body").click()
    self.driver.find_element(By.ID, "button1").click()
    assert self.driver.switch_to.alert.text == "La data di check-in non può essere successiva alla data di check-out."


  def test_nC1DS1IC1DCI1DCO2(self):
    delay = 5.0
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1265, 1372)
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").send_keys("sofiaesposito@gmail.com")
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").click()
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").send_keys("Passsofy1@")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    self.driver.find_element(By.ID, "search").click()
    self.driver.find_element(By.ID, "search").send_keys("Salerno")
    self.driver.find_element(By.ID, "nutton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(6) .mb-0:nth-child(2)").click()
    element = self.driver.find_element(By.LINK_TEXT, "Next")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "lastCheckInDate").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "lastCheckOutDate").click()
    self.driver.find_element(By.ID, "button1").click()
    assert self.driver.switch_to.alert.text == "Check-in e check-out sono lo stesso giorno."



  def test_nC1DS1IC1DCI1DCO1P2(self):
    delay = 5.0
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1265, 1372)
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").send_keys("sofiaesposito@gmail.com")
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").click()
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").send_keys("Passsofy1@")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    self.driver.find_element(By.ID, "search").click()
    self.driver.find_element(By.ID, "search").send_keys("Salerno")
    self.driver.find_element(By.ID, "nutton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(6) .img-fluid").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    #self.driver.find_element(By.ID, "lastCheckOutDate").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "lastCheckOutDate").clear()
    time.sleep(delay)
    self.driver.find_element(By.ID, "lastCheckOutDate").send_keys("13-02-2024")
    time.sleep(delay)
    self.driver.find_element(By.ID, "lastCheckInDate").click()
    self.driver.find_element(By.ID, "button1").click()
    time.sleep(delay)
    assert self.driver.switch_to.alert.text == "L\'affitto deve essere minimo di 3 mesi."

  def test_nC1DS1IC1DCI1DCO1P1(self):
    delay = 5.0
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1265, 1372)
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "exampleDropdownFormEmail1").send_keys("sofiaesposito@gmail.com")
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").click()
    self.driver.find_element(By.ID, "exampleDropdownFormPassword1").send_keys("Passsofy1@")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    self.driver.find_element(By.ID, "search").click()
    self.driver.find_element(By.ID, "search").send_keys("Salerno")
    self.driver.find_element(By.ID, "nutton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(6) .img-fluid").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    time.sleep(delay)
    self.driver.find_element(By.ID, "lastCheckInDate").click()
    self.driver.find_element(By.ID, "lastCheckInDate").clear()
    time.sleep(delay)
    self.driver.find_element(By.ID, "lastCheckInDate").send_keys("13-01-2025")
    time.sleep(delay)
    self.driver.find_element(By.ID, "lastCheckOutDate").clear()
    time.sleep(delay)
    self.driver.find_element(By.ID, "lastCheckOutDate").send_keys("13-11-2025")
    time.sleep(delay)
    self.driver.find_element(By.ID, "lastCheckInDate").click()
    self.driver.find_element(By.ID, "button1").click()
    time.sleep(delay)

  
