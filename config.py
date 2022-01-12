from modules import *

SESSION_NAME = 'session'

API_ID = 1890553
API_HASH = 'c6f46b5330f5953e5201c3185337ed73'

# https://developer.brawlstars.com/
BRAWLSTARS_TOKEN = '298PJL20'

# http://www.last.fm/api/account/create
LASTFM_KEY = '50c4da48aa16885c9e91a6d417d601e7'  # usable example key
LASTFM_USERNAME = ''  # enter your last.fm username

MODULES = {
    # Current time
    'time': Time('%H:%M'),

    # Number of blocked accounts
    #'blocked': BlockedCount(),


    # BrawlStars Trophies by tag
    #'trophies': BrawlStarsTrophies('298PJL20', BRAWLSTARS_TOKEN),

}

INTERVAL = 60

TEMPLATES = {
    'about': '⌛: $time'
}
