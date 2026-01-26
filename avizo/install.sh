#!/usr/bin/env sh

CONFIG_DIR="$XDG_CONFIG_HOME/avizo" 

[ -L "$CONFIG_DIR/config.ini" ] || rm "$CONFIG_DIR/config.ini"
mkdir -p $CONFIG_DIR
ln -sf "$DOTFILES_PATH/avizo/config.ini" "$CONFIG_DIR/config.ini"
