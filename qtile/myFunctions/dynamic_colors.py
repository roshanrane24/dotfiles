import os
import json
import configparser
from typing import Any
from numpy import array, float64, ndarray
from dominant_colors import DominantColors
from dominant_colors.utils import Colors

HOME = os.environ["HOME"]


class DynamicColors:
    CACHE: str = os.path.join(HOME, ".cache/dynamicaccent")
    CSS: str = os.path.join(HOME, ".cache/dynamic-rofi.rasi")

    def __init__(self):
        self.cache: Any = None
        self.wallpaper = DynamicColors.get_wallpaper_path()
        self.is_cache: bool = self.check_cache()
        if not self.is_cache:
            self.dominant: DominantColors = DominantColors(self.wallpaper,
                                                           no_of_colors=3)
            self.primary_color: ndarray = self.get_primary()

    def get_colors(self) -> ndarray:
        if self.is_cache:
            self.primary_color = array(list(self.cache.values())[1])
            return array(list(self.cache.values())[0])
        else:
            colors: ndarray = self.get_hex_varient()
            self.write_cache(self.wallpaper, colors, self.primary_color)
            self.is_cache: bool = self.check_cache()
            return colors

    def check_cache(self) -> bool:
        if os.path.exists(DynamicColors.CACHE):
            with open(DynamicColors.CACHE, 'r') as cache:
                self.cache = json.load(cache)
                if self.wallpaper in self.cache.keys():
                    return True
                else:
                    return False
        else:
            return False

    @classmethod
    def write_cache(cls, path: str, colors: ndarray, primary: ndarray) -> None:
        with open(cls.CACHE, 'w') as cache:
            json.dump({path: colors.tolist(),
                       "Primary": primary.astype(int).tolist()},
                      cache)

        with open(cls.CSS, 'w') as css:
            lines = ["* {\n",
                     f"dark-primary: {colors[0]};\n",
                     f"dark-primary-trans: {colors[0]}44;\n",
                     f"dark-primary-trans1: {colors[0]}88;\n",
                     f"dark-primary-trans2: {colors[0]}BB;\n",
                     f"primary: {colors[1]};\n",
                     f"primary-trans: {colors[1]}44;\n",
                     f"primary-trans1: {colors[1]}88;\n",
                     f"primary-trans2: {colors[1]}BB;\n",
                     f"light-primary: {colors[2]};\n",
                     f"light-primary-trans: {colors[2]}44;\n",
                     f"light-primary-trans1: {colors[2]}88;\n",
                     f"light-primary-trans2: {colors[2]}BB;\n",
                     "}"]
            css.writelines(lines)

    @staticmethod
    def get_wallpaper_path() -> str:
        with open(os.path.join(HOME, ".fehbg"), 'r') as wall:
            return wall.readlines()[-1].split(' ')[-1].strip()[1:-1]

    def get_primary(self) -> ndarray:
        if self.cache:
            self.dominant: DominantColors = DominantColors(self.wallpaper)
        return self.dominant.colors[0]

    @staticmethod
    def get_variants(primary: ndarray) -> ndarray:
        H, S, L = Colors.rgb2hsl(primary).astype(float64)

        if S < 20:
            S = 20

        if L < 30:
            L = 25
            light = array([H, S, L])
            primary = array([H, S, L + 20])
            dark = array([H, S, L + 40])
        elif L < 65:
            light = array([H, S, L - 15])
            primary = array([H, S, L])
            dark = array([H, S, L + 15])
        else:
            light = array([H, S, L - 30])
            primary = array([H, S, L - 15])
            dark = array([H, S, L])

        return array([light, primary, dark])

    def get_hex_varient(self):
        varients = self.get_variants(self.primary_color)
        return array([Colors.hsl2hex(varients[0]),
                      Colors.hsl2hex(varients[1]),
                      Colors.hsl2hex(varients[2])])


def set_theme(primary: ndarray) -> None:
    primary = Colors.rgb2hsl(primary)
    theme: ndarray = get_theme(primary)
    change_config(theme)


def get_theme(primary: ndarray) -> ndarray:
    H, S, _ = primary
    H = round(H / 30)

    if S < 25:
        return array(["Flat-Remix-GTK-Blue-Dark", "Flat-Remix-Grey-Dark"])
    else:
        return {0: array(["Flat-Remix-GTK-Red-Dark",
                          "Flat-Remix-Red-Dark"]),
                1: array(["Flat-Remix-GTK-Yellow-Dark",
                          "Flat-Remix-Orange-Dark"]),
                2: array(["Flat-Remix-GTK-Yellow-Dark",
                          "Flat-Remix-Yellow-Dark"]),
                3: array(["Flat-Remix-GTK-Green-Dark",
                          "Flat-Remix-Green-Dark"]),
                4: array(["Flat-Remix-GTK-Green-Dark",
                          "Flat-Remix-Green-Dark"]),
                5: array(["Flat-Remix-GTK-Green-Dark",
                          "Flat-Remix-Teal-Dark"]),
                6: array(["Flat-Remix-GTK-Blue-Dark",
                          "Flat-Remix-Cyan-Dark"]),
                7: array(["Flat-Remix-GTK-Blue-Dark",
                          "Flat-Remix-Blue-Dark"]),
                8: array(["Flat-Remix-GTK-Blue-Dark",
                          "Flat-Remix-Blue-Dark"]),
                9: array(["Flat-Remix-GTK-Blue-Dark",
                          "Flat-Remix-Violet-Dark"]),
                10: array(["Flat-Remix-GTK-Red-Dark",
                           "Flat-Remix-Magenta-Dark"]),
                11: array(["Flat-Remix-GTK-Red-Dark",
                           "Flat-Remix-Magenta-Dark"]),
                12: array(["Flat-Remix-GTK-Red-Dark",
                           "Flat-Remix-Red-Dark"])}[H]


def change_config(theme: ndarray) -> None:
    qt = os.path.join(HOME, '.config/qt5ct/qt5ct.conf')
    gtk = os.path.join(HOME, '.config/gtk-3.0/settings.ini')
    gtk2 = os.path.join(HOME, '.gtkrc-2.0')

    # QT
    try:
        qt5ct = configparser.ConfigParser()
        qt5ct.read(qt)
        qt5ct['Appearance']['icon_theme'] = theme[1]

        with open(qt, 'w') as qtw:
            qt5ct.write(qtw)
    except Exception as e:
        print("Exception:", e)

    # GTK
    try:
        gtk_settings = configparser.ConfigParser()
        gtk_settings.read(gtk)
        gtk_settings['Settings']['gtk-icon-theme-name'] = theme[1]
        gtk_settings['Settings']['gtk-theme-name'] = theme[0]

        with open(gtk, 'w') as gtkw:
            gtk_settings.write(gtkw)
    except Exception as e:
        print("Exception:", e)

    with open(gtk2, 'r') as file:
        newlines = []
        for line in file.readlines():
            if line.split('=')[0] == 'gtk-theme-name':
                x = line.split('=')
                x[1] = f'"{theme[0]}"\n'
                newlines.append('='.join(x))
            elif line.split('=')[0] == 'gtk-icon-theme-name':
                x = line.split('=')
                x[1] = f'"{theme[1]}"\n'
                newlines.append('='.join(x))
            else:
                newlines.append(line)

    with open(gtk2, 'w') as gtk2w:
        gtk2w.writelines(newlines)
