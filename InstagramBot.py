import time
import math
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./assets/chromedriver')

class InstagramBot:
    """An bot which crawls instagram and interacts with users"""

    def __init__(self, insta_username=None, insta_password=None, nogui=False):
        if nogui:
            self.display = Display(visible=0, size=(800, 600))
            self.display.start()

        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--lang=en-US')
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US'})
        
        if not insta_username or insta_password:
            print('Please provide Username and Password')
        
        self.insta_username = insta_username
        self.insta_password = insta_password
        self.nogui = nogui
            
    def login_user(self):
        """Logins the user with the given username and password""" 
        print('Logging in the user...')
        driver.get('http://www.instagram.com');
        time.sleep(3) # Let the user actually see something!

        # if on sign up page, switch to login
        # if there is a mobile field, we know we are on the sign up page
        mobile_field = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/div[1]/input[@name="emailOrPhone"]'
        )
        switch_to_login_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a'
        )
        if mobile_field is not None:
            print("switching from sign-up page to login page")
            ActionChains(driver).move_to_element(switch_to_login_button).click().perform()
        
        # if already on sign-up page, login
        username_field = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[1]/div/div[1]/input[@name="username"]'
        )
        password_field = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/div[1]/input[@name="password"]'
        )
        login_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button'
        )
        if username_field is not None:
            print("Entering user credentials...")
            username_field.send_keys(self.insta_username)
            password_field.send_keys(self.insta_password)
            login_button.click()
        
        print("User logged in!")
    
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
        # there are 9 users displayed by default
        # scroll: amount of followers to interact with / 9 +1 (to round up and avoid bugs)
        print("Fetching followers of user")
        for i in range(int(math.ceil(amount_of_followers/9)+1)):
            driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", followers_modal)
            time.sleep(1)
        
        # iterate over every user and store their url into an array
        account_list = []
        for i in range (amount_of_followers):
            xpath = "/html/body/div[4]/div/div[2]/div/div[2]/ul/div/li["
            xpath += str(i+1) # +1 because index of a tags start at 1
            xpath += "]/div/div[1]/a"
            user = driver.find_element_by_xpath(xpath)
            user_url = user.get_attribute('href')
            account_list.append(user_url)
        
        # iterate over each user and like their posts
        for account in account_list:
            driver.get(account);
            time.sleep(3)

            # for each user, store the amount of posts to like in an array
            posts_array = []
            for i in range (posts_to_like):
                image_xpath = '//*[@id="react-root"]/section/main/article/div/div[1]/div[1]/div['
                image_xpath += str(i+1) # +1 because index of tags start at 1
                image_xpath += ']/a'
                image = driver.find_element_by_xpath(image_xpath)
                image_url = image.get_attribute('href')
                posts_array.append(image_url)
            
            print(posts_array)
            
            # iterate over each post to like, and like it
            for post in posts_array:
                driver.get(post)
                time.sleep(3)
                like_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/a')
                like_button.click()
                print("post liked!")



