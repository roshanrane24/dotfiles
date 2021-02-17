from libqtile.config import Click, Drag, Group, Screen, Match, Key
from libqtile import bar, layout, widget
from libqtile.utils import guess_terminal
from libqtile.lazy import lazy
from colors import Colors
from libqtile import hook
from typing import List  # noqa: F401
import subprocess
import os


# Defining Constants
class COLORS:
    LIGHT_BACKGROUND = Colors.GRAY
    BACKGROUND = Colors.DARK_GRAY
    DARK_BACKGROUND = Colors.BLACK
    LIGHT_PRIMARY = Colors.LIGHT_GREEN
    PRIMARY = Colors.GREEN
    DARK_PRIMARY = Colors.DARK_GREEN
    LIGHT_COMPLEMENTARY = Colors.LIGHT_PINK
    COMPLEMENTARY = Colors.PINK
    DARK_COMPLEMENTARY = Colors.DARK_PINK
    LIGHT_URGENT = Colors.LIGHT_RED
    URGENT = Colors.RED
    DARK_URGENT = Colors.DARK_RED
    LIGHT_FONT = Colors.WHITE
    DARK_FONT = Colors.BLACK


MODKEY: str = "mod4"
TERMINAL = guess_terminal() # "terminator" 
BROWSER = "brave"
backlight = widget.Backlight(
    brightness_file="/sys/class/backlight/intel_backlight/subsystem/intel_backlight/brightness",
    max_brightness_file="/sys/class/backlight/intel_backlight/subsystem/intel_backlight/max_brightness",
    change_command="xbacklight -set {0}",
    step=1,
)


# Defining Functions

