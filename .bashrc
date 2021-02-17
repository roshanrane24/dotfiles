
# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Aliases
alias __='sudo'
alias ls='ls --color=auto'
alias lsa='ls -la'
alias cf='cd'
alias mkdir='mkdir -p'
alias grep='grep --color=auto'

##
PS1='\e[32m\w\n\e[031m>\e[m '

## ENV
QT_QPA_PLATFORMTHEME=qt5ct


#############COLORS####
#RESET
export COLOR_NO_COLOR='\e[m'

#Regular Colors
export COLOR_BLACK='\e[0;30m'
export COLOR_GRAY='\e[1;30m'
export COLOR_LIGHT_GRAY='\e[0;37m'
export COLOR_CYAN='\e[0;36m'
export COLOR_LIGHT_CYAN='\e[1;36m'
export COLOR_BLUE='\e[0;34m'
export COLOR_LIGHT_BLUE='\e[1;34m'
export COLOR_RED='\e[0;31m'
export COLOR_LIGHT_RED='\e[1;31m'
export COLOR_GREEN='\e[0;32m'
export COLOR_LIGHT_GREEN='\e[1;32m'
export COLOR_PURPLE='\e[0;35m'
export COLOR_LIGHT_PURPLE='\e[1;35m'
export COLOR_BROWN='\e[0;33m'
export COLOR_YELLOW='\e[1;33m'
export COLOR_WHITE='\e[0;37m'

# Bold
export COLOR_B_BLACK='\e[1;30m'       # Black
export COLOR_B_RED='\e[1;31m'         # Red
export COLOR_B_GREEN='\e[1;32m'       # Green
export COLOR_B_YELLOW='\e[1;33m'      # Yellow
export COLOR_B_BLUE='\e[1;34m'        # Blue
export COLOR_B_PURPLE='\e[1;35m'      # Purple
export COLOR_B_CYAN='\e[1;36m'        # Cyan
export COLOR_B_WHITE='\e[1;37m'       # White

# Underline
export COLOR_U_BLACK='\e[4;30m'       # Black
export COLOR_U_RED='\e[4;31m'         # Red
export COLOR_U_GREEN='\e[4;32m'       # Green
export COLOR_U_YELLOW='\e[4;33m'      # Yellow
export COLOR_U_BLUE='\e[4;34m'        # Blue
export COLOR_U_PURPLE='\e[4;35m'      # Purple
export COLOR_U_CYAN='\e[4;36m'        # Cyan
export COLOR_U_WHITE='\e[4;37m'       # White

# Background
export COLOR_BG_BLACK='\e[40m'       # Black
export COLOR_BG_RED='\e[41m'         # Red
export COLOR_BG_GREEN='\e[42m'       # Green
export COLOR_BG_YELLOW='\e[43m'      # Yellow
export COLOR_BG_BLUE='\e[44m'        # Blue
export COLOR_BG_PURPLE='\e[45m'      # Purple
export COLOR_BG_CYAN='\e[46m'        # Cyan
export COLOR_BG_WHITE='\e[47m'       # White

# High Intensity
export COLOR_HI_BLACK='\e[0;90m'       # Black
export COLOR_HI_RED='\e[0;91m'         # Red
export COLOR_HI_GREEN='\e[0;92m'       # Green
export COLOR_HI_YELLOW='\e[0;93m'      # Yellow
export COLOR_HI_BLUE='\e[0;94m'        # Blue
export COLOR_HI_PURPLE='\e[0;95m'      # Purple
export COLOR_HI_CYAN='\e[0;96m'        # Cyan
export COLOR_HI_WHITE='\e[0;97m'       # White

# Bold High Intensity
export COLOR_BHI_BLACK='\e[1;90m'      # Black
export COLOR_BHI_RED='\e[1;91m'        # Red
export COLOR_BHI_GREEN='\e[1;92m'      # Green
export COLOR_BHI_YELLOW='\e[1;93m'     # Yellow
export COLOR_BHI_BLUE='\e[1;94m'       # Blue
export COLOR_BHI_PURPLE='\e[1;95m'     # Purple
export COLOR_BHI_CYAN='\e[1;96m'       # Cyan
export COLOR_BHI_WHITE='\e[1;97m'      # White

# High Intensity backgrounds
export COLOR_BG_HI_BLACK='\e[0;100m'   # Black
export COLOR_BG_HI_RED='\e[0;101m'     # Red
export COLOR_BG_HI_GREEN='\e[0;102m'   # Green
export COLOR_BG_HI_YELLOW='\e[0;103m'  # Yellow
export COLOR_BG_HI_BLUE='\e[0;104m'    # Blue
export COLOR_BG_HI_PURPLE='\e[10;95m'  # Purple
export COLOR_BG_HI_CYAN='\e[0;106m'    # Cyan
export COLOR_BG_HI_WHITE='\e[0;107m'   # White


if [ "$TERM" = "linux" ]; then
	echo -en "\e]P0000000" #black
	echo -en "\e]P82B2B2B" #darkgrey
	echo -en "\e]P1D75F5F" #darkred
	echo -en "\e]P9E33636" #red
	echo -en "\e]P287AF5F" #darkgreen
	echo -en "\e]PA98E34D" #green
	echo -en "\e]P3D7AF87" #brown
	echo -en "\e]PBFFD75F" #yellow
	echo -en "\e]P48787AF" #darkblue
	echo -en "\e]PC7373C9" #blue
	echo -en "\e]P5BD53A5" #darkmagenta
	echo -en "\e]PDD633B2" #magenta
	echo -en "\e]P65FAFAF" #darkcyan
	echo -en "\e]PE44C9C9" #cyan
	echo -en "\e]P7E5E5E5" #lightgrey
	echo -en "\e]PFFFFFFF" #white
