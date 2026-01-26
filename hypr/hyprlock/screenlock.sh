# enter the live wallpaper you want also if you want then you can just enter a pic and it'll work
wallpaper=$HOME/.config/hypr/hyprlock/wallpaper.mp4   # This is just an example wallpaper
wallpaper=$HOME/Documents/video_wallpaper/Videos/4K/SDR/4k_sdr.m3u

#don't worry about this variable it'll do
current=$(hyprctl activeworkspace -j | jq '.id')

mpvpaper -p --mpv-options="--no-config --script-opts=mpv-mpris:disable --loop-playlist --shuffle --no-audio loop" --layer overlay ALL $wallpaper & hyprlock ; pkill mpvpaper
# mpvpaper -vs -o "no-audio loop" --layer overlay ALL $wallpaper & hyprlock; pkill mpvpaper

