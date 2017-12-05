import tweepy
import json
from firebase import firebase
from time import sleep
from datetime import timezone, datetime

with open('.configs.json') as json_data_file:
    configs = json.load(json_data_file)


# MODIFY THIS
city = "Calgary"
granularity = "city"  # Can be country if you want to pull all the data from a country

auth = tweepy.OAuthHandler(configs['c_key'], configs['c_sec'])
auth.set_access_token(configs['a_token'], configs['a_sec'])


api = tweepy.API(auth, wait_on_rate_limit=True)
places = api.geo_search(query=city, granularity=granularity)
place_id = places[0].id
minLen = 70  # Only include tweets with text length greater than minLen
pull_interval = 0.5 # Pull tweets every 5 seconds

firebase = firebase.FirebaseApplication(configs['firebase_url'], None)

time_counter = 0
log_duration = pull_interval * 10


def save_to_cloud(data_to_save, time_path):
    if configs['firebase_url'].endswith(('/')):
        firebase.post('tweets/' + city + time_path, data_to_save)
    else:
        firebase.post('/tweets/' + city + time_path, data_to_save)


# This is contains the information to get from twitter
# For more information about what information you can get, see
# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
def make_json(tweet_object):
    item = []
    if len(tweet_object.text) >= minLen:
        item = ({
            "date": str(tweet_object.created_at),
            "tweet": tweet_object.text,
            "username": tweet_object.user.screen_name,
            "name": tweet_object.user.name,
            "coordinates": tweet_object.coordinates,
            "place": str(tweet_object.place),
            "user_desc": tweet_object.user.description,
            "location": tweet_object.user.location,
            "followers": tweet_object.user.followers_count,
            "verified": tweet_object.user.verified,
            "where": city})
        return item
    return item


# This is a continuous stream of new tweets in a given location
for tweet in tweepy.Cursor(api.search,
                           q="place:%s" % place_id,
                           count=100,
                           rpp=1000,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
    made_json = make_json(tweet);
    if "date" in made_json:
        ts = made_json['date']
        f = '%Y-%m-%d %H:%M:%S'
        # Save each tweet by hour and by day
        time_path = datetime.strptime(ts, f).replace(tzinfo=timezone.utc).astimezone(tz=None)
        time_path = time_path.strftime('/' + "%Y-%m-%d") + '/' + time_path.strftime("%H")
        save_to_cloud(made_json, time_path)
        sleep(pull_interval)  # Time in seconds.
        time_counter += pull_interval
    if time_counter >= log_duration:
        print("Success: " + str(datetime.now()))
        time_counter = 0

