from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import pandas as pd
from collections import OrderedDict
from datetime import date

today = str(date.today())
date = today.split(",")
month = date[0].split("-")
monthdict = {
	"1":"Jan",
	"2":"Feb",
	"3":"March",
	"4":"April",
	"5":"May",
	"6":"June",
	"7":"July",
	"8":"August",
	"9":"Sep",
	"10":"Oct",
	"11":"Nov",
	"12":"Dec"
}

for x,y in monthdict.items():
	if (x == month[1]):
		monthChar = y


print(monthChar + " 30, " + month[0])

pd.set_option('display.max_colwidth', 1000)
df = pd.read_csv("CheckSammy_WorkOrder.csv")

address1 = str(df.loc[5])
address2 = str(df.loc[6])
phone = str(df.loc[7])
name = str(df.loc[16])
service = str(df.loc[22])



namesplit = name.split("          ")
finalName = namesplit[1].split(", ")
lastName = finalName[1].split("-")
print(finalName[0])
print(lastName[0])
phoneSplit = phone.split("+")
finalPhone = phoneSplit[1].split(" ")
print(finalPhone[0]+finalPhone[1]+finalPhone[2]+finalPhone[3])
tempAddress1 = address1.split("Location: ")
finalAddress1 = tempAddress1[1].split("\nName:")
print(finalAddress1[0])
tempAddress2 = address2.split("Summary    ")
finalAddress2 = tempAddress2[1].split("\nName:")
city = finalAddress2[0].split(" ")
print(city[0])
print(city[1])
print(city[2])
item = service.split()
print(item[3])
print(item[5])

DRIVER_PATH = "/home/lcldawg/Documents/selenium/chromedriver"

options = Options()
options.headless = True
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(executable_path=DRIVER_PATH)


driver.get("https://secure.getjobber.com")
driver.get("https://secure.getjobber.com/login")

driver.find_element_by_xpath("//*[@id='email']").send_keys("alex@checksammy.com")
driver.find_element_by_xpath("//*[@id='user_session_password']").send_keys("jal561234")
driver.find_element_by_xpath("//*[@id='login_form']/input[4]").click()

WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='controls']")))

driver.get("https://secure.getjobber.com/invoices?utf8=%E2%9C%93&search=waste%20management&start_at_filter=" + monthChar + "%2001%2C%202020&end_at_filter=" + monthChar + "%2030%2C%20202")
a = driver.find_element_by_class_name("u-marginBottomSmallest").get_attribute('innerHTML')
for x in a:
	print(x)


'''	
driver.get("https://secure.getjobber.com/clients/new")

WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='client_first_name']")))

driver.find_element_by_xpath("//*[@id='client_first_name']").send_keys(finalName[0]);
driver.find_element_by_xpath("//*[@id='client_last_name']").send_keys(lastName[0]);
driver.find_element_by_xpath("//*[@id='client_company_name']").send_keys("Waste Management");
driver.find_element_by_xpath("//*[@id='new_client']/div/div/div/div[1]/div[1]/div[2]/label/div[2]/label/sg-icon").click()
driver.find_element_by_xpath("//*[@id='client_phones']/li/div/div[2]/div[1]/div/div[2]/div/div[1]/placeholder-field/input").send_keys(finalPhone[0]+finalPhone[1]+finalPhone[2]+finalPhone[3]);
driver.find_element_by_xpath("//*[@id='new_client']/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/div/placeholder-field/input").send_keys(finalAddress1[0]);
driver.find_element_by_xpath("//*[@id='new_client']/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/div[3]/div[1]/placeholder-field/input").send_keys(city[0]);
driver.find_element_by_xpath("//*[@id='new_client']/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/div[3]/div[2]/placeholder-field/input").send_keys(city[1]);
driver.find_element_by_xpath("//*[@id='new_client']/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/div[4]/div[1]/placeholder-field/input").send_keys(city[2]);
driver.find_element_by_xpath("//*[@id='new_client']/div/div/div/div[1]/div[2]/div[4]/div/div[1]/label/sg-icon").click();
driver.find_element_by_xpath("//*[@id='client_billing_address1']").send_keys("415 Day Hill Road");
driver.find_element_by_xpath("//*[@id='client_billing_city']").send_keys("Windsor");
driver.find_element_by_xpath("//*[@id='client_billing_province']").send_keys("CT");
driver.find_element_by_xpath("//*[@id='client_billing_postal_code']").send_keys("06095");
driver.find_element_by_xpath("//*[@id='new_client']/div/div/div/div[2]/div[2]/div/button[1]").click();



WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='new_client']/input[246]")))
driver.find_element_by_xpath("//*[@id='new_client']/input[246]").click();

WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='controls']/div/div/div[3]/div/button")))
driver.find_element_by_xpath("//*[@id='controls']/div/div/div[3]/div/button").click();
WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='controls']/div/div/div[3]/div/div[1]/nav/div[1]/a[4]")))
driver.find_element_by_xpath("//*[@id='controls']/div/div/div[3]/div/div[1]/nav/div[1]/a[4]").click();

driver.find_element_by_xpath("//*[@id='new_invoice']/div/div[1]/div/div[1]/div/div[3]/div[2]/div/ul/li[2]/div/div[2]/div[1]/span").click()
driver.find_element_by_xpath("//*[@id='invoice_invoice_net']").send_keys("Custom")
driver.find_element_by_xpath("//*[@id='invoice_due_date']").click()


driver.find_element_by_xpath("//*[@id='invoice_due_date']").send_keys(monthChar + "30," + month[0])

driver.find_element_by_xpath("//*[@id='invoice_line_items_attributes_0_name']").send_keys("WM - Multi-Family Junk Removal - Full Truck");
driver.find_element_by_xpath("//*[@id='invoice_line_items_attributes_0_name']").click()
driver.find_element_by_xpath("//*[@id='invoice_line_items_attributes_0_name']").send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath("//*[@id='invoice_line_items_attributes_0_name']").send_keys(Keys.ENTER)

driver.find_element_by_xpath("//*[@id='new_invoice']/div/div[1]/div/div[2]/div[5]/div[2]/div/button").click()
'''