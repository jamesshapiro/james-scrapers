# use instascrape to scrape all posts from an instagram account and download all the photos

import instascrape
import pandas as pd
import time

# get the username of the account you want to scrape
username = 'followthebuti'

# create an instance of the profile scraper
profile = instascrape.Profile(username)

# scrape the profile
profile.scrape()

# get the posts
posts = profile.get_posts()

# create a list to store the posts
post_list = []

# loop through the posts
for post in posts:
    # scrape the post
    post.scrape()
    # get the post's data
    post_data = post.to_dict()
    # add the post's data to the list
    post_list.append(post_data)
    # wait 2 seconds
    time.sleep(2)

# create a dataframe from the list of posts
df = pd.DataFrame(post_list)

# save the dataframe as a json file
df.to_json('instagram_posts.json', orient='records')
with open('instagram_posts.json', 'r') as f:
    data = json.load(f)
    print(data)

# # create an instance of the profile scraper
# profile = instascrape.Profile(username)

# # scrape the profile
# profile.scrape()

# # get the posts
# posts = profile.get_posts()

# # create a list to store the posts
# post_list = []

# # loop through the posts
# for post in posts:
#     # scrape the post
#     post.scrape()
#     # get the post's data
#     post_data = post.to_dict()
#     # add the post's data to the list
#     post_list.append(post_data)
#     # wait 2 seconds
#     time.sleep(2)

# # save the dataframe as a json file
# df.to_json('instagram_posts.json', orient='records')
