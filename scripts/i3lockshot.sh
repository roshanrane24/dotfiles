#/bin/sh

image=/tmp/lockshot.png
if [ image > /dev/null ];
then
	rm $image
	echo image removed.
fi
scrot -z $image
mogrify -blur 0x15 $image
i3lock -p default -i $image
