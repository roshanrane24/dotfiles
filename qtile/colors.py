from setting import DYNAMIC_COLORS, THEME
import os


class Colors:
    BLACK = "#000000"
    DARK_GRAY = "#212121"
    MATERIAL_GRAY = "#222222"
    GRAY = "#383838"
    LIGHT_RED = "#FF5131"
    RED = "#D50000"
    DARK_RED = "#9B0000"
    LIGHT_PINK = "#FA5788"
    PINK = "#C2185B"
    DARK_PINK = "#8C0032"
    LIGHT_PURPLE = "#C158DC"
    PURPLE = "#8E24AA"
    DARK_PURPLE = "#5C007A"
    LIGHT_VOILET = "#B085F5"
    VOILET = "#7E57C2"
    DARK_VOILET = "#4D2C91"
    LIGHT_INDIGO = "#757DE8"
    INDIGO = "#3F51B5"
    DARK_INDIGO = "#002984"
    LIGHT_BLUE = "#63A4FF"  # DARK
    BLUE = "#1976D2"  # LIGHT
    DARK_BLUE = "#004BA0"  # LIGHT
    LIGHT_GREEN = "#E4FF54"  # DARK
    GREEN = "#AEEA00"  # DARK
    DARK_GREEN = "#79B700"  # DARK
    WHITE = "#FFFFFF"


THEME_LIGHT, THEME_PRIMARY, THEME_DARK = {
    "Red": (Colors.LIGHT_RED, Colors.RED, Colors.DARK_RED),
    "Pink": (Colors.LIGHT_PINK, Colors.PINK, Colors.DARK_PINK),
    "Purple": (Colors.LIGHT_PURPLE, Colors.PURPLE, Colors.DARK_PURPLE),
    "Voilet": (Colors.LIGHT_VOILET, Colors.VOILET, Colors.DARK_VOILET),
    "Indigo": (Colors.LIGHT_INDIGO, Colors.INDIGO, Colors.DARK_INDIGO),
    "Blue": (Colors.LIGHT_BLUE, Colors.BLUE, Colors.DARK_BLUE),
    "Green": (Colors.LIGHT_GREEN, Colors.GREEN, Colors.DARK_GREEN),
                                          }[THEME]

if DYNAMIC_COLORS:
    from myFunctions import DynamicColors
    from myFunctions import set_theme
    dc = DynamicColors()
    dark_primary, primary, light_primary = dc.get_colors()
    set_theme(dc.primary_color)
else:
    dark_primary, primary, light_primary = (THEME_DARK,
                                            THEME_PRIMARY,
                                            THEME_LIGHT)
    with open(os.path.join(os.environ["HOME"], ".cache/dynamic-rofi.rasi"),
              'w') as css:
        lines = ["* {\n",
                 f"dark-primary: {dark_primary};\n",
                 f"dark-primary-trans: {dark_primary}44;\n",
                 f"dark-primary-trans1: {dark_primary}88;\n",
                 f"dark-primary-trans2: {dark_primary}BB;\n",
                 f"primary: {primary};\n",
                 f"primary-trans: {primary}44;\n",
                 f"primary-trans1: {primary}88;\n",
                 f"primary-trans2: {primary}BB;\n",
                 f"light-primary: {light_primary};\n",
                 f"light-primary-trans: {light_primary}44;\n",
                 f"light-primary-trans1: {light_primary}88;\n",
                 f"light-primary-trans2: {light_primary}BB;\n",
                 "}"]
        css.writelines(lines)


class COLORS:
    LIGHT_BACKGROUND = Colors.GRAY
    BACKGROUND = Colors.MATERIAL_GRAY
    DARK_BACKGROUND = Colors.BLACK
    LIGHT_PRIMARY = light_primary
    PRIMARY = primary
    DARK_PRIMARY = dark_primary
    LIGHT_COMPLEMENTARY = Colors.LIGHT_PINK
    COMPLEMENTARY = Colors.PINK
    DARK_COMPLEMENTARY = Colors.DARK_PINK
    LIGHT_URGENT = Colors.LIGHT_RED
    URGENT = Colors.RED
    DARK_URGENT = Colors.DARK_RED
    LIGHT_FONT = Colors.WHITE
    DARK_FONT = Colors.BLACK
