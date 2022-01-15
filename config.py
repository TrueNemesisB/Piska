from modules import *

SESSION_NAME = 'session'

API_ID = 1890553
API_HASH = 'c6f46b5330f5953e5201c3185337ed73'

# https://developer.brawlstars.com/
BRAWLSTARS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjMxZGY0NThiLWJjYmEtNDk1MS1hMGQ4LTE5ZGI5ODVlNzYwNyIsImlhdCI6MTY0MjI2OTgxNSwic3ViIjoiZGV2ZWxvcGVyLzNlMDYwMjcyLWY2ZmUtMTg2OS1kOWU1LTM0ZTRkMTBmNWVlMyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNjIuMTE4Ljg3LjE5OSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.tNl1EcwMajP0-g7zY8xt8swoum5MEe8HylFRWiHNBZwEZW4mqWApI035QAThzEuBFTqfnMuE_3CSvFISF_QzEw'

# http://www.last.fm/api/account/create
LASTFM_KEY = '50c4da48aa16885c9e91a6d417d601e7'  # usable example key
LASTFM_USERNAME = ''  # enter your last.fm username

MODULES = {
    # Current time
    'time': Time('%H:%M'),

    # Number of blocked accounts
    #'blocked': BlockedCount(),

    # About of the entity
    #'about': EntityInfo('True_Alexey'),

    # Iterates strings
    'first_name': Cycle('АлексейВеликий 💀', 'АлексейНастоящий 💀'), 

    # BrawlStars Trophies by tag
     'trophies': BrawlStarsTrophies('298PJL20' , BRAWLSTARS_TOKEN),

}

INTERVAL = 60

TEMPLATES = {
   'about': 'Я настоящий. ⌛: $time ᅠᅠᅠᅠ BrawlStars🏆: $trophies', 
   'first_name': '$first_name: $time'
} 
