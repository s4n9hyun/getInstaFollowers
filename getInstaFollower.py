# Importing Libraries
import instaloader
import pandas as pd

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
bot.login(user="dawara0058@gmail.com", passwd="kjin1203")
NAME = "hufs_chinese"
# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, NAME)

# Retrieving the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]

# Converting the data to a DataFrame
followers_df = pd.DataFrame(followers)

# Storing the results in a CSV file
followers_df.to_csv(NAME+'.csv', index=False, encoding='UTF8')
