import requests as req
import syslog as syslog
from os import system
from pathlib import Path

# Retrieve current external IP address
ip_api = req.get("https://api.ipify.org?format=json").json()
ext_ip = ip_api['ip']

# Retrieve Lonitude and Latitude of current IP
loc_api = req.get("http://ip-api.com/json/"+ext_ip).json()
lon_coord = loc_api['lon']
lat_coord = loc_api['lat']

sun_api = req.get(
    f"https://api.sunrisesunset.io/json?lat={str(lat_coord)}&lng={str(lon_coord)}").json()
sunrise = sun_api['results']['sunrise']
sunset = sun_api['results']['sunset']

cur_rise = Path('/opt/conkyrefs/.sunrise').read_text()
cur_set = Path('/opt/conkyrefs/.sunset').read_text()

# Write sunrise time to file
if cur_rise != sunrise:
    risefile = open("/opt/conkyrefs/.sunrise", "r+")
    contents = risefile.read().split("\n")
    risefile.seek(0)
    risefile.truncate()
    risefile.write(sunrise)
    syslog.syslog(syslog.LOG_INFO,
                  f"Sunrise time set to {sunrise} from {cur_rise}")
else:
    syslog.syslog(syslog.LOG_INFO,
                  "Retrieved sunrise time identical to current. Not changed.")

# Write sunset time to file
if cur_set != sunset:
    setfile = open("/opt/conkyrefs/.sunset", "r+")
    contents = setfile.read().split("\n")
    setfile.seek(0)
    setfile.truncate()
    setfile.write(sunset)
    syslog.syslog(syslog.LOG_INFO,
                  f"Sunset time set to {sunset} from {cur_set}")
else:
    syslog.syslog(syslog.LOG_INFO,
                  "Retrieved sunset time identical to current. Not changed.")
