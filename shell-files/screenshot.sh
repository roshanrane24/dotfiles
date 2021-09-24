#!/bin/bash

getopts ':iw' mode;
if [[ $mode == 'i' ]]
then
    `scrot -zs "$HOME/Pictures/Screenshots/%Y%m%d_%H%M%S_$wx$h.png"`
    `paplay /usr/share/sounds/freedesktop/stereo/camera-shutter.oga`
elif [[ $mode == 'w' ]]
then
    `scrot -zu "$HOME/Pictures/Screenshots/%Y%m%d_%H%M%S_$wx$h.png"`
    `paplay /usr/share/sounds/freedesktop/stereo/camera-shutter.oga`
else
    `scrot -z "$HOME/Pictures/Screenshots/%Y%m%d_%H%M%S_$wx$h.png"`
    `paplay /usr/share/sounds/freedesktop/stereo/camera-shutter.oga`
fi
