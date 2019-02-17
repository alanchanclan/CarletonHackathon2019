from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, os
from time import sleep

class searcher():
    """
    Google reverse image search bot
    Dependincies:
        - Selenium
        - Chrome Webdriver
    """

    def __init__(self, image_dir):
        self.image_dir = image_dir
        if 'linux' in sys.platform:
             os.chdir('../webdriver/linux')
        elif 'win' in sys.platform:
             os.chdir('../webdriver/win')
        elif 'darwin' in sys.platform:
             os.chdir('../webdriver/mac')

        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)


    def __del__(self):
        self.driver.close()

    def __open_image_dialog(self):
        self.driver.get("https://www.google.com/imghp?hl=EN")
        cam_button = self.driver.find_elements_by_xpath("//div[@aria-label=\"Search by image\" and @role=\"button\"]")[0]
        cam_button.click()
        upload_image = self.driver.find_elements_by_xpath("//div[@class=\"qbtbha sl\"]")[0]
        upload_image.click()
        self.upload_dialog = self.driver.find_elements_by_xpath("//input[@id=\"qbfile\" and @name=\"encoded_image\"]")[0]


    def text(self):
        return self.driver.text

    def upload_image(self,path):
        try:
            self.upload_dialog
        except:
            self.__open_image_dialog()
        self.upload_dialog.send_keys(self.image_dir+"\\"+path)
        sleep(10)


s = searcher("C:\\Users\\geren\\Desktop\\CarletonHackathon2019\\CarletonHackathon2019\\images_backend")
s.upload_image('bottle.bmp')
