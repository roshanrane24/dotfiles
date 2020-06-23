#!/usr/bin/bash

# Terminate already running bar instances
killall -q polybar
# If all your bars have ipc enabled, you can also use 
# polybar-msg cmd quit

# Launch bar1 and bar2
echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
polybar  primary >>/tmp/polybar1.log 2>&1 &
polybar -l info secondary >>/tmp/polybar2.log 2>&1 &

echo "Bars launched..."
