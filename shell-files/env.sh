# >>> ls
export LS_COLORS="$(vivid generate jellybeans)"

# >>> Path
export PATH=$PATH:$HOME/.local/bin

# >>> Locale
export LC_ALL="en_US.UTF-8"


# >>> prompt
PS1='\e[32m\w\n\e[031m>\e[m '

# >>> qt-gtk theme
QT_QPA_PLATFORMTHEME=qt5ct

# Ignore These Commands in history
export HISTIGNORE=${HISTIGNORE:-"shutdown*:halt*:poweroff*:hibernate*:history*"}

