import requests
import time
import json
from datetime import datetime
import logging


cnt=0 
best=10
worst=0
average=0 
total=0
rest_sleep=6
LATENCY="latency"
HEALTHY="healthy"


while True:
    try:
        cnt +=1 
        req = requests.get('http://hello:8080/health')
        req.raise_for_status()
        j = req.json()
        jresponse = json.loads(j)
        if jresponse[HEALTHY] is False:
            logging.warning('Alert not healthy {}'.format(str(datetime.now())))
        total = total + jresponse[LATENCY] 
        if jresponse[LATENCY] <= best:
            best = jresponse[LATENCY]
        if worst < jresponse[LATENCY]:
            worst = jresponse[LATENCY]
        time.sleep(10)
        if cnt == rest_sleep:
            logging.warning("time:{}, best:{}, worst:{}, average:{}".format(str(datetime.now()), best,worst,total/rest_sleep))
            (best, worst, total, cnt) = (10,0,0,0)
    except requests.exceptions.HTTPError as err:
        logging.warning("Alert non 200 status code")
    except Exception as ex: 
        logging.warning("Exception received {}".format(ex))
    


