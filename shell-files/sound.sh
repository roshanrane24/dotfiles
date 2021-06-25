#!/usr/bin/sh

# Check Dunst Cache
cache_loc="$HOME/.cache/sound"
if [ ! -d $cache_loc ]; then
    mkdir -p $cache_loc
fi

sound="/usr/share/sounds"
if [ -n "$SOUNDTHEME" ]; then
    sound_theme="$sound/$SOUNDTHEME/stereo"
else
    sound_theme="$sound/freedesktop/stereo"
fi

# Set Volume
if [ ! -e "$cache_loc/volume" ]; then
    echo 50 > "$cache_loc/volume"
fi
volume=`cat "$cache_loc/volume"`
if [ -n "$2" ]; then
    if [ "$2" -gt 0 ] && [ "$2" -le 100 ]; then
        volume="$2"
    fi
fi

# Play Sound
if [ ! -e "$cache_loc/silent" ]; then
    case "$1" in
        notify)
            paplay --volume $volume -p "$sound_theme/bell.oga"
            ;;
        dev-connect)
            paplay --volume $volume -p "$sound_theme/device-added.oga"
            ;;
        dev-disconnect)
            paplay --volume $volume -p "$sound_theme/device-removed.oga"
            ;;
        net-connect)
            paplay --volume $volume -p "$sound_theme/network-connectivity-established.oga"
            ;;
        net-disconnect)
            paplay --volume $volume -p "$sound_theme/network-connectivity-lost.oga"
            ;;
        message)
            paplay --volume $volume -p "$sound_theme/message.oga"
            ;;
        audio)
            paplay --volume $volume -p "$sound_theme/audio-volume-change.oga"
            ;;
        error)
            paplay --volume $volume -p "$sound_theme/dialog-error.oga"
            ;;
        capture)
            paplay --volume $volume -p "$sound_theme/camera-shutter.oga"
            ;;
        trash)
            paplay --volume $volume -p "$sound_theme/trash.oga"
            ;;
        login)
            paplay --volume $volume -p "$sound_theme/service-login.oga"
            ;;
        logout)
            paplay --volume $volume -p "$sound_theme/service-logout.oga"
            ;;
        *)
            exit
            ;;
    esac
fi
