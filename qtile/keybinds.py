from libqtile.config import Key, Drag, Click 
from libqtile.lazy import lazy
from setting import MODKEY, TERMINAL, BROWSER, HOME
from groups import groups
import os


keys = [
    # Switch between windows in current stack pane
    Key([MODKEY], "Up", lazy.layout.up(), desc="Move focus up in stack pane"),
    Key([MODKEY], "Down", lazy.layout.down(), desc="Move focus down in stack pane"),
    Key([MODKEY], "Left", lazy.layout.left(), desc="Move focus left in stack pane"),
    Key([MODKEY], "Right", lazy.layout.right(), desc="Move focus right in stack pane"),
    # Move windows up or down in current stack
    Key([MODKEY, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up in current stack "),
    Key([MODKEY, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down in current stack "),
    Key([MODKEY, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window left in current stack "),
    Key([MODKEY, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window right in current stack "),
    # Flip windows up or down in current stack
    Key([MODKEY, "control"], "Up", lazy.layout.flip_up(), desc="Flip window up in current stack "),
    Key([MODKEY, "control"], "Down", lazy.layout.flip_down(), desc="Flip window down in current stack "),
    Key([MODKEY, "control"], "Left", lazy.layout.flip_left(), desc="Flip window left in current stack "),
    Key([MODKEY, "control"], "Right", lazy.layout.flip_right(), desc="Flip window right in current stack "),
    # grow windows up or down in current stack
    Key([MODKEY, "mod1"], "Up", lazy.layout.grow_up(), desc="Grow window up in current stack "),
    Key([MODKEY, "mod1"], "Down", lazy.layout.grow_down(), desc="Grow window down in current stack "),
    Key([MODKEY, "mod1"], "Left", lazy.layout.grow_left(), desc="Grow window left in current stack "),
    Key([MODKEY, "mod1"], "Right", lazy.layout.grow_right(), desc="Grow window right in current stack "),
    Key([MODKEY], "n", lazy.layout.normalize(), desc="Normalize current layout "),
    Key([MODKEY], "m", lazy.layout.maximize(), desc="Maximize selected window "),
    # Switch window focus to other pane(s) of layout
    Key([MODKEY], "Tab", lazy.layout.next(), desc="Switch window focus to next pane(s) of layout"),
    Key([MODKEY, 'shift'], "Tab", lazy.layout.previous(), desc="Switch window focus to prev pane(s) of layout"),
    # Swap panes of split stack
    Key([MODKEY,"shift"], "r", lazy.layout.rotate(), desc="Swap panes of split stack"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([MODKEY], "s", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    # Toggle between different layouts as defined below
    Key([MODKEY, "mod1"], "space", lazy.next_layout(), desc="next layouts"),
    Key([MODKEY, "control"], "space", lazy.prev_layout(), desc="previous layouts"),
    Key([MODKEY, "shift"], "space", lazy.next_urgent(), desc="next urgent layouts"),
    Key([MODKEY], "Page_Up", lazy.next_screen(), desc="next screen"),
    Key([MODKEY], "Page_Down", lazy.prev_screen(), desc="previous screen"),
    # Window
    Key([MODKEY, "shift"], "Page_Up", lazy.up_opacity(), desc="Increase Opacity"),
    Key([MODKEY, "shift"], "Page_Down", lazy.down_opacity(), desc="Decrease Opacity"),
    Key([MODKEY, "mod1"], "f", lazy.bring_to_front(), desc="Toggle between layouts"),
    Key([MODKEY, "mod1"], "minus", lazy.toggle_minimize(), desc="Toggle between layouts"),
    Key([MODKEY, "mod1"], "plus", lazy.toggle_maximize(), desc="Toggle between layouts"),
    Key([MODKEY], "q", lazy.window.kill(), desc="Kill focused window"),
    # wm sys command
    Key([MODKEY], "F2", lazy.restart(), desc="Restart qtile"),
    Key([MODKEY, "control"], "F12", lazy.shutdown(), desc="Shutdown qtile"),
    # Run Command/Application Launcher
    Key([MODKEY, "shift"], "g", lazy.spawn('dmenu_run -l 10 -p Run'), desc="Spawn a command using a prompt widget"),
    Key([MODKEY], "g", lazy.spawn('rofi -show drun -theme lime-amber -show-icons -icon-theme Flat-Remix-Green-Dark -display-drun ""'), desc="Spawn a command using a prompt widget"),
    Key([MODKEY, "mod1"], "g", lazy.spawn('rofi -show window -theme lime-amber -display-window ""'), desc="Spawn a command using a prompt widget"),
    Key([MODKEY], "Return", lazy.spawn(TERMINAL), desc="Launch Terminal"),
    Key([MODKEY, "control"], "2", lazy.spawn(BROWSER), desc="Launch Browser (Brave)"),
    Key([MODKEY, "control"], "3", lazy.spawn("thunar"), desc="Launch File Manager (Thunar)"),
    Key([MODKEY, "control", "shift"], "3", lazy.spawn("pcmanfm"), desc="Launch File Manager (Thunar)"),
    Key([MODKEY, "control"], "4", lazy.spawn("code"), desc="Launch Editor (Code)"),
    Key([MODKEY, "control"], "5", lazy.spawn("vlc"), desc="Launch Media Player (VLC)"),
    Key([MODKEY, "control"], "6", lazy.spawn("spotify"), desc="Launch Music Player (Spotify)"),
    Key([MODKEY, "control"], "7", lazy.spawn("signal-desktop"), desc="Launch Signal"),
    Key([MODKEY, "shift"], "7", lazy.spawn("discord"), desc="Launch Discord"),
    Key([MODKEY, "mod1"], "7", lazy.spawn("telegram-desktop"), desc="Launch Telegram"),
    Key([MODKEY, "control"], "8", lazy.spawn("qbittorrent"), desc="Launch qBittorrent"),
    Key([MODKEY, "control"], "p", lazy.spawn("pycharm"), desc="Launch pycharm"),
    Key([MODKEY, "mod1"], "p", lazy.spawn("Pilorama"), desc="Launch Pilorama "),

    Key([MODKEY], "space", lazy.window.toggle_floating(), desc="Toggle Floating for Focused Window"),
    Key([MODKEY], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
    Key([MODKEY], "b", lazy.hide_show_bar("top"), desc="Toggle Fullscreen"),
    Key([MODKEY], "Print", lazy.spawn(f"flameshot gui -p {os.path.join(HOME,'Pictures/Screenshots')}"), desc="Screenshot"),
    Key([], "Print", lazy.spawn(f"flameshot full -p {os.path.join(HOME,'Pictures/Screenshots')}"), desc="Screenshot"),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5"), desc="Increase Brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spwan("xbacklight -dec 5"), desc="Decrease Brightness"),
    # Audio
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2%"), desc="Raise Volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2%"), desc="Lower Volume"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Mute Volume"),
    Key([], "XF86Tools", lazy.spawn("spotify"), desc="Launch Spotify"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Music Next"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Music Play/Pause"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Music Previous"),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop"), desc="Music Stop"),
]

mouse = [
    Drag([MODKEY], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MODKEY], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MODKEY], "Button2", lazy.window.bring_to_front()) 
]


# adding extra key binding to keys
for i in groups:
    keys.extend([
        # Switch to screen
        Key([MODKEY], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
        # Switch Window to Screen
        Key([MODKEY, "shift"], i.name, lazy.window.togroup(i.name), 
        desc=f"Switch to focused window to group {i.name}"),
    ])
