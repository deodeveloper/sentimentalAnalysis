TRACK_TERMS = "stock"
SEPARATOR = "#"
LANGUAGE = ["en"]
# CONNECTION_STRING = "mysql://root:@localhost/twitter"
#uncomment this for windows machine
#CONNECTION_STRING = "sqlite:///C:/Users/Satya/Documents/GitHub/sentimentalAnalysis/sqllite/samsung.db"
CONNECTION_STRING = "sqlite:////Users/admin/Documents/Development/python/sentimentalAnalysis/outputDir/tweets.db"
CSV_NAME = "tweets.csv"
TABLE_NAME = "tweet"
TWITTER_APP_KEY = "QdjZPGYPwd99r72qQfyZyZEcO"
TWITTER_APP_SECRET = "yUgsvYUSFtNQIEgLW1aY9DMJRRxYajxfYC2pg3RzFhR3rkcl5L"
TWITTER_KEY = "174336590-kvtw1cqrwuH75LIMKqXZkKSeoU9BfEAB9QBnMIoI"
TWITTER_SECRET = "KdnYcVNI0h6ny7i9ACzNw3I0h0hLSlqdjXTSDoYpgDXc5"
try:
    from private import *
except Exception:
    pass