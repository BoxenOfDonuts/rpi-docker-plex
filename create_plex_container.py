try:
    from urllib.parse import urlparse
except ImportError:
    from urllib2 import urlparse

try:  # python3
    from urllib.request import urlopen
except:  # python2
    from urllib2 import urlopen

import os

PLEX_SYNOLOGY_URL = 'https://plex.tv/downloads/latest/1?channel=16&build=linux-synology-armv7&distro=synology'
PLEX_DOCKER_DIRECTORY = os.environ['HOME'] + '/git/rpi-docker-plex'
res = urlopen(PLEX_SYNOLOGY_URL)
PLEX_SYNOLOGY_FINAL_URL = res.geturl()
PLEX_SYNOLOGY_URL_PARSED = urlparse(PLEX_SYNOLOGY_FINAL_URL)
PLEX_SYNOLOGY_URL_PATHS = PLEX_SYNOLOGY_URL_PARSED.path.split("/")
PLEX_SYNOLOGY_PARSED_VERSION = PLEX_SYNOLOGY_URL_PATHS[2]

print("newest plex version is: " + PLEX_SYNOLOGY_PARSED_VERSION)

os.chdir(PLEX_DOCKER_DIRECTORY)

os.system('docker build -t johnypony3/rpi-docker-plex:latest . --build-arg PLEX_VERSION=' +
          PLEX_SYNOLOGY_PARSED_VERSION)

os.system('docker build -t johnypony3/rpi-docker-plex:' + PLEX_SYNOLOGY_PARSED_VERSION + ' . --build-arg PLEX_VERSION=' +
          PLEX_SYNOLOGY_PARSED_VERSION)

os.system('sudo -s source /usr/bin/.variables && docker push johnypony3/rpi-docker-plex:latest')

os.system('sudo -s source /usr/bin/.variables && docker push johnypony3/rpi-docker-plex:' +
          PLEX_SYNOLOGY_PARSED_VERSION)
