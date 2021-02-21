from libqtile import hook
import subprocess
import os
from keybinds import keys
from setting import HOME
from layout_screen import layouts, floating_layout, screens, display
from groups import groups

# Configuration Variables
auto_fullscreen = True
bring_front_click = True
cursor_warp = True
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
focus_on_window_activation = "smart"
follow_mouse_focus = True
wmname = "LG3D"
widget_defaults = dict(
    font='Space Mono',
    fontsize=13,
    padding=8,
)
extension_defaults = widget_defaults.copy()


# Calling Hooks
@hook.subscribe.startup_once
def autostart():
    processes = [
        ["numlockx", "on"],
        ["nm-applet"],
        ['blueman-applet'],
        ["picom"],
        ["xset", "b", "off"],
        ["/usr/lib/mate-polkit/polkit-mate-authentication-agent-1"],
        ["kdeconnect-indicator"],
        ["xmodmap", "-e", "\"keycode", "78=d", "D", "d", "D\""], # for broker `d` key
    ]

    for p in processes:
        subprocess.Popen(p)
        print(f"succefully ran {' '.join(p)}")


@hook.subscribe.startup_complete
def wallpaper():
    subprocess.call([os.path.join(HOME, ".fehbg")])


@hook.subscribe.startup_complete
def randr():
    display.set_extend_all()
