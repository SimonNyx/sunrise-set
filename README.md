# Sunrise & Sunset Times API

Using public API's this pulls the sunrise and sunset times based on your external IP location.

## Documentation

The initial purpose was to support the Conky configuration pinched from [here](https://askubuntu.com/a/1014284) kindly posted by [WinEunuuchs2Unix](https://github.com/WinEunuuchs2Unix)

Where eyesome was used to pull the sunrise and sunset time for this configuration, I didn't require the dimming feature, and wanted to play with python and pulling API data.

For standard usage -

Create 2 files in /opt/conkyrefs (or under home directory if preferred) called .sunrise and .sunset

If using the Conky configuration above amend the names for the paths of the above 2 files

Save the python file to /usr/bin/

Set the following crontab entries.

@reboot /usr/bin/python3 /usr/bin/sunrise-set.py # Runs on boot/login

15 0-23/3 \* \* \* /usr/bin/python3 /usr/bin/sunrise-set.py # Runs every 3 hours

Note: If this doesn't run on cron correctly you might need to preface it with

SHELL=/bin/bash

PATH=/bin:/sbin:/usr/bin:/usr/sbin
