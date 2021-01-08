from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\Users\Emon\Downloads\Compressed\geckodriver-v0.19.1-win64\geckodriver.exe')

browser.get('https://google.com')

searchElem  = browser.find_element_by_css_selector('#lst-ib')

searchElem.send_keys('selenium python tutorial')
searchElem.submit()

