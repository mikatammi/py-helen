#!/usr/bin/env python

from datetime import date, timedelta
from json import dump
from requests import get

url = "https://www2.helen.fi/api/meteringpoints/0/%s/series?enddate=%s&numberofmonths=12&numberofyears=2&resolution=DAYS_AS_HOURS&selector=value,status,day,month,year,hour,milestones(title,note,timestamp(date,month,year)),temperature,prediction,telePrediction,budget,teleEuro,waterFlowPrice"

auth = "REPLACE_WITH_YOUR_AUTH_COOKIE"
cookie = "REPLACE_WITH_YOUR_SESSION_COOKIE"

headers = {'Authorization': auth,
           'Cookie': cookie}

meteringpoint = 1234 # Replace with your metering point number (part of the URL)

# You might want to replace these as well
date_begin = date(2016, 8, 3)
date_end = date(2018, 4, 30)

date_delta = date_end - date_begin
dates = [(date_begin + timedelta(days=i)).strftime("%Y%m%d") for i in range(date_delta.days + 1)]


def _dumpdata(d):
    print(d)
    r = get(url % (meteringpoint, d), headers=headers)
    return r.json()


if __name__ == '__main__':
    datas = {d: _dumpdata(d) for d in dates}
    with open("helendata.json", 'w') as f:
        dump(datas, f, indent=4, sort_keys=True)
