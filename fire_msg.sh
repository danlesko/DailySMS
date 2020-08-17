#!/bin/sh

timestamp=$(date +%s)

cd /Users/$(whoami)/$DAILY_SMS_DIR

source bin/activate

message_id=$(python src/stasia_sms.py)

timestamp=`date`

log="${timestamp} - ${message_id}"

echo $log >> log/sent_msgs.log

deactivate
