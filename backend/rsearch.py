# fixed by Allen Tao

from selenium import webdriver
import os
import time

# Using Chrome to access web

# change this link accordingly to where you installed your chrome driver dependency
chromedriver = r"C:\Users\Admin\Documents\Allen\CBSS\Grade 11 IB\SET_application\CarletonHackathon2019\webdriver\win\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

try:
    # Open the website
    driver.get('https://images.google.com/')

    # Find cam button
    cam_button = driver.find_elements_by_xpath("//div[@aria-label=\"Search by image\" and @role=\"button\"]")[0]
    cam_button.click()

    # Find upload tab
    upload_tab = driver.find_elements_by_xpath("//*[contains(text(), 'Upload an image')]")[0]
    upload_tab.click()

    # Find image input
    upload_btn = driver.find_element_by_name('encoded_image')
    os.chdir("../images_backend")
    upload_btn.send_keys(os.getcwd()+"/buyme.jpg")

    time.sleep(5)

    # Go to shopping tab
    shoppingButton = driver.find_element_by_link_text("Shopping")
    shoppingButton.click()
    time.sleep(2)

    # Go to sort by
    sortButton = driver.find_element_by_class_name("vkYnff")
    sortButton.click()
    time.sleep(2)

    time.sleep(100000) # let the user browse thru
    

except Exception as e:
    print(e)

driver.quit()
