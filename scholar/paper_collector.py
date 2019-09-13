from selenium import webdriver
import time


google='https://scholar.google.com/citations?user=NDrCCokAAAAJ&hl=en'
driver=webdriver.Firefox()
driver.get(google)
driver.implicitly_wait(10)
#click showmore
path = "//button[@class='gs_btnPD gs_in_ib gs_btn_flat gs_btn_lrge gs_btn_lsu']"
button = driver.find_element_by_xpath(path)
#click several times
button.click()
button.click()
button.click()
path = "//a[@class='gsc_a_at']"
urls = []
buttons = driver.find_elements_by_xpath(path)
#click each one
for button in buttons:
    button.click()
    urls.append(driver.current_url)
    driver.back()
    time.sleep(2)
print(urls)

