#!/bin/sh
hypr_home=$HOME/.config/hypr

#_is_install() {
#    
#}

_install_config() {
    for file in hypr*; do
        if [[ -e $hypr_home/$file ]]; then
            rm $hypr_home/$file
        fi
        ln -sf $PWD/$file $hypr_home/$file
    done

    hyprctl reload
}

_install_config
