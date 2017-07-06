# coding:utf-8

import json
from feedback import Feedback
import urllib2
import os

USER_DIRS = 'UserImage'

v2exURL = 'http://v2ex.com/api/topics/latest.json'
result = json.load(urllib2.urlopen(v2exURL))
feeds = Feedback()
if not os.path.exists(USER_DIRS):
    os.mkdir(USER_DIRS)
for i in result:
    icon_path = USER_DIRS + '/' + str(i['id']) + '.png'
    if not os.path.exists(icon_path):
        icon_url = 'http:' + i['member']['avatar_large']
        im = urllib2.urlopen(icon_url)
        with open(icon_path, 'w') as f:
            f.write(im.read())
    
    feeds.add_item(title=i['title'], subtitle=i['content'], arg=i['url'], icon=icon_path)

print feeds
