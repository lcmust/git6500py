#!/bin/bash
PIDISRUN=$1
which $PIDISRUN &>/dev/null || exit 1
$(ps aux|grep "$PIDISRUN"|grep -v "grep" -q)
if [ $? = 0 ]; then
    echo "$PIDISRUN is running..."
else
    echo "$PIDISRUN is not run!"
fi
