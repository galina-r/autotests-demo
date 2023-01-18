from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://www.amazon.com/'
driver = webdriver.Chrome()

driver.get(link)

search__area = driver.find_element_by_id("twotabsearchtextbox")  # locates a search area
search__area.send_keys("brio 33773")  # finds an element

search_submit_button = driver.find_element_by_id(
    "nav-search-submit-button")  # locates and clicks a search_submit_button
search_submit_button.click()

select_item = driver.find_element_by_css_selector(
    "a[href*='brio+33773']").click()  # locates and clicks a link with an item

add_to_cart_button = driver.find_element_by_id("add-to-cart-button").click()  # locates and clicks add_to_cart_button

# locates and clicks proceed_to_checkout_button after waiting up to 5 sec an appearance of a popup window
proceed_to_checkout_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "attach-sidesheet-checkout-button")))
proceed_to_checkout_button.click()




