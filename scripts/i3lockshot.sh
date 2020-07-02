#/bin/sh

image=/tmp/lockshot.png
scrot -z $image
mogrify -blur 0x3 $image
i3lock -p default -i $image
