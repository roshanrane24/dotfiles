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
@hook.subscribe.startup_once
def autostart():
    processes = [
        ["numlockx", "on"],
        ["xset", "b", "off"],
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


@hook.subscribe.startup_complete
def randr():
    display.set_extend_all()


@hook.subscribe.client_new
def floating_dialogs(window):
    if ((window.window.get_wm_type() == 'dialog') or
       (window.window.get_wm_transient_for())):
        window.floating = True
