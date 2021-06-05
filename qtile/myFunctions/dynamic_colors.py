import os
import json
from typing import Any
from numpy import array, float64, ndarray
from dominant_colors import DominantColors
from dominant_colors.utils import Colors

HOME = os.environ["HOME"]


class DynamicColors:
    CACHE: str = os.path.join(HOME, ".cache/dynamicaccent")

    def __init__(self):
        self.cache: Any = None
        self.wallpaper = DynamicColors.get_wallpaper_path()
        self.is_cache: bool = self.check_cache()
        if not self.is_cache:
            self.dominant: DominantColors = DominantColors(self.wallpaper,
                                                           no_of_colors=3)
            self.primary_color: ndarray = self.get_primary()
            with open(DynamicColors.CACHE+"primary", 'w') as fp:
                json.dump({"primary": list(self.primary_color)}, fp)

    def get_colors(self) -> ndarray:
        if self.is_cache:
            return array(list(self.cache.values())[0])
        else:
            colors: ndarray = self.get_hex_varient()
            self.write_cache(self.wallpaper, colors)
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
    def write_cache(cls, path: str, colors: ndarray) -> None:
        with open(cls.CACHE, 'w') as cache:
            json.dump({path: colors.tolist()}, cache)

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
