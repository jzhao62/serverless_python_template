from youtrack.connection import Connection as YouTrack

from config.settings import YOUTRACK_TOKEN

yt = YouTrack('https://jingyi.myjetbrains.com/youtrack',
              token=YOUTRACK_TOKEN)

issue = yt.getIssue('FEJIS-4')

print(issue)
print(issue)