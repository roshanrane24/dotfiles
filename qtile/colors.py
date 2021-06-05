dynamic = True


class Colors:
    BLACK = "#000000"
    DARK_GRAY = "#212121"
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
    LIGHT_DEEP_PURPLE = "#B085F5"
    DEEP_PURPLE = "7E57C2"
    DARK_DEEP_PURPLE = "4D2C91"
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


if dynamic:
    from myFunctions import DynamicColors
    dc = DynamicColors()
    dark_primary, primary, light_primary = dc.get_colors()
else:
    dark_primary, primary, light_primary = (Colors.LIGHT_GREEN,
                                            Colors.GREEN,
                                            Colors.DARK_GREEN)


class COLORS:
    LIGHT_BACKGROUND = Colors.GRAY
    BACKGROUND = Colors.DARK_GRAY
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
