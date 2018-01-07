import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./assets/chromedriver')

class InstagramBot:

    def login_user(self, insta_username, insta_password):
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
    
    def find_user(self, user_1):
        """Finds a user and navigates to their profile""" 
        # let the elements load on the page
        time.sleep(3)
        
        user_input_field = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
        )
        # user_input_field.click()
        time.sleep(3)
        user_input_field.send_keys(user_1)
        time.sleep(3)
        user_to_click = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]'
        )
        user_to_click.click()
    
    def like_posts_of_user_followings(self, amount_of_followers, posts_to_like):
        """Obtains a list of followings from user and likes their posts"""
        # let the elements load on the page
        time.sleep(3)
        follower_list = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/header/section/ul/li[2]/a'
        )
        follower_list.click()
        time.sleep(3)

        # find the followers modal
        followers_modal = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]")

        # scroll x number of times inside the modal to load the users
        for i in range(int(10)):
            driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", followers_modal)
            time.sleep(1)



