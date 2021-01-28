#Last login: Thu Jan 21 11:14:51 on ttys002
#(base) nithinvenkat@student-10-201-23-058 ~ % ipython
#Python 3.7.6 (default, Jan  8 2020, 13:42:34)
#Type 'copyright', 'credits' or 'license' for more information
#IPython 7.12.0 -- An enhanced Interactive Python. Type '?' for help.

#import
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

#chcek for chrome driver install on every start
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

 # locate email form by_class_name
username = driver.find_element_by_class_name('input__input')

 # send_keys() to simulate key strokes
username.send_keys('username')

 # locate email form by_class_name
password = driver.find_element_by_id('session_password')

 # send_keys() to simulate key strokes
password.send_keys('password')
#
 # locate submit button by_class_name
log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')

 # .click() to mimic button click
log_in_button.click()

#redirect to the desired linkedin profile
driver.get('required profile URL')

# get the image source
img = driver.find_element_by_xpath('//*[@id="ember59"]')

#get the source URL element of the image
src = img.get_attribute('src')

# download the image//*[@id="ember59"]
url = driver.find_element_by_id("ember59").get_attribute("src")

#sacve it to local folder
urllib.request.urlretrieve(src, "linkedIn_picture.jpeg")

#once done. close the script
driver.close()


