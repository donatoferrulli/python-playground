from selenium import webdriver

options = webdriver.ChromeOptions()
# background Chrome
# options.add_argument("headless")

chrome_browser = webdriver.Chrome(executable_path='./chromedriver', options= options)
chrome_browser.maximize_window()

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys("I'm Donato")
show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')
assert "I'm Donato" in output_message.text

# using css, get all elements with id get-input with button as a child
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)

# close current Chrome
# chrome_browser.close()

# close all instances
chrome_browser.quit()