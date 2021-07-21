from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# number = driver.find_element_by_css_selector("#articlecount a")

# # number.click()

# all_portalls = driver.find_element_by_partial_link_text("All portals")
# # all_portalls.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
button = driver.find_element_by_class_name("btn")

first_name.send_keys("wes")
last_name.send_keys("lee")
email.send_keys("wes@lee.com")
button.click()
