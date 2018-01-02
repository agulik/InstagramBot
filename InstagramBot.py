import time
from selenium import webdriver

driver = webdriver.Chrome('./assets/chromedriver')
insta_username = ''
insta_password = ''

class InstagramBot():

    def login_user(self):
        """Logins the user with the given username and password""" 
        print('Logging in user...')
        driver.get('http://www.instagram.com');
        time.sleep(5) # Let the user actually see something!

        # if on sign up page, switch to login

        mobile_field = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/input[@placeholder="Mobile Number or Email"]'
        )
        if mobile_field is not None:
            print("you are on the sign-up page")
        # login_box.send_keys(insta_username)
        # search_box.submit()
        # time.sleep(5) # Let the user actually see something!
        # first_result = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div/div[1]/div/header/a')
        # first_result.click()
        # time.sleep(5) # Let the user actually see something!
        # driver.quit()

session = InstagramBot()
session.login_user()
