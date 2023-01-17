from selenium.webdriver import Chrome, ChromeOptions
import time
ayarlar = ChromeOptions()
ayarlar.add_extension("buster.crx")

tarayici = Chrome(options=ayarlar)
tarayici.get("https://www.yemeksepeti.com/login/new?step=email")
time.sleep(5000000.60)
    
