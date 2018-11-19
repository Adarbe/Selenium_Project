from selenium import webdriver
import time
import re
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'seleniumproject.txt')

with open(filename) as file:
   for line in file:
        buy_me = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)

#Opening chrome browser on a desired page
browser = os.path.join(dirname, 'chromedriver.exe')
driver = webdriver.Chrome(executable_path=browser)
driver.maximize_window()

#Getting browser current page URL
driver.get(buy_me[0])
driver.implicitly_wait(10)

#Press on login / regestration button
driver.find_element_by_xpath("//span[@class='seperator-link']").click()

#Press registration
driver.find_element_by_xpath("//span[@class='text-btn']").click()

#Enter first name
driver.find_element_by_id("ember973").send_keys("Adar")

#Enter email
driver.find_element_by_id("ember975").send_keys("adarzag@gmail.com")

#Enter password
driver.find_element_by_id("valPass").send_keys("Aa123456")

#Verify password
driver.find_element_by_id("ember979").send_keys("Aa123456")

#Agree to roles
driver.find_element_by_class_name("fa ").click()

#Register
driver.find_element_by_css_selector("button[type = 'submit'").click()
time.sleep(3)

#Pick a price point
driver.find_element_by_xpath("//*[contains(text(),'סכום')]").click()
driver.find_element_by_xpath("//*[contains(text(),'עד 99')]").click()
time.sleep(2)

#Pick the area
driver.find_element_by_xpath("//*[contains(text(),'אזור')]").click()
driver.find_element_by_xpath("//*[contains(text(),'מרכז')]").click()

#Pick category
driver.find_element_by_xpath("//*[contains(text(),'קטגוריה')]").click()
driver.find_element_by_xpath("//*[contains(text(),'גיפט קארד לבריאות')]").click()

#Press the search button
driver.find_element_by_id("ember709").click()
time.sleep(2)

#Pick a Buisness
pick_buisness = driver.find_elements_by_class_name("card-item")
pick_buisness[1].click()

#Type a price
choose_price = driver.find_element_by_class_name("input-cash")
choose_price.send_keys("99")
time.sleep(2)

#Choose and continue
driver.find_element_by_xpath("//*[contains(text(),'לבחירה')]").click()
time.sleep(2)

#Press radio button from whom
send_to = driver.find_elements_by_class_name("circle")
send_to[0].click()

#Enter receiver name
reciver_name = driver.find_elements_by_class_name("ember-text-field")
reciver_name[2].clear()
reciver_name[2].send_keys("Shay Benjamin")

#Choose occasion
driver.find_element_by_xpath("//*[contains(text(),'לאיזה אירוע?')]").click()
event = driver.find_elements_by_class_name("active-result")
event[4].click()

occasion = driver.find_element_by_tag_name("textarea")
occasion.clear()
occasion.send_keys("לעוד הרבה שנים של אהבה ואושר")

#Upload a picture
pic = os.path.join(dirname, 'us.jpg')
driver.find_element_by_name("fileUpload").send_keys(pic)

#Press radio button "מיד אחרי התשלום"
driver.find_element_by_class_name("send-now").click()

#How to send by email or SMS
how_to_send = driver.find_elements_by_class_name("btn-text")
how_to_send[1].click()

#Enter email address
enter_email = driver.find_elements_by_class_name("ember-text-field")
enter_email[5].clear()
enter_email[5].send_keys("shay.benjamin1983@gmail.com")
driver.find_element_by_class_name("btn-save").click()

#Submit
submit = driver.find_elements_by_class_name("btn-theme")
submit[2].click()
time.sleep(5)

#Quit browser
driver.quit()




