import os
import subprocess

from setting import HOME, SCREEN
from groups import groups
from keybinds import keys
from layout_screen import floating_layout, layouts, screens
from libqtile import hook

# Configuration Variables
auto_fullscreen = True
bring_front_click = True
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []
focus_on_window_activation = "smart"
follow_mouse_focus = True
wmname = "LG3D"
widget_defaults = dict(
    font='Space Mono',
    fontsize=13,
    padding=8,
)
extension_defaults = widget_defaults.copy()
keys = keys
layouts = layouts
floating_layout = floating_layout
screens = screens
groups = groups


# Calling Hooks
# def randr():
#     if SCREEN == 'extend':
#         display.set_extend_all()
#     elif SCREEN == 'mirror':
#         display.set_mirror_all()


@hook.subscribe.startup_once
def autostart():
    processes = [
        ["numlockx", "on"],
        ["xset", "b", "off"],
        ["xrandr", "--auto"],
        ["xset", "s", "600", "300"],
        ["xset", "dpms", "900", "1500", "2100"],
        ["xss-lock", "-l", "betterlockscreen"],
        ["cbatticon", "-u", "10", "-l", "18", "-r", "6", "-c",
         "\"systemctl suspend\""],
        ["nm-applet"],
        ["pasystray", "-m", "125", "-t"],
        ["mictray"],
    ]

    for p in processes:
        try:
            subprocess.Popen(p)
            print(f"succefully ran {' '.join(p)}")
        except Exception as e:
            print(e)


@hook.subscribe.startup_complete
def wallpaper():
    subprocess.call([os.path.join(HOME, ".fehbg")])


# @hook.subscribe.client_new
# def floating_dialogs(window):
#     if ((window.window.get_wm_type() == 'dialog') or
#        (window.window.get_wm_transient_for())):
#         window.floating = True


@hook.subscribe.client_new
def spotify_6(window):
    print(window)
    if window.name == 'Spotify Free':
        window.togroup('6')


@hook.subscribe.screen_change
def refresh_screens():
    subprocess.Popen(["xrandr", "--auto"])
