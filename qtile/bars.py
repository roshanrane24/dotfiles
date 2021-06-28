from libqtile import bar, widget, qtile
from colors import COLORS
from setting import bar_config


widget_background = COLORS.BACKGROUND
widget_foreground = COLORS.PRIMARY
bar_background = COLORS.BACKGROUND


# Common Widgets
end_sep = widget.Sep(
    background=widget_background,
    foreground=COLORS.LIGHT_BACKGROUND,
    linewidth=1,
    padding=3,
    size_percent=80,
    )
mid_sep = widget.Sep(
    background=widget_background,
    foreground=COLORS.LIGHT_BACKGROUND,
    linewidth=1,
    padding=3,
    margin=5,
    size_percent=65,
    )

clock = widget.Clock(
    timezone="Asia/Kolkata",
    background=widget_background,
    foreground=widget_foreground,
    font='SpaceMono Nerd Font',
    format="%a %d %b %Y %H:%M",
    update_interval=5.5,
    )

# Primary screen widget
main_screen_bar = bar.Bar([
    # End Separator
    end_sep,
    # Group Box
    widget.GroupBox(
        active=COLORS.DARK_PRIMARY,
        background=widget_background,
        block_highlight_text_color=COLORS.PRIMARY,
        borderwidth=3,
        center_aligned=True,
        disable_drag=True,
        font='Font Awesome 5 Free,Font Awesome 5 Free Regular',
        foreground=COLORS.LIGHT_FONT,                      # For unused groups
        hide_unused=True,
        highlight_color=[COLORS.BACKGROUND],
        highlight_method="line",
        inactive=COLORS.LIGHT_BACKGROUND,
        # Inactive Screen Bar > Active Screen Group
        other_current_screen_border=COLORS.DARK_PRIMARY,
        # Inactive Screen Bar > Inactive Screen Group
        other_screen_border=COLORS.DARK_PRIMARY,
        # Active Screen Bar > Active Screen Group
        this_current_screen_border=COLORS.LIGHT_PRIMARY,
        # Active Screen Bar > Inactive Screen Group
        this_screen_border=COLORS.PRIMARY,
        urgent_alert_method="block",
        urgent_border=COLORS.URGENT,
        urgent_text=COLORS.LIGHT_FONT,
        rounds=False,
    ),
    mid_sep,
    # widget.CurrentLayoutIcon(
        # scale=0.6,
        # background=widget_background,
        # foreground=widget_foreground
    # ),
    widget.CurrentLayout(
        background=widget_background,
        foreground=widget_foreground
    ),
    mid_sep,
    # widget.CurrentScreen(
        # active_color=COLORS.PRIMARY,
        # active_text="",
        # inactive_color=COLORS.BACKGROUND,
        # inactive_text="ﴹ",
        # font='SpaceMono Nerd Font Mono',
        # background=widget_background,
        # fontsize=25
    # ),
    widget.WindowCount(
        background=widget_background,
        foreground=widget_foreground,
        font='SpaceMono Nerd Font'
    ),
    mid_sep,
    widget.Spacer(),
    mid_sep,
    widget.Backlight(
        brightness_file="/sys/class/backlight/intel_backlight/brightness",
        max_brightness_file="/sys/class/backlight/intel_backlight/"\
                            "max_brightness",
        step=2,
        padding=5,
        font='SpaceMono Nerd Font',
        background=widget_background,
        foreground=widget_foreground,
        format=' {percent:2.0%}'
    ),
    mid_sep,
    widget.PulseVolume(
        background=widget_background,
        foreground=widget_foreground,
        # theme_path='/usr/share/icons/Papirus-Dark/22x22/panel/',
        emoji=True,
        font='SpaceMono Nerd Font',
        padding=2,
        update_interval=0.1
    ),
    widget.PulseVolume(
        background=widget_background,
        foreground=widget_foreground,
        font='SpaceMono Nerd Font',
        padding=5,
        update_interval=0.1
    ),
    mid_sep,
    widget.Wlan(
        background=widget_background,
        foreground=widget_foreground,
        disconnected_message="睊",
        font='SpaceMono Nerd Font',
        format="{essid} {quality}"
    ),
    mid_sep,
    widget.BatteryIcon(
        background=widget_background,
        foreground=widget_foreground,
        update_interval=20,
        # theme_path='/usr/share/icons/Papirus-Dark/16x16/panel',
        theme_path='/usr/share/icons/Flat-Remix-Green-Dark/panel',
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
        background=widget_background,
        foreground=widget_foreground,
        font='SpaceMono Nerd Font',
        padding=0,
    ),
    mid_sep,
    widget.Systray(
        background=widget_background,
        foreground=widget_foreground,
        icon_size=25,
        padding=0
    ),
    mid_sep,
    clock,
    mid_sep,
    widget.TextBox(
        '',
        background=widget_background,
        foreground=widget_foreground,
        font='SpaceMono Nerd Font',
        mouse_callbacks={
            'Button1': lambda: qtile.cmd_spawn(
                "sh -c '~/.config/dunst/scripts/notification-center'"
            )
        },
        padding=7
    ),
    end_sep,
    ],
    background=bar_background,
    **bar_config,
)

