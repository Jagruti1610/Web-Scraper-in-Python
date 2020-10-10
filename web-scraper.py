from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions  
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd


driver = webdriver.Chrome("c:\\data\\chromedriver\\chromedriver.exe")
driver.get("https://google.com/")


elem = driver.find_element(By.NAME, "q")
elem.clear()     
elem.send_keys("food")

elem.send_keys(Keys.RETURN)

try:
	elem.submit()
except exceptions.StaleElementReferenceException as e:
	print("exception 1: ", e)
	pass

href_list = []  # collecting all the data in a Python list


try:	

	results = driver.find_elements_by_xpath("//a[@href]")
	
	for result in results:		
		try:
			# print(result.get_attribute("href"))
			href_list.append(result.get_attribute("href"))			
		except exceptions.StaleElementReferenceException as e:
			print("exception 2: ", e)
			pass

	pd.DataFrame({'Links': href_list}).to_excel('c:\\users\\admin\\documents\\test\\data.xlsx', sheet_name='sheet1', index=False)

	

except exceptions.TimeoutException as e:
	print("exception 3: ", e)
	pass

finally:
    driver.quit()
