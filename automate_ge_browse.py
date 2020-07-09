"""Automate Google Earth Browsing
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Edge(r"C:\Users\tjosh\Downloads\edgedriver_win64\msedgedriver")


# using google earth
# driver.get(
#     "https://earth.google.com/web/@0,0,-24018.82718741a,36750128.22569847d,35y,0h,0t,0r/data=KAE"
# )


# using google maps
# driver.get("https://www.google.com/maps/")
driver.get("https://www.google.com/maps/@35.6855862,139.7422207,159m")
sleep(3)

driver.maximize_window()
sleep(1)

# disable login
driver.find_element_by_xpath(
    "/html/body/jsl/div[3]/div[9]/div[9]/div/div/div/div[1]/div[3]/div/div/div[2]/div/a[1]"
).click()
sleep(1)

# change to satellite view
satellite_widget = driver.find_element_by_xpath(
    "/html/body/jsl/div[3]/div[9]/div[23]/div[4]/div/div[2]/button"
)
satellite_widget.click()
sleep(1)
search_box = driver.find_element_by_id("searchboxinput")
search_box.send_keys("34.688,137.478")
search_box.send_keys(Keys.ENTER)
sleep(2)

# save screenshot
import time

begin = time.time()
driver.save_screenshot("page.png")
print("Duration: ", time.time() - begin)


# we can loop something here
for i in range(10):
    search_box.send_keys(Keys.CONTROL + "a")
    search_box.send_keys(Keys.DELETE)
    search_box.send_keys("34.688,137.478")
    search_box.send_keys(Keys.ENTER)
    sleep(2)


# driver.find_element_by_class_name("earth-gm2-icon-button")
# driver.find_element_by_link_text("Search")
# search_btn = driver.find_element_by_id("search")
# search_bar = driver.find_element_by_id("omniboxInput")

# # import enterkey

# from selenium.webdriver.common.keys import keys

# # press enter
# search_bar.send_keys(keys.ENTER)

# search_bar = driver.find_element_by_xpath('//input[@id="omniboxInput"]')

# /html/body/earth-app//paper-drawer-panel/div/earth-toolbar//earth-gm2-icon-button[2]

# driver.find_elements_by_css_selector()
# driver.find_elements_by_tag_name("earth-gm2-icon-button")
