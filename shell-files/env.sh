# >>> Path
export PATH=$PATH:$HOME/.local/bin:/usr/local/go/bin:$HOME/.cargo/bin

# >>> ls
export LS_COLORS="$(vivid generate jellybeans)"

# >>> Locale
export LC_ALL="en_US.UTF-8"

# >>> prompt
export PS1='\e[32m\w\n\e[031m>\e[m '

# >>> qt-gtk theme
export QT_QPA_PLATFORMTHEME=qt5ct

# Ignore These Commands in history
export HISTIGNORE=${HISTIGNORE:-"shutdown*:halt*:poweroff*:hibernate*:history*"}

# GOLANG
# export GOROOT=/usr/lib/go
# export GO111MODULE=on
# export GOPATH="$HOME/.local/lib/golib"
# export GOPATH="$HOME/Build/gocode"
# export PATH=$PATH:$GOPATH/bin:$GOROOT/bin

# EDITOR
export EDITOR=vim

# DOTFILES
export DOTFILES_PATH='~/.config/dotfiles'

# JAVA
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk

# TEMP
export TMUX_TMPDIR='/tmp'
