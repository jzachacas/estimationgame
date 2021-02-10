#!/bin/bash

HTTP=$(which http)

if [ ! -x "$HTTP" ]; then
    echo 'You need HTTPie to run this script'
    echo 'install all requirements from requirements.txt'
    echo 'with pip -r requirements'
    exit 1
fi

URL=:5000/api

set -x

http GET $URL/story
http PUT $URL/story title="[TICKET-1] Dinge tun" description="Denn sie sind wichtig"
http GET $URL/story

http GET $URL/users
