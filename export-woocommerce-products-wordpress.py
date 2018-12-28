# Author: Ron Aduna
# Date: 12/27/18
# Licence: MIT
# Tags: Selenium, Chrome, Wordpress, Woocommerce, Export, Products 
# Requires at least: Wordpress 3.0.1
# Tested up to: Wordpress 5.0.2
# Requires: Python 3.7.1, Selenium 1.22, Chromedriver 2.24.1
# Donate link: https://www.paypal.me/ronaduna

from selenium import webdriver
import selenium
# Using Chrome to access web
driver = webdriver.Chrome()
# Your Wordpress website admin URL 
driver.get('https://yourwordpresssite.com/wp-admin')

# Find generate button (uncomment next line if jetpack login is enabled)
# generate_button = driver.find_element_by_xpath("//a [@class='jetpack-sso-toggle wpcom']")
# Click generate button (uncomment next line if jetpack login is enabled)
# generate_button.click()

# Select the id box
id_box = driver.find_element_by_id('user_login')
# Make python type your username 
id_box.send_keys('your-user-name')

# Find password box
pass_box = driver.find_element_by_id('user_pass')
# Make python type your password
pass_box.send_keys('your-password')

# Find login button
login_button = driver.find_element_by_id('wp-submit')
# Click login
login_button.click()

# Find product
product_button = driver.find_element_by_id('menu-posts-product')
# Click product
product_button.click()

# Find export
export_button = driver.find_element_by_partial_link_text('Export')
# Click export
export_button.click()

# Find generate button
generate_button = driver.find_element_by_xpath("//button [@type='submit' and @value='Generate CSV']")
# Click generate button
generate_button.click()

# These should initiate the download. The downloaded file should be on your downloads folder.