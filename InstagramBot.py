import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

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
        # if there is a mobile field, we know we are on the sign up page
        mobile_field = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/input[@placeholder="Mobile Number or Email"]'
        )
        switch_to_login_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a'
        )
        if mobile_field is not None:
            print("switching from sign-up page to login page")
            ActionChains(driver).move_to_element(switch_to_login_button).click().perform()
        
        # if already on sign-up page, login
        username_field = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[1]/div/input[@name="username"]'
        )
        password_field = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/input'
        )
        login_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button'
        )
        if username_field is not None:
            print("logging user credentials...")
            username_field.send_keys(insta_username)
            password_field.send_keys(insta_password)
            login_button.click()

session = InstagramBot()
session.login_user()
