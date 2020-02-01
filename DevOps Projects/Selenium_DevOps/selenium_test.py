from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="/home/shadibdair/Desktop/chromedriver")
# driver.get('https://translate.google.com')
# print(driver.current_url)
# driver.implicitly_wait(5)
# print(driver.title)
# driver.implicitly_wait(8)
# #print(driver.page_source)
# # driver.find_element_by_name("name")
# # driver.find_element_by_id("name_id")
# # driver.find_element_by_class_name("gb_ma")
# driver.find_element_by_id("source").send_keys(Keys.ENTER)
# # elements = driver.find_elements_by_id("source")
# # print(len(elements))
# # driver.find_element_by_xpath('//input[@type="asdas"]')
# # driver.quit()  #Quit from website.
#
# source_elements = driver.find_element_by_id("source")
# if source_elements.is_enabled():
#     source_elements.send_keys("shadi")
#     source_elements.clear()
#     source_elements.send_keys("the")
#     source_elements.clear()
#     source_elements.send_keys("best")
#     source_elements.clear()
#
#
# print(source_elements.get_attribute("rows"))
#

driver = webdriver.Chrome(executable_path="/home/shadibdair/Desktop/chromedriver")
driver.get('https://gofile.io/?t=uploadFiles')

driver.find_element_by_id("btnChooseFiles").send_keys()

# btnChooseFiles