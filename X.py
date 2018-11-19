from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\adarb\\Documents\\devops\\chromedriver.exe")
driver.get("https://translate.google.com/")
driver.implicitly_wait(10)

print (driver.current_url)
print(driver.title)
print(driver.page_source)
driver.find_element_by_id("gt-submit")
my_list = driver.find_elements_by_id("gt-submit")
my_list[0].click()
x = driver.find_element_by_id("source")
x.send_keys("Hello");
time.sleep(4)
z = driver.find_element_by_id("source")
print(z.get_attribute("value"))
driver.refresh()
driver.quit()