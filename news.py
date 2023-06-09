import requests
import json
import os
import _G
from datetime import datetime
import utils

PREV_NEWS_FILE = '.prevnews.json'

NEWS_URL    = os.getenv('NEWS_URL')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

def get_webhook_url():
    global WEBHOOK_URL
    return WEBHOOK_URL

def get_old_news():
    ret = {}
    if not os.path.exists(PREV_NEWS_FILE):
        ret = requests.get(NEWS_URL).json()['newsList']
        ret = sorted(ret, key=lambda o: -o['id'])
        with open(PREV_NEWS_FILE, 'w') as fp:
            json.dump(ret, fp)
    else:
        with open(PREV_NEWS_FILE, 'r') as fp:
            ret = json.load(fp)
    return ret


def update():
    news = {}
    try:
        news = requests.get(NEWS_URL).json()['newsList']
        news = sorted(news, key=lambda o: -o['id'])
    except Exception as err:
        utils.handle_exception(err)
        return
    olds = get_old_news()
    o_cksum = int(datetime.fromisoformat(olds[0]['postedAt']).timestamp())
    n_cksum = int(datetime.fromisoformat(news[0]['postedAt']).timestamp())
    if o_cksum > n_cksum:
        _G.log_warning(f"Old news newer than latest news ({o_cksum} > {n_cksum})")
    elif o_cksum == n_cksum:
        _G.log_info("No news, skip")
        return

    _G.log_info("Gathering news")
    ar = []
    for n in news:
        if n['id'] > olds[0]['id']:
            ar.append(n)
        else:
            break
    for a in ar:
        try:
            send_message(a)
        except Exception as err:
            utils.handle_exception(err)
    with open(PREV_NEWS_FILE, 'w') as fp:
        json.dump(news, fp)


def send_message(obj):
    payload = {}
    payload['embeds'] = [{
        'author': {
            'name': _G.VOCAB_JP['NEWS_TAG'][obj['tag']],
            'icon_url': _G.NEWS_ICON[obj['tag']],
        },
        'title': f"**{obj['title']}**",
        'description': f"<t:{int(datetime.fromisoformat(obj['postedAt']).timestamp())}>",
        'color': _G.NEWS_COLOR[obj['tag']],
        'fields': []
    }]
    # this will fail if total length is over 6000
    for msg in utils.chunk(obj['message'], 1000):
        payload['embeds'][0]['fields'].append({
            'name': " \u200b", # zero-width space
            'value': msg
        })
    return requests.post(get_webhook_url(), json=payload)