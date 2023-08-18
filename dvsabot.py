from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

def CheckTestDates():
    driver = webdriver.Chrome()
    driver.get("https://www.gov.uk/book-driving-test")
    driver.implicitly_wait(5)
    driver.find_element(by = By.LINK_TEXT, value = "Start now").click() #page1 start now button
    driver.implicitly_wait(5)
    driver.find_element(by = By.ID, value = "test-type-car").click() #page2 test type button
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "driving-licence").send_keys("JAROC001265JJ9YW") #page 3
    driver.find_element(By.ID, "special-needs-none").click()
    driver.find_element(By.ID, "driving-licence-submit").click()
    driver.implicitly_wait(5)
    driver.find_element(By.I, "test-choice-calendar").send_keys(str(datetime.today().strftime("%d/%m/%y"))) #page 4
    driver.find_element(By.ID, "driving-licence-submit").click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "test-centres-input").send_keys("BD17 5PQ") #page 5
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "center-name-185").click() #page 6
    driver.implicitly_wait(5)
    availabledates = driver.find_elements(By.CLASS_NAME, "BookingCalendar-date--bookable")
    return availabledates 