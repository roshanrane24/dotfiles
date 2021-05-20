from libqtile import bar, widget, qtile
from colors import COLORS
from setting import bar_config

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

clock = widget.Clock(
    timezone="Asia/Kolkata",
    background=COLORS.LIGHT_BACKGROUND,
    font='SpaceMono Nerd Font',
    foreground=COLORS.LIGHT_FONT,
    format="%H:%M",
    update_interval=5.5,
    )

# Primary screen widget
main_screen_bar = bar.Bar([
    # End Separator
    end_sep,
    # Group Box
    widget.GroupBox(
        active=COLORS.LIGHT_PRIMARY,
        background=COLORS.LIGHT_BACKGROUND,
        block_highlight_text_color=COLORS.DARK_FONT,
        borderwidth=0,
        disable_drag=True,
        foreground=COLORS.LIGHT_FONT,                      # For unused groups
        hide_unused=True,
        inactive=COLORS.LIGHT_BACKGROUND,
        highlight_method="block",
        # Inactive Screen Bar > Active Screen Group
        other_current_screen_border=COLORS.DARK_PRIMARY,
        # Inactive Screen Bar > Inactive Screen Group
        other_screen_border=COLORS.DARK_PRIMARY,
        # Active Screen Bar > Active Screen Group
        this_current_screen_border=COLORS.PRIMARY,
        # Active Screen Bar > Inactive Screen Group
        this_screen_border=COLORS.LIGHT_PRIMARY,
        urgent_alert_method="block",
        urgent_border=COLORS.URGENT,
        urgent_text=COLORS.LIGHT_FONT,
        rounds=False,
        font='Font Awesome 5 Free,Font Awesome 5 Free Regular'
    ),
    mid_sep,
    widget.CurrentLayoutIcon(
        scale=0.6,
        background=COLORS.LIGHT_BACKGROUND
    ),
    mid_sep,
    widget.CurrentScreen(
        active_color=COLORS.PRIMARY,
        active_text="",
        inactive_color=COLORS.URGENT,
        inactive_text="ﴹ",
        font='SpaceMono Nerd Font Mono',
        background=COLORS.LIGHT_BACKGROUND,
        fontsize=25
    ),
    mid_sep,
    widget.WindowCount(
        background=COLORS.LIGHT_BACKGROUND,
        foreground=COLORS.LIGHT_FONT,
        font='SpaceMono Nerd Font'
    ),
    mid_sep,
    widget.Spacer(),
    widget.Backlight(
        brightness_file="/sys/class/backlight/intel_backlight/brightness",
        max_brightness_file="/sys/class/backlight/intel_backlight/"\
                            "max_brightness",
        step=2,
        padding=5,
        font='SpaceMono Nerd Font',
        background=COLORS.LIGHT_BACKGROUND,
        format=' {percent:2.0%}'
    ),
    mid_sep,
    widget.PulseVolume(
        background=COLORS.LIGHT_BACKGROUND,
        emoji=True,
        font='SpaceMono Nerd Font',
        foreground=COLORS.LIGHT_FONT,
        padding=2,
        update_interval=0.1
    ),
    widget.PulseVolume(
        background=COLORS.LIGHT_BACKGROUND,
        font='SpaceMono Nerd Font',
        padding=5,
        update_interval=0.1
    ),
    mid_sep,
    widget.Wlan(
        disconnected_message="睊",
        background=COLORS.LIGHT_BACKGROUND,
        font='SpaceMono Nerd Font',
        format="{essid} {quality}"
    ),
    mid_sep,
    widget.BatteryIcon(
        update_interval=20,
        background=COLORS.LIGHT_BACKGROUND,
        theme_path='/usr/share/icons/Papirus-Dark/16x16/panel',
    ),
    widget.Battery(
        # charge_char=" ",
        # discharge_char=" ",
        # empty_char=" ",
        # full_char=" ",
        format="{percent:2.0%}",
        # low_percent=0.15,
        # notify_below=15,
        # show_short_text=False,
        background=COLORS.LIGHT_BACKGROUND,
        font='SpaceMono Nerd Font',
        padding=0,
    ),
    mid_sep,
    widget.Systray(
        background=COLORS.LIGHT_BACKGROUND,
        icon_size=25,
        padding=0
    ),
    mid_sep,
    clock,
    mid_sep,
    widget.TextBox(
        '',
        background=COLORS.LIGHT_BACKGROUND,
        font='SpaceMono Nerd Font',
        mouse_callbacks={
            'Button1': lambda: qtile.cmd_spawn(
                "zsh -c 'kill -s USR1 $(pidof deadd-notification-center)'"
            )
        },
        padding=7
    ),
    end_sep,
    ],
    **bar_config
)

