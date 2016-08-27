import twitter

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN_KEY = ""
ACCESS_TOKEN_SECRET = ""

api = twitter.Api(consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET,
                    access_token_key=ACCESS_TOKEN_KEY,
                    access_token_secret=ACCESS_TOKEN_SECRET)

USER_SCREEN_NAME = "StatMLPapers"

#user = api.GetUser(screen_name=USER_SCREEN_NAME)
#print(user.name + " : " + user.description + "\n")

statuses = api.GetUserTimeline(screen_name=USER_SCREEN_NAME)
for s in statuses:
    print(s.created_at, s.text, s.favorite_count, s.retweet_count)

for it in range(0,5):
    print("")
    max_id = statuses[-1].id
    statuses = api.GetUserTimeline(screen_name=USER_SCREEN_NAME, max_id=max_id)

    if len(statuses) == 1:
        break
    else:
        statuses = statuses[1:]

    for s in statuses:
        print(s.created_at, s.text, s.favorite_count, s.retweet_count)
