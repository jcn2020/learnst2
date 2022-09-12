#!/usr/bin/bash
TIMEZONE=$1
echo $( TZ=${TIMEZONE} date +"%D - %r ${TIMEZONE#*/}" )