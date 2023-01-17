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




gmail = []
sifre=[]
liste=[]
i=0
#okuma
with open("account.txt", "r",encoding="utf-8") as f:
  contents = f.read().split("\n")
  for content in contents:
    if not content == "":
      if (contents.index(content)%2) == 0:
        #print(f"Link: {content}")
        gmail.append(content)
      else:
        #print(f"{i}   Link: {content}")
        i=i+1
        sifre.append(content)

#yazma
def yazma():
  f = open("KuponYazma.txt", "a")
  f.writelines("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
  f.writelines(f"Mail =   {gmail[sayac1]}\n")
  f.writelines(f"Şifre=   {sifre[sayac1]}\n")
  f.writelines(f"{liste}\n")#bunu her 5 de bir yap yani liste[0,1,2,3,4]
  liste.pop()

print(len(gmail))
print(len(sifre))
sayac1=0

def main():
  sayac2=0
  driver=webdriver.Chrome()
  driver.get("https://www.yemeksepeti.com/login/new?step=email")
  time.sleep(3)
  driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(gmail[sayac2])
  time.sleep(3)
  driver.find_element(By.XPATH,'//*[@id="login-page-react-root"]/main/div/form/div[3]/button').click()
  time.sleep(5)
  driver.find_element(By. XPATH,'//*[@id="password"]').send_keys(sifre[sayac2])
  time.sleep(3)
  driver.find_element(By.XPATH,'//*[@id="login-page-react-root"]/main/div/form/div[4]/button').click()
  time.sleep(5)
  driver.get("https://www.yemeksepeti.com/vouchers")
  time.sleep(5)
  labels= driver.find_elements(By.XPATH,'//*[@id="voucher-wallet-react-root"]/div/div/div[2]/ul/li/div')
  for label in labels:
        print(label.text)
        liste.append(label.text)
  print(liste)
  yazma()
  time.sleep(5)
  sayac2=sayac2+1

if(__name__=="__main__"):
    while True:
        main()