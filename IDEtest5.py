# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class IDEtest5(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote("http://localhost:4444/wd/hub",
                                                webdriver.DesiredCapabilities.CHROME)

        self.driver.implicitly_wait(30)
        self.base_url = "http://docs.telerik.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_i_d_etest5(self):
        driver = self.driver
        driver.get(self.base_url + "/kendo-ui/api/javascript/ui/grid#configuration-columns.hidden")
        driver.find_element_by_id("gsc-i-id1").click()
        driver.find_element_by_css_selector("img.logo").click()
        driver.find_element_by_link_text("Demos").click()
        driver.find_element_by_link_text("Map").click()
        driver.find_element_by_link_text("Bubble layer").click()
        driver.find_element_by_link_text("Export").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
