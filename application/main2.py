from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random



driver = webdriver.Chrome()
vars = {}
  
  
driver.quit()
  
driver.get("https://wikiroulette.co/")

vars["input_title"] = "WikiRoulette — Random Wikipedia Pages"
   
vars["str_titre"] = driver.title

assert(vars["str_titre"] == "vars[input_title]")

print("{}".format(vars["input_title"]))
print("Bonjour je suis un message")



# driver = webdriver.Chrome()

# driver.get("https://www.reddit.com/")

# # if(random.choice([True, False])):
# #     driver.set_window_size(1600,1200)
# # else:
# #     driver.set_window_size(800,600)

# driver.set_window_size(1600,1200)

# button = driver.find_elements(by=By.LINK_TEXT, value="Se connecter")
# button2 = driver.find_elements(by=By.XPATH, value="//a[contains(text(),'S’inscrire')]")

# if button:
#     button[0].click()
#     print("click")
# else:
#     print("il n'y a pas de bouton")

# if button2:
#     button2[0].click()
#     print("click sur le bouton 2")
# else:
#     print("il n'y a pas de bouton 2")


# time.sleep(500)
# driver.close()