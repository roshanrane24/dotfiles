# >>> Lines configured by zsh-newuser-install
HISTFILE=~/.cache/zsh-history
HISTSIZE=1000
SAVEHIST=3000
unsetopt beep
bindkey -v
# <<< End of lines configured by zsh-newuser-install
# >>> The following lines were added by compinstall
zstyle :compinstall filename "$HOME/.zshrc"
#autoload -Uz compinit
#compinit
# <<< End of lines added by compinstall
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/anaconda/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/anaconda/etc/profile.d/conda.sh" ]; then
        . "/opt/anaconda/etc/profile.d/conda.sh"
    else
        export PATH="/opt/anaconda/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# >>> Load Source Files >>>
# --- Enviroment Variables
source "$HOME/.config/shell-files/env.sh"
# --- Aliases
source "$HOME/.config/shell-files/alias.sh"
# --- Functions
source "$HOME/.config/shell-files/functions.sh"

# >>> Plugins
ZSH_PLUGINS="$HOME/.config/shell-files/plugins"
#Zinit
if [ -e "$ZSH_PLUGINS/zinit/zinit.zsh"  ]
then
    source "$ZSH_PLUGINS/zinit/zinit.zsh"
fi

autoload -Uz _zinit
(( ${+_comps} )) && _comps[zinit]=_zinit

#AutoComplete
zinit light marlonrichert/zsh-autocomplete

#F-Sy-H
zinit light zdharma/fast-syntax-highlighting

#URL Highlighter
zinit light ascii-soup/zsh-url-highlighter

#Autosuggetion
zinit light zsh-users/zsh-autosuggestions

# AutoEnv
#zinit load wookayin/zsh-autoswitch-virtualenv
zinit load gimbo/venv-lite.zsh

# Spaceship Prompt
#zinit light denysdovhan/spaceship-prompt
#SPACESHIP_VI_MODE_SHOW=false
zinit light starship/starship
eval "$(starship init zsh)"

#AutoNotify
zinit load MichaelAquilina/zsh-auto-notify
export AUTO_NOTIFY_THRESHOLD=300
export AUTO_NOTIFY_TITLE="%command has just finished."
export AUTO_NOTIFY_BODY="in %elapsed seconds.[%exit_code]"
export AUTO_NOTIFY_EXPIRE_TIME=5000
AUTO_NOTIFY_IGNORE+=("docker", "man", "sleep", "info", "python")

# ZVim
#zinit ice depth=1
#zinit light jeffreytse/zsh-vi-mode

#bd
zinit ice atclone'./init.sh' nocompile'!' wait'!0' 
zinit light b4b4r07/enhancd 

# <<< Plugins

# >>> Prompt Engine
autoload -Uz promptinit
promptinit
# <<< eol prompt engine
#>>> Ex
# <<< Ex
