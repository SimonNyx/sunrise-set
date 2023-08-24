import requests as req

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

# Write sunrise time to file
risefile = open("/usr/local/bin/.sunrise", "r+")
contents = risefile.read().split("\n")
risefile.seek(0)
risefile.truncate()
risefile.write(sunrise)

# Write sunset time to file
setfile = open("/usr/local/bin/.sunset", "r+")
contents = setfile.read().split("\n")
setfile.seek(0)
setfile.truncate()
setfile.write(sunset)
