#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

## ENV
QT_QPA_PLATFORM=qt5ct
export WALLPAPER='~/Pictures/EarthPlasma2NoLogo.png'
