#!/bin/bash

if [[ `ip link show wlan0 | cut -d ' ' -f 9` == 'DOWN' ]]
then
    `sudo ip link set wlan0 up`
elif [[ `ip link show wlan0 | cut -d ' ' -f 9` == 'UP' ]]
then
    `sudo ip link set wlan0 down`
fi
