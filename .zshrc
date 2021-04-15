# >>> Lines configured by zsh-newuser-install
HISTFILE=~/.cache/zsh-history
HISTSIZE=1000
SAVEHIST=3000
unsetopt beep
bindkey -v
# <<< End of lines configured by zsh-newuser-install
# >>> The following lines were added by compinstall
zstyle :compinstall filename "$HOME/.zshrc"
autoload -Uz compinit
compinit
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
source "$HOME/.config/shell-files/alias.sh"
source "$HOME/.config/shell-files/functions.sh"
source '/usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh'
# >>> Prompt Engine
autoload -Uz promptinit
promptinit
prompt spaceship
# <<< eol prompt engine
