from selenium import webdriver

chrome_driver_path = "C:\Developer\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# docs = driver.find_element_by_css_selector(".documentation-widget a")
# print(docs.text)

# application = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[1]/div[3]/h2"')
# print(application.text)

menu_list = driver.find_elements_by_css_selector(".event-widget time")
# for list in menu_list:
#     print(list.text)
menu_names = driver.find_elements_by_css_selector(".event-widget li a")
# for name in menu_names:
#     print(name.text)
events = {}
for n in range(len(menu_list)):
    events[n] = {
        "time": menu_list[n].text,
        "name": menu_names[n].text,
    }

print(events)
driver.close()