fi

##EXPORTS
export HISTIGNORE=${HISTIGNORE:-"shutdown*:halt*:poweroff*:hibernate*:rm -rf*"}



## Function
err()
{
	echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $@" >&2
}




repo()
{
  local giturl=$(git config --get remote.origin.url \
    | sed 's/git@/\/\//g' \
    | sed 's/.git$//' \
    | sed 's/https://g' \
    | sed 's/:/\//g')

  if [[ $giturl == "" ]]; then
    echo "Not a git repository or no remote.origin.url is set."
  else
    local gitbranch=$(git rev-parse --abbrev-ref HEAD)
    local giturl="https:${giturl}"

    if [[ $gitbranch != "master" ]]; then
      if echo "${giturl}" | grep -i "bitbucket" > /dev/null ; then
        local giturl="${giturl}/branch/${gitbranch}"
      else
        local giturl="${giturl}/tree/${gitbranch}"
      fi
    fi

    echo $giturl
    o $giturl
  fi
}

__git_prompt()
{
  local s=''
  local branchName=''

  # Check if the current directory is in a Git repository.
  if [[ $(git rev-parse --is-inside-work-tree &>/dev/null; echo "${?}") == "0" ]]; then

    # The following is to too slow on cygwin/mingw. especially for large repositoryies.
    if [[ $SYSTEM_TYPE != "CYGWIN" && $SYSTEM_TYPE != "MINGW" ]]; then
      # Check if the current directory is in .git before running git checks.
      if [[ "$(git rev-parse --is-inside-git-dir 2>/dev/null)" == "false" ]]; then

        # Create a copy of the index to avoid conflicts with parallel git commands, e.g. git rebase.
        __GIT_INDEX_FILE_ORIG="$GIT_INDEX_FILE"
        __GIT_DIR="$(git rev-parse --git-dir)"
        if [[ -z "$GIT_INDEX_FILE" ]]; then
          __GIT_INDEX_FILE="$__GIT_DIR/index"
        else
          __GIT_INDEX_FILE="$GIT_INDEX_FILE"
        fi
        __GIT_INDEX_PROMPT="/tmp/git-index-prompt$$"
        cp "$__GIT_INDEX_FILE" $__GIT_INDEX_PROMPT 2>/dev/null
        export GIT_INDEX_FILE="$__GIT_INDEX_PROMPT"

        # Ensure the copied index is up to date.
        git update-index --really-refresh -q &> /dev/null;
        # Check if we are ahead or behind our tracking branch (https://gist.github.com/HowlingMind/996093).
        local git_status="$(LANG=C LANGUAGE=C git status 2>/dev/null)";

        local remote_pattern="Your branch is (ahead|behind).*by ([[:digit:]]*) commit"

        if [ -n "$BASH_VERSION" ]; then

          if [[ "$git_status" =~ $remote_pattern ]]; then
            if [[ "${BASH_REMATCH[1]}" == "ahead" ]]; then
              s+="${ICON_FOR_UP}${BASH_REMATCH[2]} "
            else
              s+="${ICON_FOR_DOWN}${BASH_REMATCH[2]} "
            fi
          fi

        elif [ -n "$ZSH_VERSION" ]; then

          if [[ "$git_status" =~ $remote_pattern ]]; then
            if [[ "${match[1]}" == "ahead" ]]; then
              s+="${ICON_FOR_UP}${match[2]} "
            else
              s+="${ICON_FOR_DOWN}${match[2]} "
            fi
          fi

        fi

        # Check for uncommitted changes in the index.
        if ! $(git diff --quiet --no-ext-diff --ignore-submodules --cached); then
          s+="+"
        fi

        # Check for unstaged changes.
        if ! $(git diff-files --quiet --ignore-submodules -- 2>/dev/null); then
          s+="!"
        fi

        # Check for untracked files.
        if [ -n "$(git ls-files --others --exclude-standard 2>/dev/null)" ]; then
          s+="?"
        fi

        # Check for stashed files.
        if $(git rev-parse --verify refs/stash &>/dev/null); then
          s+="$"
        fi

        # The number of commits ahead/behind ends with a trailing space. If no other indicator was added, it will be lingering at the end of `s`.
        s=$(echo "${s}" | sed 's/ *$//')

        export GIT_INDEX_FILE="$__GIT_INDEX_FILE_ORIG"
        # "rm" the temporary index.
        rm "$__GIT_INDEX_PROMPT" 2>/dev/null
      fi
    else
      s="-";
      if [[ $(git config --get core.autocrlf) != "true" ]]; then
        s+=" CRLF";
      fi
      if [[ $(git config --get core.filemode) != "false" ]]; then
        s+=" FILEMODE";
      fi
    fi

    # Get the short symbolic ref.
    #
    # If HEAD isn’t a symbolic ref, get the short SHA for the latest commit
    # Otherwise, just give up.
    branchName="$({ LANG=C LANGUAGE=C git symbolic-ref --quiet HEAD 2>/dev/null || \
      git rev-parse --short HEAD 2>/dev/null || \
      echo '(unknown)'; } | sed 's/^refs\/heads\///')";

    [[ -n "${s}" ]] && s=" [${s}]"

    echo " (${branchName})${s}"
  else
    return
  fi
}
