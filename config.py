from modules import *

SESSION_NAME = 'session'

API_ID = 1890553
API_HASH = 'c6f46b5330f5953e5201c3185337ed73'

# https://developer.brawlstars.com/
BRAWLSTARS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImQzNDNhZjkzLTY3MmEtNGIxZi05ODBhLTFmZGY4OTk3OWYxMyIsImlhdCI6MTY0MjMxMTY2NCwic3ViIjoiZGV2ZWxvcGVyLzNlMDYwMjcyLWY2ZmUtMTg2OS1kOWU1LTM0ZTRkMTBmNWVlMyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMjEzLjg3LjIyNS4xODAiXSwidHlwZSI6ImNsaWVudCJ9XX0.GTBxtMwb5jj1WsFnGtKlmgt_tkP2X0SOjB90hzatI9MnJ3QfsR-1OSdJiDl7x87rPfR99hkPzWIozAYcOvh3wQ'

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
   'about': 'Я настоящий. ⌛: $time ᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠ BrawlStars🏆: $trophies', 
   'first_name': '$first_name: $time'
} 
