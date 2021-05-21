get-temps()
{
    if [ $(sensors  &> /dev/null; echo $?) -ne 0  ]
    then
        print '\e[5m\e[91msensors\e[0m command not found \nplease install \e[31mlm-sensor\e[0m'
    else
        print '\e[1m\e[92mCPU TEMPS:\e[0m'
        print "$(sensors | grep '..\.*C*(')"
    fi
    if [ $(hddtemp  -v &> /dev/null; echo $?) -ne 0  ]
    then
        print '\n\e[5m\e[91mhddtemp\e[0m command not found. please install \e[31mhddtemp\e[0m.'
    else
        print '\n\e[1m\e[92mHDD TEMPS:\e[0m'
        print "$(hddtemp /dev/sda | cut -d ' ' -f 1,3)"
    fi
}


cppc(){
    file_base=`echo $1 |cut -d. -f1`;
    compiled=""

    if [ -n "$3" ]
    then
        output="$3/$file_base";
    else
        output="$PWD/bin/$file_base";
    fi

    echo "Output file $output"
    clang++ $1 -o $output && compiled=1;

    if [ $2 -eq 1 ] && [ "$compiled" -eq 1 ]
    then
        echo "executing $output"
        dash -c "$output";
    fi
}


pvenv(){
    working_directory=$PWD
    for directory in `ls -d $working_directory/*/`
    do
        echo `test -e $directory/`
        if [ -e "$directory/bin/activate" ]
        then
            `source "directory/bin/activate"`
            echo "$directory activated."
        fi
    done
    echo 'No Python VENV available in current location.'
}


function _set_cursor() {
    if [[ $TMUX = '' ]]
    then
        echo -ne $1
    else
        echo -ne "\ePtmux;\e\e$1\e\\"
    fi
}

# Remove mode switching delay.
KEYTIMEOUT=5

function _set_block_cursor() { _set_cursor '\e[2 q' }
function _set_beam_cursor() { _set_cursor '\e[0 q' }

function zle-keymap-select {
if [[ ${KEYMAP} == vicmd ]] || [[ $1 = 'block' ]]; then
    _set_block_cursor
else
    _set_beam_cursor
fi
}


zle -N zle-keymap-select

# ensure beam cursor when starting new terminal
precmd_functions+=(_set_beam_cursor) #

# ensure insert mode and beam cursor when exiting vim
zle-line-init() { zle -K viins; _set_beam_cursor }
zle-line-finish() { _set_block_cursor }
zle -N zle-line-finish


