#!/usr/bin/env python3

# Tested only from quay.io to hub.docker.com.

import sys
import requests
import os

def getApiUrl(repo, type):
    parts = repo.split('/')
    domain = 'registry.hub.docker.com/'
    if (len(parts) > 3):
        print('Invalid repo ' + type)
        exit(1)
    elif (len(parts) == 3):
        domain = ''
        parts.insert(1, 'v2')
    else:
        parts.insert(0, 'v2')

    apiUrl = 'https://' + domain + '/'.join(parts) + '/tags/list'
    return apiUrl

if (len(sys.argv) < 3):
    print('You need 2 arguments: source and destination images.')
    exit(1)


argv = sys.argv[1:]
source = argv[0]
sourceApiUrl = getApiUrl(source, 'source')
destination = argv[1]
destinationApiUrl = getApiUrl(destination, 'destination')

# Validate source exist and you have access.
response = requests.get(sourceApiUrl)
if (response.status_code != 200):
    print('Source repository not working.')
    exit()

tagsJson = response.json()

for tag in tagsJson['tags']:
    pullCommand = 'docker pull ' + source + ':' + tag
    print('Running ' + pullCommand + '...')
    os.system(pullCommand)
    retagCommand = 'docker tag ' + source + ':' + tag + ' ' + destination + ':' + tag
    print('Running ' + retagCommand + '...')
    os.system(retagCommand)
    pushCommand = 'docker push ' + destination + ':' + tag
    print('Running ' + pushCommand + '...')
    os.system(pushCommand)
    pruneCommand = 'docker image prune -f'
    print('Running ' + pruneCommand + '...')
    os.system(pruneCommand)


