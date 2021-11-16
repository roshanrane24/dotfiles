from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy
from setting import (BROWSER, BROWSER_2, MODKEY, TERMINAL, EDITOR_GUI,
                     FILE_MANAGER, FILE_MANAGER_2, SCRIPTS,
                     ROFI_THEME)
from groups import groups
from functions import move_group_to_next_screen, move_group_to_prev_screen
import os


keys = [
    # Switch between windows in current stack pane
    # BSP
    Key([MODKEY], "Up",
        lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([MODKEY], "Down",
        lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([MODKEY], "Left",
        lazy.layout.left(),
        desc="Move focus left in stack pane"),
    Key([MODKEY], "Right",
        lazy.layout.right(),
        desc="Move focus right in stack pane"),
    Key([MODKEY], "k",
        lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([MODKEY], "j",
        lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([MODKEY], "h",
        lazy.layout.left(),
        desc="Move focus left in stack pane"),
    Key([MODKEY], "l",
        lazy.layout.right(),
        desc="Move focus right in stack pane"),

    # Move windows up or down in current stack
    # BSP
    Key([MODKEY, "shift"], "Up",
        lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    Key([MODKEY, "shift"], "Down",
        lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([MODKEY, "shift"], "Left",
        lazy.layout.shuffle_left(),
        desc="Move window left in current stack "),
    Key([MODKEY, "shift"], "Right",
        lazy.layout.shuffle_right(),
        desc="Move window right in current stack "),
    Key([MODKEY, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    Key([MODKEY, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([MODKEY, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window left in current stack "),
    Key([MODKEY, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window right in current stack "),

    # Flip windows up or down in current stack
    # BSP
    Key([MODKEY, "control"], "Up",
        lazy.layout.flip_up(),
        desc="Flip window up in current stack "),
    Key([MODKEY, "control"], "Down",
        lazy.layout.flip_down(),
        desc="Flip window down in current stack "),
    Key([MODKEY, "control"], "Left",
        lazy.layout.flip_left(),
        desc="Flip window left in current stack "),
    Key([MODKEY, "control"], "Right",
        lazy.layout.flip_right(),
        desc="Flip window right in current stack "),
    Key([MODKEY, "control"], "k",
        lazy.layout.flip_up(),
        desc="Flip window up in current stack "),
    Key([MODKEY, "control"], "j",
        lazy.layout.flip_down(),
        desc="Flip window down in current stack "),
    Key([MODKEY, "control"], "h",
        lazy.layout.flip_left(),
        desc="Flip window left in current stack "),
    Key([MODKEY, "control"], "l",
        lazy.layout.flip_right(),
        desc="Flip window right in current stack "),

    # grow windows up or down in current stack
    # BSP
    Key([MODKEY, "mod1"], "Up",
        lazy.layout.grow_up(),
        desc="Grow window up in current stack "),
    Key([MODKEY, "mod1"], "Down",
        lazy.layout.grow_down(),
        desc="Grow window down in current stack "),
    Key([MODKEY, "mod1"], "Left",
        lazy.layout.grow_left(),
        desc="Grow window left in current stack "),
    Key([MODKEY, "mod1"], "Right",
        lazy.layout.grow_right(),
        desc="Grow window right in current stack "),
    Key([MODKEY, "mod1"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up in current stack "),
    Key([MODKEY, "mod1"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down in current stack "),
    Key([MODKEY, "mod1"], "h",
        lazy.layout.grow_left(),
        desc="Grow window left in current stack "),
    Key([MODKEY, "mod1"], "l",
        lazy.layout.grow_right(),
        desc="Grow window right in current stack "),

    Key([MODKEY], "n",
        lazy.layout.normalize(),
        desc="Normalize current layout "),
    Key([MODKEY], "m",
        lazy.layout.maximize(),
        desc="Maximize selected window "),

    # Switch window focus to other pane(s) of layout
    Key([MODKEY], "Tab",
        lazy.layout.next(),
        desc="Switch window focus to next pane(s) of layout"),
    Key([MODKEY, 'shift'], "Tab",
        lazy.layout.previous(),
        desc="Switch window focus to prev pane(s) of layout"),

    # Swap panes of split stack
    Key([MODKEY, "shift"], "r",
        lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # BSP
    Key([MODKEY], "s",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([MODKEY, "mod1"], "space",
        lazy.next_layout(),
        desc="next layouts"),
    Key([MODKEY, "control"], "space",
        lazy.prev_layout(),
        desc="previous layouts"),
    Key([MODKEY], "u",
        lazy.next_urgent(),
        desc="next urgent layouts"),
    Key([MODKEY, "shift"], "u",
        lazy.next_urgent(),
        desc="next urgent layouts"),
    Key([MODKEY, "control", "mod1"], "Right",
        lazy.next_screen(),
        desc="next screen"),
    Key([MODKEY, "control", "mod1"], "Left",
        lazy.next_screen(),
        desc="previous screen"),
    Key([MODKEY, "control", "mod1"], "l",
        lazy.next_screen(),
        desc="next screen"),
    Key([MODKEY, "control", "mod1"], "h",
        lazy.prev_screen(),
        desc="previous screen"),

    # Window
    Key([MODKEY, "shift"], "Page_Up",
        lazy.up_opacity(),
        desc="Increase Opacity"),
    Key([MODKEY, "shift"], "Page_Down",
        lazy.down_opacity(),
        desc="Decrease Opacity"),
    Key([MODKEY, "mod1"], "f",
        lazy.window.bring_to_front(),
        desc="Toggle between layouts"),
    Key([MODKEY, "mod1"], "minus",
        lazy.toggle_minimize(),
        desc="Toggle between layouts"),
    Key([MODKEY, "mod1"], "plus",
        lazy.toggle_maximize(),
        desc="Toggle between layouts"),
    Key([MODKEY], "q",
        lazy.window.kill(),
        desc="Kill focused window"),
    # wm sys command
    Key([MODKEY], "F2",
        lazy.restart(),
        desc="Restart qtile"),
    Key([MODKEY, "control"], "F12",
        lazy.shutdown(),
        desc="Shutdown qtile"),

    # Run Command/Application Launcher
    Key([MODKEY], "d",
        lazy.spawn("rofi -show drun -matching fuzzy -modi" \
                   f"run,ssh -theme {ROFI_THEME}"),
        desc="Spawn a command using a prompt widget"),
    Key([MODKEY, "mod1"], "d",
        lazy.spawn("rofi -show window -matching fuzzy -modi" \
                   f"windowcd -theme {ROFI_THEME}"),
        desc="Spawn a command using a prompt widget"),
    Key([MODKEY], "Return",
        lazy.spawn(TERMINAL),
        desc="Launch Terminal"),
    Key([MODKEY, "control"], "Return",
        lazy.spawn(TERMINAL + " -e '/bin/zsh'"),
        desc="Launch Terminal"),
    Key([MODKEY, "control"], "2",
        lazy.spawn(BROWSER),
        desc="Launch Browser (Brave)"),
    Key([MODKEY, "control", "shift"], "2",
        lazy.spawn(BROWSER_2),
        desc="Launch Browser (Brave)"),
    Key([MODKEY, "control"], "3",
        lazy.spawn(FILE_MANAGER),
        desc="Launch File Manager (Main)"),
    Key([MODKEY, "control", "shift"], "3",
        lazy.spawn(FILE_MANAGER_2),
        desc="Launch File Manager (Alt)"),
    Key([MODKEY, "control"], "4",
        lazy.spawn(EDITOR_GUI),
        desc="Launch Editor (Code)"),
    Key([MODKEY, "control"], "e",
        lazy.spawn("eclipse"),
        desc="Launch Editor (eclipse)"),
    Key([MODKEY, "control"], "i",
        lazy.spawn("idea"),
        desc="Launch Editor (idea)"),
    Key([MODKEY, "control"], "5",
        lazy.spawn("vlc"),
        desc="Launch Media Player (VLC)"),
    Key([MODKEY, "control"], "6",
        lazy.spawn("spotify"),
        desc="Launch Music Player (Spotify)"),
    Key([MODKEY, "control"], "7",
        lazy.spawn("discord"),
        desc="Launch Discord"),
    Key([MODKEY, "control", "shift"], "7",
        lazy.spawn("telegram-desktop"),
        desc="Launch HexChat"),
    Key([MODKEY, "control"], "8",
        lazy.spawn("qbittorrent"),
        desc="Launch qBittorrent"),
    Key([MODKEY, "control"], "0",
        lazy.spawn("zoom"),
        desc="Launch Zoom Client"),
    Key([MODKEY, "control"], "p",
        lazy.spawn("pycharm"),
        desc="Launch pycharm"),
    Key(["mod1", "control"], "v",
        lazy.spawn("pavucontrol"),
        desc="Launch pavucontrol (Sound Manager)"),

    # Dunst
    Key(["control"], "grave",
        lazy.spawn("dunstctl history-pop"),
        desc="Dunst pop notifications from history"),
    Key(["control", "mod1"], "space",
        lazy.spawn("dunstctl close"),
        desc="Dunst close single notification"),
    Key(["control", "shift"], "space",
        lazy.spawn("dunstctl close-all"),
        desc="Dunst close all notification"),
    Key(["mod1", "shift"], "space",
        lazy.spawn("dunstctl context"),
        desc="Dunst show context menu"),


    Key([MODKEY], "space",
        lazy.window.toggle_floating(),
        desc="Toggle Floating for Focused Window"),
    Key([MODKEY], "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle Fullscreen"),
    Key([MODKEY], "b",
        lazy.hide_show_bar("top"),
        desc="Toggle Fullscreen"),

    # ScreenShot
    Key([MODKEY], "Print",
        lazy.spawn(f"bash -c '{os.path.join(SCRIPTS, 'screenshot.sh')}'"),
        desc="Screenshot"),
    Key([MODKEY, "control"], "Print",
        lazy.spawn(f"bash -c '{os.path.join(SCRIPTS, 'screenshot.sh')} -i'"),
        desc="Screenshot"),
    Key([MODKEY, "shift"], "Print",
        lazy.spawn(f"bash -c '{os.path.join(SCRIPTS, 'screenshot.sh')} -w'"),
        desc="Screenshot"),

    # Brightness
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("xbacklight -inc 5"),
        desc="Increase Brightness"),
    Key([], "XF86MonBrightnessDown",
        lazy.spwan("xbacklight -dec 5"),
        desc="Decrease Brightness"),

    # Audio
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
        desc="Raise Volume"),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
        desc="Lower Volume"),
    Key([], "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        desc="Mute Volume"),
    Key(["mod1"], "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-source-volume @DEFAULT_SOURCE@ +5%"),
        desc="Raise Mic Volume"),
    Key(["mod1"], "XF86AudioLowerVolume",
        lazy.spawn("pactl set-source-volume @DEFAULT_SOURCE@ -5%"),
        desc="Lower Mic Volume"),
    Key(["mod1"], "XF86AudioMute",
        lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle"),
        desc="Mute Mic Volume"),
    Key([], "XF86Tools",
        lazy.spawn("spotify"),
        desc="Launch Spotify"),
    Key([], "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="Music Next"),
    Key([], "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Music Play/Pause"),
    Key([], "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="Music Previous"),
    Key([], "XF86AudioStop",
        lazy.spawn("playerctl stop"),
        desc="Music Stop"),
    ]

mouse = [
    Drag([MODKEY], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MODKEY], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MODKEY], "Button2", lazy.window.bring_to_front())
    ]


# adding extra key binding to keys
for group in groups:
    keys.extend([
        # Switch to Group
        Key([MODKEY], group.name,
            lazy.group[group.name].toscreen(),
            desc=f"Switch to group {group.name}"),
        # Switch Window to Group
        Key([MODKEY, "shift"], group.name,
            lazy.window.togroup(group.name),
            desc=f"Switch to focused window to group {group.name}"),
    ])
