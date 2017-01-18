from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from sys import argv

def main():
    url = 'https://vahan.nic.in/nrservices/faces/user/jsp/SearchStatus.jsp'
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)

    assert "National" in driver.title

    v1 = '__First-Six-alphanumeric-elements-of-number-plate'
    v2 = '__Last-4-numeric-elements-of-number-plate'


    Vehicle_1 = driver.find_element_by_id('vehiclesearchstatus:regn_no1_exact')
    Vehicle_2 = driver.find_element_by_id('vehiclesearchstatus:regn_no2_exact')

    Vehicle_1.send_keys(v1)
    Vehicle_2.send_keys(v2)

    Vehicle_2.send_keys(Keys.ENTER)

    tag = driver.find_element_by_id('vehiclesearchstatus:msg').text
    print tag
    driver.close()



main()