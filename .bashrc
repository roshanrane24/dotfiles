
# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# >>> source
source "$HOME/.config/shell-files/env.sh"
source "$HOME/.config/shell-files/alias.sh"

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
    | sed 's/:/\//g'):

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
 # $giturl
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
