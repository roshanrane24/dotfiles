from libqtile import layout
from libqtile.config import Screen
from setting import floating_rules
from colors import COLORS
from bars import main_screen_bar, second_screen_bar
from functions import Display


layouts = [
    layout.Bsp(
        border_focus=COLORS.LIGHT_PRIMARY,
        border_normal=COLORS.DARK_PRIMARY,
        border_width=1,
        fair=True,
        grow_amount=2,
        low_right=False,
        margin=4,
    ),
    layout.Max(),
    layout.MonadTall(
        border_focus=COLORS.LIGHT_PRIMARY,
        border_normal=COLORS.DARK_PRIMARY,
        border_width=1,
        change_size=4,
        margin=3,
        single_border_width=0,
        single_margin=0,
    ),
    layout.MonadWide(
        border_focus=COLORS.LIGHT_PRIMARY,
        border_normal=COLORS.DARK_PRIMARY,
        border_width=1,
        change_size=4,
        margin=2,
        single_border_width=0,
        single_margin=0,
    ),
    layout.RatioTile(
        border_focus=COLORS.LIGHT_PRIMARY,
        border_normal=COLORS.DARK_PRIMARY,
        border_width=1,
        margin=1,
    ),
    layout.TreeTab(
        active_bg=COLORS.LIGHT_PRIMARY,
        active_fg=COLORS.DARK_FONT,
        bg_color=COLORS.BACKGROUND,
        border_width=0,
        inactive_bg=COLORS.DARK_PRIMARY,
        inactive_fg=COLORS.LIGHT_FONT,
        level_shift=4,
        margin_y=18,
        padding_left=0,
        padding_y=9,
        pannel_width=199,
        previous_on_rm=True,
        sections=["Main", "Extra"],
        section_bottom=9,
        section_fg=COLORS.LIGHT_BACKGROUND,
        section_fontsize=14,
        section_left=19,
        section_padding=19,
        section_top=19,
        urgent_bg=COLORS.URGENT,
        urgent_fg=COLORS.LIGHT_FONT,
        vspace=4,
    ),
]


floating_layout = layout.Floating(
    float_rules=floating_rules,
    border_focus=COLORS.LIGHT_PRIMARY,
    border_normal=COLORS.DARK_PRIMARY,
    border_width=3,
)

screens_created = [Screen(top=main_screen_bar)]


def add_screen(screens):
    display = Display()
    if display.get_connect_display_count() > 1:
        if len(screens) < display.get_connect_display_count():
            for _ in range(1, display.get_connect_display_count()):
                screens.append(Screen(top=second_screen_bar))


def remove_screen(screens):
    display = Display()
    if display.get_connect_display_count() < len(screens):
        screens = screens[:display.get_connect_display_count()]


add_screen(screens=screens_created)
