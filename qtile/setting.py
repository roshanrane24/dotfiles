import os
from libqtile import layout
from libqtile.config import Match
from libqtile.utils import guess_terminal


# Set
SCREEN: str = 'extend'  # extend, mirror
DYNAMIC_COLORS: bool = True
ROFI_THEME='lime-amber'
if DYNAMIC_COLORS:
  ROFI_THEME='qtile-dynamic-clear'

# Applications
TERMINAL = guess_terminal()
BROWSER = "brave"
FILE_MANAGER = "dolphin"
FILE_MANAGER_2 = "nautilus"
EDITOR_GUI = ""
MODKEY = "mod4"

# Enviroment
HOME = os.environ["HOME"]
CONFIG = os.path.join(HOME, ".config")
SCRIPTS = os.path.join(CONFIG, "shell-files")

# Config
bar_config = {
    "size": 25,
    "margin": 0,
    "opacity": 1,
    "font": "Space Mono"
}

# Worspaces/Group
workspaces = {
    "1": {"label": "",
          "matches": {"wm_class": ["Terminator", "Alacritty"]}},
    "2": {"label": "",
          "matches": {"wm_class": ["Brave-browser", "Chromium"]}},
    "3": {"label": "",
          "matches": {"wm_class": ["Thunar", "dolphin"]}},
    "4": {"label": "",
          "matches": {"wm_class": ["code-oss", "jetbrains-pycharm-ce"]}},
    "5": {"label": "",
          "matches": {"wm_class": ["mpv", "vlc"]}},
    "6": {"label": "",
          "matches": {"wm_class": ["Spotify", "spotify"]}},
    "7": {"label": "",
          "matches": {"wm_class": ["Discord"]}},
    "8": {"label": "",
          "matches": {"wm_class": ["qBittorrent", "qbittorrent"]}},

    "9": {"label": "1",
          "matches": None},
    "0": {"label": "2",
          "matches": None}
              }

floating_rules = [*layout.Floating.default_float_rules,
                  Match(wm_class='Pulseeffects'),
                  Match(wm_class='kvms pro.exe'),
                  Match(wm_class='confirmreset'),
                  Match(wm_class='makebranch'),
                  Match(wm_class='maketag'),
                  Match(wm_class='QML Timer'),
                  Match(wm_class='polkit-kde-authentication-agent-1'),
                  Match(wm_class='kdialog'),
                  Match(wm_class='kdesu'),
                  Match(wm_class='ssh-askpass'),
                  Match(title='branchdialog'),
                  Match(title='Terminator Preferences'),
                  Match(title='pinentry'),
                  Match(title='Confirm'),
                  Match(title='Tip of the Day'),
                  Match(title='Confirm Exit'),
                  Match(title='Copying files'),
                  Match(title='Save File'),
                  Match(title='Delete Permanently'),
                  ]
