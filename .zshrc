# Lines configured by zsh-newuser-install
HISTFILE=~/.cache/zsh-history
HISTSIZE=1000
SAVEHIST=3000
unsetopt beep
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/greenalien/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
# Prompt Engine
autoload -Uz promptinit
promptinit
prompt spaceship

alias config='/usr/bin/git --git-dir=/home/greenalien/build/dotfiles --work-tree=/home/greenalien'
alias ls='ls --color=auto'
alias lsa='ls -la'