second_screen_bar = bar.Bar([
    end_sep,
    widget.GroupBox(
        active=COLORS.LIGHT_PRIMARY,
        background=COLORS.LIGHT_BACKGROUND,
        block_highlight_text_color=COLORS.DARK_FONT,
        borderwidth=0,
        disable_drag=True,
        foreground=COLORS.LIGHT_FONT,                      # For unused groups
        hide_unused=True,
        inactive=COLORS.LIGHT_BACKGROUND,
        highlight_method="block",
        # Inactive Screen Bar > Active Screen Group
        other_current_screen_border=COLORS.DARK_PRIMARY,
        # Inactive Screen Bar > Inactive Screen Group
        other_screen_border=COLORS.DARK_PRIMARY,
        # Active Screen Bar > Active Screen Group
        this_current_screen_border=COLORS.PRIMARY,
        # Active Screen Bar > Inactive Screen Group
        this_screen_border=COLORS.LIGHT_PRIMARY,
        urgent_alert_method="block",
        urgent_border=COLORS.URGENT,
        urgent_text=COLORS.LIGHT_FONT,
        rounds=False,
        font='Font Awesome 5 Free,Font Awesome 5 Free Regular'
    ),
    mid_sep,
    widget.CurrentLayoutIcon(
        scale=0.6,
        background=COLORS.LIGHT_BACKGROUND
    ),
    mid_sep,
    widget.CurrentScreen(
        active_color=COLORS.PRIMARY,
        active_text="",
        inactive_color=COLORS.URGENT,
        inactive_text="ﴹ",
        font='SpaceMono Nerd Font Mono',
        background=COLORS.LIGHT_BACKGROUND,
        fontsize=25
    ),
    mid_sep,
    widget.WindowCount(
        background=COLORS.LIGHT_BACKGROUND,
        foreground=COLORS.LIGHT_FONT,
        font='SpaceMono Nerd Font'
    ),
    mid_sep,
    widget.Spacer(),
    # mid_sep,
    # widget.WidgetBox(
    #     widget=[widget.BitcoinTicker(font='SpaceMono Nerd Font',
    #             background=COLORS.LIGHT_BACKGROUND,
    #             foreground=COLORS.LIGHT_FONT,),
    #             widget.TextBox(text="THIS IS IT")
    #             ],
    #     close_button_location='right',
    #     background=COLORS.LIGHT_BACKGROUND,
    #     font='SpaceMono Nerd Font',
    #     text_closed="  ",
    #     text_open=" ﲒ ",
    #     padding=10
    # ),
    # mid_sep,
    widget.CPU(
        format=" {load_percent}%",
        background=COLORS.LIGHT_BACKGROUND,
        font='SpaceMono Nerd Font',
    ),
    mid_sep,
    widget.Memory(
        format=" {MemPercent}%",
        background=COLORS.LIGHT_BACKGROUND,
        font='Font Awesome 5 Free,Font Awesome 5 Free Regular'
    ),
    mid_sep,
    widget.Memory(
        format=" {SwapPercent}%",
        background=COLORS.LIGHT_BACKGROUND,
        font='SpaceMono Nerd Font',
    ),
    mid_sep,
    widget.ThermalSensor(
        font='SpaceMono Nerd Font',
        background=COLORS.LIGHT_BACKGROUND,
        foreground_alert=COLORS.URGENT,
        tag_sensor="Package id 0",
        threshold=59
    ),
    mid_sep,
    widget.HDDBusyGraph(
        background=COLORS.LIGHT_BACKGROUND,
        font='SpaceMono Nerd Font',
        border_color=COLORS.LIGHT_FONT,
        fill_color=COLORS.LIGHT_URGENT,
        graph_color=COLORS.PRIMARY,
        border_width=1,
        linewidth=1,
        margin_y=1,
    ),
    mid_sep,
    clock,
    mid_sep,
    widget.TextBox(
        '',
        background=COLORS.LIGHT_BACKGROUND,
        font='SpaceMono Nerd Font',
        mouse_callbacks={
            'Button1': lambda: qtile.cmd_spawn(
                "zsh -c 'kill -s USR1 $(pidof deadd-notification-center)'"
            )
        },
        padding=7
    ),
    end_sep,
    ],
    **bar_config
)
