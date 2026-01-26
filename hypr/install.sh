#!/bin/sh
hypr_home=$HOME/.config/hypr

#_is_install() {
#    
#}

_install_config() {
    for file in hypr*; do
        if [[ -f $hypr_home/$file ]]; then
            rm $hypr_home/$file
        fi
        ln -sf $PWD/$file $hypr_home/$file
    done

    hyprctl reload
}

_install_hyprlock() {
    for file in hyprlock/*; do
        if [[ -f $hypr_home/$file ]]; then
            rm $hypr_home/$file
        fi
        ln -sf $PWD/$file $hypr_home/$file
    done

    hyprctl reload
}

_install_config
_install_hyprlock
