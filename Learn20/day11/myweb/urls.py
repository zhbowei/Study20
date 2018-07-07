#__author:  bwzhang
#__date:    2018/7/7
from Learn20.day11.myweb.server3 import current_time
def routers():
    urlpatterns = (
        ("/current_time",current_time),

    )
    return urlpatterns
