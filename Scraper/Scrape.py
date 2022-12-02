from selenium import webdriver
from time import sleep


driver_path = "C:\Giri_Practice\PythonPractice\rental\chromedriver.exe"
def launch_driver():
    driver = webdriver.Chrome(driver_path)
    driver.get('https://www.oyorooms.com/')
    sleep(5)
    driver.close()
    

launch_driver()