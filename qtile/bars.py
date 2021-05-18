from libqtile import widget, bar, qtile
#from libqtile.lazy import lazy
from .colors import COLORS
from .setting import bar_config

# Common Widgets
end_sep = widget.Sep(
    background=COLORS.BACKGROUND,
    foreground=COLORS.LIGHT_BACKGROUND,
    linewidth=3,
    padding=3,
    size_percent=80,
    )
mid_sep = widget.Sep(
    background=COLORS.BACKGROUND,
    foreground=COLORS.LIGHT_BACKGROUND,
    linewidth=1,
    padding=3,
    size_percent=65,
    )

# tasklist = widget.TaskList(
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
#     )

clock = widget.Clock(
    timezone="Asia/Kolkata",
    format="%H:%M",
    update_interval=5.5,
    )

# Primary screen widget
main_screen_bar = bar.Bar([
    end_sep,
    widget.GroupBox(
    active=COLORS.LIGHT_PRIMARY,
    background=COLORS.BACKGROUND,
    block_highlight_text_color=COLORS.DARK_FONT,
    borderwidth=0,
    disable_drag=True,
    foreground=COLORS.LIGHT_FONT,
    hide_unused=True,
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
    mid_sep,
    widget.Spacer(),
    widget.TextBox(
        " "
    ),
    widget.Backlight(
        brightness_file="/sys/class/backlight/intel_backlight/subsystem/intel_backlight/brightness",
        max_brightness_file="/sys/class/backlight/intel_backlight/subsystem/intel_backlight/max_brightness",
        step=1,
        padding=0,
    ),
    widget.TextBox(
        ""
    ),
    widget.PulseVolume(),
    widget.Wlan(
        disconnected_message="xxx",

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
    clock,
    widget.LaunchBar(
        [('', 'wlogout', 'Wayland Logout Menu')]
    ),
    widget.CurrentLayoutIcon(
    scale=0.7
    ),
    end_sep,
    ],
    **bar_config
)

second_screen_bar = bar.Bar([
    end_sep,
    widget.GroupBox(
        active=COLORS.LIGHT_PRIMARY,
        background=COLORS.BACKGROUND,
        block_highlight_text_color=COLORS.DARK_FONT,
        borderwidth=0,
        disable_drag=True,
        foreground=COLORS.LIGHT_FONT,
        hide_unused=True,
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
    mid_sep,
    widget.Spacer(),
    mid_sep,
    widget.HDDBusyGraph(
    border_color=COLORS.LIGHT_FONT,
    fill_color=COLORS.LIGHT_COMPLEMENTARY,
    graph_color=COLORS.PRIMARY,
    border_width=1,
    ),
    widget.BitcoinTicker(),
    widget.TextBox(
        " ",
    ),
    widget.Memory(
        format="{MemPercent}%"
    ),
    widget.TextBox(
        " ",
    ),
    widget.Memory(
        format="{SwapPercent}%"
    ),
    widget.TextBox(
        " ",
    ),
    widget.CPU(
        format="{load_percent}%"
    ),
    widget.TextBox(
        " ",
    ),
    widget.ThermalSensor(
        foreground_alert=COLORS.URGENT,
    ),
    clock,
    widget.CurrentLayoutIcon(
    scale=0.7
    ),
    end_sep,
    ],
    **bar_config
)
