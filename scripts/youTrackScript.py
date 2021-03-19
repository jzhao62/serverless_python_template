from youtrack.connection import Connection as YouTrack

import os

token = os.environ['YOUTRACK_TOKEN']

print(token)

yt = YouTrack('https://jingyi.myjetbrains.com/youtrack',
              token=token)

yt.getIssue('FEJIS-4')
