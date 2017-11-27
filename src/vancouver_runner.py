import tweepy
import json
from firebase import firebase
from time import sleep
from datetime import timezone, datetime

with open('.configs.json') as json_data_file:
    configs = json.load(json_data_file)

city = "Vancouver"
gran = "city"

auth = tweepy.OAuthHandler(configs[city]['c_key'], configs[city]['c_sec'])
auth.set_access_token(configs[city]['a_token'], configs[city]['a_sec'])


api = tweepy.API(auth)
places = api.geo_search(query=city, granularity=gran)
place_id = places[0].id
minLen = 70 # Only include tweets with text length greater than minLen
interval = 0.5 # Pull tweets every 5 seconds

firebase = firebase.FirebaseApplication(configs[city]['db_url'], None)


def save_to_cloud(t,time_path):
    res = firebase.post('/tweets/' + time_path, t)
    print(res)


def make_json(tweet):
    item = []
    if len(tweet.text) >= minLen:
        item = ({
            "date": str(tweet.created_at),
            "tweet": tweet.text,
            "username": tweet.user.screen_name,
            "name": tweet.user.name,
            "coordinates": tweet.coordinates,
            "place": str(tweet.place),
            "user_desc": tweet.user.description,
            "location": tweet.user.location,
            "followers": tweet.user.followers_count,
            "verified": tweet.user.verified,
            "where": city})
        return item
    return item


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
        timePath = datetime.strptime(ts, f).replace(tzinfo=timezone.utc).astimezone(tz=None)
        timePath = timePath.strftime("%Y-%m-%d") + '/' + timePath.strftime("%H")
        save_to_cloud(made_json, timePath)
        sleep(0.5)  # Time in seconds.
