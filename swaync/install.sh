#!/bin/sh
__home=$HOME/.config/swaync

if [[ ! -d $__home ]]; then
    mkdir $__home
fi

#_is_install() {
#    
#}

_install_config() {
    for file in *.{json,css}; do
        if [[ -e $__home/$file ]]; then
            rm $__home/$file
        fi
        ln -sf $PWD/$file $__home/$file
    done
}
_install_config
