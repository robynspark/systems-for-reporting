from twython import Twython
import csv

CONSUMER_KEY = 'LaCtdjRH7JNfZYdqwmOdOtDON'
CONSUMER_SECRET = 'GiOjDQXfQIH5mOF5PCjOFExvERNpNZiPkDuL1e1bitFsWobu2J'
ACCESS_TOKEN = '839153726300487681-j6GYhMANoQU3nAkru15PnYqpstP049F'
ACCESS_TOKEN_SECRET = 'YiZttnASdQP6tRE84Xr9h6Na7RFOgUaYF4g9IB7TwDtWW'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='michelle obama', count="100")
tweets = search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('Search Term', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['michelle obama', result['text'].encode('utf-8'), url]]
        a.writerows((text))