# Defining Keybindings
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
    # Switch window focus to other pane(s) of stack
    Key([MODKEY], "Tab", lazy.layout.next(), desc="Switch window focus to other pane(s) of stack"),
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
    Key([MODKEY], "g", lazy.spawn('dmenu_run -l 10 -p Run'), desc="Spawn a command using a prompt widget"),
    Key([MODKEY], "Return", lazy.spawn(TERMINAL), desc="Launch Terminal"),
    Key([MODKEY, "control"], "2", lazy.spawn(BROWSER), desc="Launch Browser (Brave)"),
    Key([MODKEY, "control"], "3", lazy.spawn("thunar"), desc="Launch File Manager (Thunar)"),
    Key([MODKEY, "control"], "4", lazy.spawn("code"), desc="Launch Editor (Code)"),
    Key([MODKEY, "control"], "5", lazy.spawn("vlc"), desc="Launch Media Player (VLC)"),
    Key([MODKEY, "control"], "6", lazy.spawn("spotify"), desc="Launch Music Player (Spotify)"),
    Key([MODKEY, "control"], "7", lazy.spawn("signal-desktop"), desc="Launch Signal"),
    Key([MODKEY, "shift"], "7", lazy.spawn("discord"), desc="Launch Discord"),
    Key([MODKEY, "mod1"], "7", lazy.spawn("telegram-desktop"), desc="Launch Telegram"),
    Key([MODKEY, "control"], "8", lazy.spawn("qbittorrent"), desc="Launch qBittorrent"),
    Key([MODKEY, "control"], "p", lazy.spawn("pycharm"), desc="Launch pycharm"),

    Key([MODKEY], "space", lazy.window.toggle_floating(), desc="Toggle Floating for Focused Window"),
    Key([MODKEY], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
    Key([MODKEY], "b", lazy.hide_show_bar("top"), desc="Toggle Fullscreen"),
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


# Defining Workspace/Group/Tag
workspaces = {
    "1": {"label": "",
          "matches": {"wm_class": ["Terminator", "Alacritty"]}},
    "2": {"label": "",
          "matches": {"wm_class": ["Brave-browser"]}},
    "3": {"label": "",
          "matches": {"wm_class": ["Thunar"]}},
    "4": {"label": "",
          "matches": {"wm_class": ["code-oss", "jetbrains-pycharm-ce"]}},
    "5": {"label": "",
          "matches": {"wm_class": ["mpv"]}},
    "6": {"label": "",
          "matches": {"wm_class": ["Spotify"]}},
    "7": {"label": "",
          "matches": {"wm_class": ["Discord"]}},
    "8": {"label": "",
          "matches": {"wm_class": ["qBitorrent"]}},
    "9": {"label": "1",
          "matches": None},
    "0": {"label": "2",
          "matches": None}
              }

groups = []
for ws in workspaces.keys():
    if workspaces[ws]["matches"] is not None:
        match = [Match(wm_class=[x for x in list(workspaces[ws]["matches"].values())[0]])]
    else:
        match = None
    group = Group(name=ws,
                  label=workspaces[ws]["label"],
                  matches=match)
    groups.append(group)

print(groups)
for i in groups:
    keys.extend([
        # MODKEY1 + letter of group = switch to group
        Key([MODKEY], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
        # MODKEY1 + shift + letter of group = switch to & move focused window to group
        Key([MODKEY, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # MODKEY1 + shift + letter of group = move focused window to group
        # Key([MODKEY, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


# Layout
layouts = [
    layout.Bsp(
        border_focus=COLORS.PRIMARY,
        border_normal=COLORS.LIGHT_COMPLEMENTARY,
        border_width=1,
        grow_amount=5,
        margin=5,
    ),
    layout.Max(),
    layout.MonadTall(
        border_focus=COLORS.PRIMARY,
        border_normal=COLORS.LIGHT_COMPLEMENTARY,
        border_width=1,
        change_size=5,
        margin=2,
        single_border_width=1,
        single_margin=5,
    ),
    layout.MonadWide(
        border_focus=COLORS.PRIMARY,
        border_normal=COLORS.LIGHT_COMPLEMENTARY,
        border_width=1,
        change_size=5,
        margin=2,
        single_border_width=1,
        single_margin=5,
    ),
    layout.RatioTile(
        border_focus=COLORS.PRIMARY,
        border_normal=COLORS.LIGHT_COMPLEMENTARY,
        border_width=1,
        margin=2,
    ),
    layout.TreeTab(
        active_bg=COLORS.PRIMARY,
        active_fg=COLORS.DARK_FONT,
        bg_color=COLORS.DARK_BACKGROUND,
        border_width=1,
        inactive_bg=COLORS.DARK_COMPLEMENTARY,
        inactive_fg=COLORS.LIGHT_FONT,
        level_shift=2,
        margin_y=19,
        padding_left=5,
        padding_y=10,
        pannel_width=200,
        previous_on_rm=True,
        sections=["Main", "Extra"],
        section_bottom=10,
        section_fg=COLORS.LIGHT_BACKGROUND,
        section_fontsize=15,
        section_left=20,
        section_padding=20,
        section_top=20,
        urgent_bg=COLORS.URGENT,
        urgent_fg=COLORS.LIGHT_FONT,
        vspace=5,
    ),
    # layout.Tile(),
    # layout.Stack(num_stacks=4),
    # layout.Matrix(),
    # layout.Slice(),
    # Try more layouts by unleashing below layouts.
    # layout.Columns(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


# Widgets
widget_defaults = dict(
    font='Space Mono',
    fontsize=13,
    padding=8,
)

extension_defaults = widget_defaults.copy()
# noinspection PyUnresolvedReferences
screens = [
    # Primary Screen
    Screen(
        top=bar.Bar([
            widget.Sep(
                background=COLORS.BACKGROUND,
                foreground=COLORS.LIGHT_BACKGROUND,
                linewidth=3,
                padding=3,
                size_percent=80,
            ),
            widget.GroupBox(
                active=COLORS.LIGHT_PRIMARY,
                background=COLORS.BACKGROUND,
                block_highlight_text_color=COLORS.DARK_FONT,
                borderwidth=0,
                disable_drag=True,
                foreground=COLORS.LIGHT_FONT,
                inactive=COLORS.LIGHT_BACKGROUND,
                highlight_method="block",
                other_current_screen_border=COLORS.COMPLEMENTARY,
                other_screen_border=COLORS.DARK_PRIMARY,
                this_current_screen_border=COLORS.PRIMARY,
                this_screen_border=COLORS.LIGHT_COMPLEMENTARY,
                urgent_alert_method="block",
                urgent_border=COLORS.URGENT,
                urgent_text=COLORS.LIGHT_FONT,
                rounds=False,
            ),
            widget.Sep(
                background=COLORS.BACKGROUND,
                foreground=COLORS.LIGHT_BACKGROUND,
                linewidth=1,
                padding=3,
                size_percent=65,
            ),
            #widget.TaskList(
            #    background=COLORS.BACKGROUND,
            #    border=COLORS.PRIMARY,
            #    borderwidth=1,
            #    foreground=COLORS.DARK_FONT,
            #    highlight_method="block",
            #    rounded=False,
            #    spacing=1,
            #    title_width_method="uniform",
            #    txt_floating="~) ",
            #    txt_maximized="+) ",
            #    txt_minimized="-) ",
            #    unfocused_border=COLORS.DARK_PRIMARY,
            #    urgent_border=COLORS.LIGHT_URGENT,
            #),
            widget.Spacer(),
            # widget.Sep(
            #     background=COLORS.BACKGROUND,
            #     foreground=COLORS.LIGHT_BACKGROUND,
            #     linewidth=1,
            #     padding=3,
            #     size_percent=65,
            # ),
            # widget.Image(
            #     filename=brightness_icon(),
            #     margin=6,
            #     padding=0,
            # ),
            widget.TextBox(
                " "
            ),
            widget.Backlight(
                brightness_file="/sys/class/backlight/intel_backlight/subsystem/intel_backlight/brightness",
                max_brightness_file="/sys/class/backlight/intel_backlight/subsystem/intel_backlight/max_brightness",
                step=1,
                padding=0,
            ),
            # widget.Image(
            #     filename=volume_icon(),
            #     margin=6,
            # ),
            widget.TextBox(
                ""
            ),
            widget.PulseVolume(
                # theme_path="/usr/share/icons/Papirus-Dark/24x24/actions/audio-volume-muted.svg"
            ),
	    widget.Battery(
                charge_char=" ",
                discharge_char=" ",
                empty_char=" ",
                full_char=" ",
                format="{char} {percent:2.0%}",
                low_percent=0.15,
                notify_below=15,
                show_short_text=False,
            ),
            widget.Systray(),
            widget.Clock(
                timezone="Asia/Kolkata",
                format="%H:%M",
                update_interval=5.5,
            ),
            widget.WidgetBox(
                widgets=[
                    widget.TextBox(
                        "",
                        mouse_callback={
                            "Button2": lazy.spwan("sleep 3 & systemctl poweroff")  
                            }
                    ),
                    widget.TextBox(
                        "",
                        mouse_callback={
                            "Button2": lazy.spwan("sleep 3 & systemctl reboot")  
                            }
                    ),
                    widget.TextBox(
                        "",
                        mouse_callback={
                            "Button2": lazy.spwan("sleep 3 & systemctl hibernate")  
                            }
                    ),
                    widget.TextBox(
                        "",
                        mouse_callback={
                            "Button2": lazy.spwan("sleep 3 & systemctl suspend")  
                            }
                    ),
                    widget.TextBox(
                        "",
                        mouse_callback={
                            "Button2": lazy.spwan()  
                            }
                    ),
                    widget.TextBox(
                        "",
                        mouse_callback={
                            "Button2": lazy.shutdown()  
                            }
                    ),
                ],
                close_button_location='right',
                text_open="  ",
                text_closed="  ",
            ),
            widget.CurrentLayoutIcon(
                scale=0.7,
            ),
            widget.Sep(
                background=COLORS.BACKGROUND,
                foreground=COLORS.LIGHT_BACKGROUND,
                linewidth=3,
                padding=3,
                size_percent=80,
            ),
        ],
            size=25,
            background=COLORS.BACKGROUND,
            margin=0,
            opacity=0.85,
        )
    ),
    # Secondary Screen
    Screen(
        top=bar.Bar([
            widget.Sep(
                background=COLORS.BACKGROUND,
                foreground=COLORS.LIGHT_BACKGROUND,
                linewidth=3,
                padding=3,
                size_percent=80,
            ),
            widget.GroupBox(
                active=COLORS.LIGHT_PRIMARY,
                background=COLORS.BACKGROUND,
                block_highlight_text_color=COLORS.DARK_FONT,
                borderwidth=0,
                disable_drag=True,
                foreground=COLORS.LIGHT_FONT,
                inactive=COLORS.LIGHT_BACKGROUND,
                highlight_method="block",
                other_current_screen_border=COLORS.DARK_COMPLEMENTARY,
                other_screen_border=COLORS.DARK_PRIMARY,
                this_current_screen_border=COLORS.PRIMARY,
                this_screen_border=COLORS.COMPLEMENTARY,
                urgent_alert_method="block",
                urgent_border=COLORS.URGENT,
                urgent_text=COLORS.LIGHT_FONT,
                rounds=False,
            ),
            widget.Sep(
                background=COLORS.BACKGROUND,
                foreground=COLORS.LIGHT_BACKGROUND,
                linewidth=1,
                padding=3,
                size_percent=65,
            ),
            widget.Spacer(),
            # widget.TaskList(
            #     background=COLORS.BACKGROUND,
            #     border=COLORS.PRIMARY,
            #     borderwidth=1,
            #     foreground=COLORS.DARK_FONT,
            #     highlight_method="block",
            #     rounded=False,
            #     spacing=1,
            #     title_width_method="uniform",
            #     txt_floating="~) ",
            #     txt_maximized="+) ",
            #     txt_minimized="-) ",
            #     unfocused_border=COLORS.DARK_PRIMARY,
            #     urgent_border=COLORS.LIGHT_URGENT,
            # ),
            widget.Sep(
                background=COLORS.BACKGROUND,
                foreground=COLORS.LIGHT_BACKGROUND,
                linewidth=1,
                padding=3,
                size_percent=65,
            ),
            # widget.TextBox(
                # " ",
                # background=COLORS.COMPLEMENTARY,
                # foreground=COLORS.LIGHT_PRIMARY,
            # ),
            widget.BitcoinTicker(
                # background=COLORS.COMPLEMENTARY,
                # foreground=COLORS.LIGHT_FONT,
            ),
            widget.TextBox(
                " ",
                # background=COLORS.PRIMARY,
                # foreground=COLORS.DARK_FONT,
            ),
            widget.Memory(
                # background=COLORS.PRIMARY,
                # foreground=COLORS.DARK_FONT,
                format="{MemPercent}%"
            ),
            widget.TextBox(
                " ",
                # background=COLORS.COMPLEMENTARY,
                # foreground=COLORS.LIGHT_PRIMARY,
            ),
            widget.Memory(
                # background=COLORS.COMPLEMENTARY,
                # foreground=COLORS.LIGHT_FONT,
                format="{SwapPercent}%"
            ),
            widget.TextBox(
                " ",
                # background=COLORS.PRIMARY,
                # foreground=COLORS.DARK_FONT,
            ),
            widget.CPU(
                # background=COLORS.PRIMARY,
                # foreground=COLORS.DARK_FONT,
                format="{load_percent}%"
            ),
            widget.TextBox(
                " ",
                # background = COLORS.COMPLEMENTARY,
                # foreground = COLORS.LIGHT_PRIMARY,
            ),
            widget.ThermalSensor(
                # background=COLORS.COMPLEMENTARY,
                # foreground=COLORS.LIGHT_FONT,
                foreground_alert=COLORS.URGENT,
            ),
            widget.Clock(
                timezone="Asia/Kolkata",
                format="%H:%M",
                update_interval=5.5,
                # background=COLORS.PRIMARY,
                # foreground=COLORS.DARK_FONT,
            ),
            widget.CurrentLayoutIcon(
                # background=COLORS.COMPLEMENTARY,
                # foreground=COLORS.LIGHT_FONT,
                scale=0.7,
            ),
            widget.Sep(
                background=COLORS.BACKGROUND,
                foreground=COLORS.LIGHT_BACKGROUND,
                linewidth=3,
                padding=3,
                size_percent=80,
            ),
        ],
            size=25,
            background=COLORS.BACKGROUND,
            margin=0,
            opacity=0.85,
        )
    ),
]


# Drag floating layouts.
mouse = [
    Drag([MODKEY], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MODKEY], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MODKEY], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'Terminator Preferences'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    ],
    border_focus=COLORS.LIGHT_PRIMARY,
    border_normal=COLORS.LIGHT_COMPLEMENTARY,
)
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


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
    ]

    for p in processes:
        subprocess.Popen(p)
        print(f"succefully ran {' '.join(p)}")


@hook.subscribe.startup_complete
def wallpaper():
    subprocess.call(["/home/greenalien/.fehbg"])
