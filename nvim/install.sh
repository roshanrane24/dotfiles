#!/bin/sh
nvim_home=$HOME/.config/nvim

#_is_install() {
#    
#}

_install_config() {
    for file in *.lua; do
        if [[ -e $nvim_home/$file ]]; then
            rm $nvim_home/$file
        fi
        ln -sf $PWD/$file $nvim_home/$file
    done

    for file in lua/swolf/*.lua; do
        if [[ -e $nvim_home/$file ]]; then
            rm $nvim_home/$file
        fi
        ln -sf $PWD/$file $nvim_home/$file
    done

    for file in after/**/*.lua; do
        if [[ -e $nvim_home/$file ]]; then
            rm $nvim_home/$file
        fi
        mkdir -p $nvim_home/$(dirname $file)
        ln -sf $PWD/$file $nvim_home/$file
    done
}

_install_config
