from InstagramBot import InstagramBot

# login credentials
insta_username = ''
insta_password = ''

# usernames to interact with
user_1 = ''

# -------------------------------------
# like posts of user followings
# -------------------------------------

# amount of followers to interact with per user
amount_of_followers = 100

# amount of posts to like per follower
posts_to_like = 3

#

session = InstagramBot()
session.login_user(insta_username=insta_username, insta_password=insta_password)
session.find_user(user_1=user_1)
session.like_posts_of_user_followings(
    amount_of_followers=amount_of_followers,
    posts_to_like=posts_to_like
    )