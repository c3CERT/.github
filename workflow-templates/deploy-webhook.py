#!/usr/bin/env python

import requests
import json
import os
import sys

def error(message):
    print(f'\033[31;1mERROR:\033[0m {message}')

def info(label, message):
    print(f'\033[33;1m{label}\033[0m{message}')

exit_code = 0

try:
    url = os.environ['url']
    payload = json.loads(os.environ['payload'])
except  KeyError as e:
    error(f'Environment {e} not found.')
    sys.exit(1)

try:
    request = requests.post(url, json=payload)
except Exception as e:
    info('WARNING: ', 'Could not execte request:')
    print(e)
    sys.exit(1)

if request.status_code != 200:
    exit_code = 1
    error(f'Received a non OK status from deploy script: {request.status_code}')

response = request.json()
info('Messages:\n', response["message"])
info('Errors:\n', response["error"])
sys.exit(exit_code)
