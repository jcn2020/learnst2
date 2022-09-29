#!/usr/bin/bash
# TIMEZONE=$1
TIMEZONE=America/Los_Angeles
echo $( TZ=${TIMEZONE} date +"%D - %r ${TIMEZONE#*/}" )
echo $( TZ=${TIMEZONE} date )
echo $( TZ=UTC+7 date )