second_screen_bar = bar.Bar([
    end_sep,
    widget.GroupBox(
        active=COLORS.DARK_PRIMARY,
        background=widget_background,
        block_highlight_text_color=COLORS.PRIMARY,
        borderwidth=3,
        center_aligned=True,
        disable_drag=True,
        font='Font Awesome 5 Free,Font Awesome 5 Free Regular',
        foreground=COLORS.LIGHT_FONT,                      # For unused groups
        hide_unused=True,
        highlight_color=[COLORS.BACKGROUND],
        highlight_method="line",
        inactive=COLORS.LIGHT_BACKGROUND,
        # Inactive Screen Bar > Active Screen Group
        other_current_screen_border=COLORS.DARK_PRIMARY,
        # Inactive Screen Bar > Inactive Screen Group
        other_screen_border=COLORS.DARK_PRIMARY,
        # Active Screen Bar > Active Screen Group
        this_current_screen_border=COLORS.LIGHT_PRIMARY,
        # Active Screen Bar > Inactive Screen Group
        this_screen_border=COLORS.PRIMARY,
        urgent_alert_method="block",
        urgent_border=COLORS.URGENT,
        urgent_text=COLORS.LIGHT_FONT,
        rounds=False,
    ),
    mid_sep,
    # widget.CurrentLayoutIcon(
        # scale=0.6,
        # background=widget_background
    # ),
    widget.CurrentLayout(
        background=widget_background,
        foreground=widget_foreground
    ),
    mid_sep,
    # widget.CurrentScreen(
        # active_color=COLORS.PRIMARY,
        # active_text="",
        # inactive_color=COLORS.BACKGROUND,
        # inactive_text="ﴹ",
        # font='SpaceMono Nerd Font Mono',
        # background=widget_background,
        # fontsize=25
    # ),
    widget.WindowCount(
        background=widget_background,
        foreground=widget_foreground,
        font='SpaceMono Nerd Font'
    ),
    mid_sep,
    widget.Spacer(),
     mid_sep,
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
        background=widget_background,
        foreground=widget_foreground,
        font='SpaceMono Nerd Font',
    ),
    mid_sep,
    widget.Memory(
        format=" {MemPercent}%",
        background=widget_background,
        foreground=widget_foreground,
        font='Font Awesome 5 Free,Font Awesome 5 Free Regular'
    ),
    mid_sep,
    widget.Memory(
        format=" {SwapPercent}%",
        background=widget_background,
        foreground=widget_foreground,
        font='SpaceMono Nerd Font',
    ),
    mid_sep,
    widget.ThermalSensor(
        font='SpaceMono Nerd Font',
        background=widget_background,
        foreground=widget_foreground,
        foreground_alert=COLORS.URGENT,
        threshold=59
    ),
    mid_sep,
    widget.HDDBusyGraph(
        background=widget_background,
        foreground=widget_foreground,
        font='SpaceMono Nerd Font',
        border_color=COLORS.DARK_PRIMARY,
        fill_color=COLORS.DARK_PRIMARY,
        graph_color=COLORS.LIGHT_PRIMARY,
        border_width=1,
        linewidth=0,
        margin_y=1,
    ),
    mid_sep,
    clock,
    mid_sep,
    widget.TextBox(
        '',
        background=widget_background,
        foreground=widget_foreground,
        font='SpaceMono Nerd Font',
        mouse_callbacks={
            'Button1': lambda: qtile.cmd_spawn(
                "zsh -c '~/.config/dunst/scripts/notification-center'"
            )
        },
        padding=7
    ),
    end_sep,
    ],
    **bar_config,
    background=bar_background
)
