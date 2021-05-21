import os
from libqtile.utils import guess_terminal
from colors import COLORS
# Applications
TERMINAL = guess_terminal()
BROWSER = "brave"
FILE_MANAGER = "dolphin"
FILE_MANAGER_2 = ""
EDITOR_GUI = ""
MODKEY = "mod4"

# Enviroment
HOME = os.environ["HOME"]
CONFIG = os.path.join(HOME, ".config")
SCRIPTS = os.path.join(CONFIG, "shell-files")

# Config
bar_config = {
    "size": 25,
    "background": COLORS.BACKGROUND,
    "margin": 0,
    "opacity": 0.99,
}

# Worspaces/Group
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

floating_rules = [
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'kvms pro.exe'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wmclass': 'QML Timer'},  # Pilorama
    {'wmclass': 'polkit-kde-authentication-agent-1'},  # Pilorama
    {'wmclass': 'kdialog'},  # Pilorama
    {'wmclass': 'kdesu'},  # Pilorama
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'Terminator Preferences'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wname': 'Confirm'},  # GPG key password entry
    {'wname': 'Tip of the Day'},  # GPG key password entry
    {'wname': 'Confirm Exit'},  # GPG key password entry
    {'wname': 'Copying files'},  # GPG key password entry
    {'wname': 'Save File'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
]

