import os
import time
import zipfile
from lib2to3.pgen2.driver import Driver
import selenium
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
import string
from selenium.webdriver import Chrome, ChromeOptions



#random gmail
def randommail():
    harfler = string.ascii_lowercase
    mail=''.join(random.choice(harfler) for i in range(20))
    gmail=mail+"@gmail.com"
    return gmail
#random şifre
def randompass():
    harfler = string.digits
    password=''.join(random.choice(harfler) for i in range(8))
    tir='.'
    tir2='a'
    tir3='A'
    password=password+tir+tir2+tir3
    return password

#txt yazma
def yazma(gmail,sifre):

    f = open("account.txt", "a")
    f.writelines(f"{gmail}\n")
    f.writelines(f"{sifre}\n")

#//*[@id="recaptcha-anchor"]/div[1]
#//*[@id="solver-button"]


def main():
    gmail=randommail()
    sifre=randompass()
    yazma(gmail=gmail,sifre=sifre)
    ayarlar = ChromeOptions()
    ayarlar.add_extension("buster.crx")
    driver= webdriver.Chrome(options=ayarlar)
    try:
      driver.get("https://www.yemeksepeti.com/login/new?step=email")
      time.sleep(50.60)
      driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(gmail)
      time.sleep(2.60)
      driver.find_element(By.XPATH,'//*[@id="login-page-react-root"]/main/div/form/div[3]/button').click()
      time.sleep(5)
      driver.find_element(By.XPATH,'//*[@id="first_name"]').send_keys("Eren")
      time.sleep(2.60)
      driver.find_element(By.XPATH,'//*[@id="last_name"]').send_keys("Sönerkeyf")
      time.sleep(2.60)
      driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(sifre)
      time.sleep(2.60)
      driver.find_element(By.XPATH,'//*[@id="login-page-react-root"]/main/div/form/div[8]/button').click()
      time.sleep(2.60)
      driver.find_element(By.XPATH,'//*[@id="select-all-label"]/div').click()
      time.sleep(2.60)
      driver.find_element(By.XPATH,'//*[@id="login-page-react-root"]/main/div/div/div[4]/button').click()
      time.sleep(10.60)
      driver.quit()
    except:
        time.sleep(5.60)
        driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(gmail)
        time.sleep(2.60)
        driver.find_element(By.XPATH,'//*[@id="login-page-react-root"]/main/div/form/div[3]/button').click()
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="first_name"]').send_keys("Eren")
        time.sleep(2.60)
        driver.find_element(By.XPATH,'//*[@id="last_name"]').send_keys("Sönerkeyf")
        time.sleep(2.60)
        driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(sifre)
        time.sleep(2.60)
        driver.find_element(By.XPATH,'//*[@id="login-page-react-root"]/main/div/form/div[8]/button').click()
        time.sleep(2.60)
        driver.find_element(By.XPATH,'//*[@id="select-all-label"]/div').click()
        time.sleep(2.60)
        driver.find_element(By.XPATH,'//*[@id="login-page-react-root"]/main/div/div/div[4]/button').click()
        time.sleep(10.60)
        driver.quit()  


if(__name__=="__main__"):
    while True:
        main()