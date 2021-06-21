#!/bin/env bash

SYSTEM=$()
# Show Main Menu
function main_menu () {
    echo "Select Config You Want to Install:"
    echo "0: Exit"
    echo "1: Alacritty"
    echo "2: Bash"
    echo "3: BSPWM"
    echo "4: Deadd"
    echo "5: Dunst"
    echo "6: i3"
    echo "7: MPV"
    echo "8: Picom"
    echo "9: QTile"
    echo "10: Rofi"
    echo "11: Tmux"
    echo "12: Vim"
    echo "13: ZSH"
    echo "A: All"

    printf "SELECT e.g.(1 5 10) :"
    read -a OPTIONS

    if [[ "${OPTIONS[@]}" =~ "A" ]]; then
        install "A"
    else
        for opt in ${OPTIONS[@]}; do
            install $opt
        done
    fi
}

# Start Selected install
function install() {
    case $1 in
        0)
           exit
            ;;
        1)
           echo
           install_alacritty
           echo
           main_menu
            ;;
        2)
           echo
           install_bash
           echo
           main_menu
            ;;
        3)
           echo
           install_bspwm
           echo
           main_menu
            ;;
        4)
           echo
           install_deadd
           echo
           main_menu
            ;;
        5)
           echo
           install_dunst
           echo
           main_menu
            ;;
        6)
           echo
           install_i3
           echo
           main_menu
            ;;
        7)
           echo
           install_mpv
           echo
           main_menu
            ;;
        8)
           echo
           install_picom
           echo
           main_menu
            ;;
        9)
           echo
           install_qtile
           echo
           main_menu
            ;;
        10)
           echo
           install_rofi
           echo
           main_menu
            ;;
        11)
           echo
           install_tmux
           echo
           main_menu
            ;;
        12)
           echo
           install_vim
           echo
           main_menu
            ;;
        13)
           echo
           install_zsh
           echo
           main_menu
            ;;
        A)
           echo
           install_alacritty
           echo
           install_bash
           echo
           install_bspwm
           echo
           install_deadd
           echo
           install_dunst
           echo
           install_i3
           echo
           install_mpv
           echo
           install_picom
           echo
           install_qtile
           echo
           install_rofi
           echo
           install_tmux
           echo
           install_vim
           echo
           install_zsh
           echo
           main_menu
            ;;
        *)
           echo "$1 is not a valid option."
           main_menu
            ;;
    esac
}


## Intalls
# Install Alacritty
function install_alacritty() {
    echo "Setting Up Alacritty"
    if [[ ! -e "/bin/alacritty" ]]; then
        echo "Alacrity is not installed."
        echo "Installing Alacriyty"
        package_install alacritty
    fi

    alacritty_dir="$HOME/.config/alacritty"
    mkdir -p $alacritty_dir

    link_file "$PWD/alacritty/*" "$alacritty_dir"

    echo "Done Setting Up Alacritty"
}

function install_bash() {
    echo "Setting Up bash"
    link_file "$PWD/.bashrc" "$HOME"

    shell_dir="$HOME/.config/shell-files"
    link_file "$PWD/shell-files/*" $shell_dir

    echo "Bashrc Config Setup Complete"
}

function install_bspwm() {
    echo "Setting Up BSPWM"
    if [[ ! -e "/bin/bspwm" ]]; then
        echo "BSPWM Not Installed"
        echo "Installing BSPWM"
        package_install bspwm
    fi

    bspwm_dir="$HOME/.config/bspwm"
    sxhkd_dir="$HOME/.config/sxhkd"
    mkdir -p $bspwm_dir
    mkdir -p $sxhkd_dir

    link_file "$PWD/bspwm/*" $bspwm_dir
    link_file "$PWD/sxhkd/*" $sxhkd_dir

    echo "Done Setiing Up BSPWM"
}

function install_deadd() {
    echo "Setting Up Deadd"
    if [[ ! -e "/bin/deadd-notification-center" ]]; then
        echo "deadd-notification-center is Not Installed"
        echo "Install deadd-notification-center."
        return
    fi

    deadd_dir="$HOME/.config/deadd"
    if [[ ! -d $deadd_dir ]]; then
        mkdir -p $deadd_dir
    fi

    link_file "$PWD/deadd/*" $deadd_dir

    echo "Done Setiing Up Deadd"
}

function install_dunst() {
    echo "Setting Up Dunst"
    if [[ ! -e "/bin/dunst" ]]; then
        echo "Dunst Not installed"
        echo "Installing Dunst"
        package_install dunst
    fi

    dunst_dir="$HOME/.config/dunst"
    dunst_extra_dir="$HOME/.config/dunst/scripts"
    mkdir -p $dunst_dir
    mkdir -p $dunst_extra_dir

    link_file "$PWD/dunst/dunstrc" $dunst_dir
    link_file "$PWD/dunst/scripts" $dunst_extra_dir

    echo "Done Setiing Up Dunst"
}
function install_i3() {
    echo "Setting Up i3WM"
    if [[ ! -e "/bin/i3" ]]; then
        echo "i3 Not installed"
        echo "Installing i3"

        if [[ -e "/bin/pacman" ]]; then
            sudo pacman -Sy i3-gaps
        else
            cwd=$PWD
            cd /tmp
            git clone 'https://github.com/Airblader/i3.git'
            cd i3
            autoreconf --force --install
            mkdir build
            cd build
            ../configure --prefix=/usr --sysconfdir=/etc
            make
            sudo make install
            cd $cwd
        fi
    fi

    if [[ ! -e "/bin/polybar" ]]; then
        echo "Polybar Not installed"
        echo "Installing Polybar"

        if [[ -e "/bin/apt" ]]; then
            package_install polybar
        else
            cwd=$PWD
            cd /tmp
            git clone --recursive https://github.com/polybar/polybar
            cd polybar
            mkdir build
            cd build
            cmake ..
            make -j$(nproc)
            # Optional. This will install the polybar executable in /usr/local/bin
            sudo make install
        fi
    fi

    i3_dir="$HOME/.config/i3"
    polybar_dir="$HOME/.config/polybar"
    i3_extra_dir="$HOME/.config/i3/scripts"
    polybar_extra_dir="$HOME/.config/polybar/scripts"
    mkdir -p $i3_extra_dir
    mkdir -p $polybar_dir

    link_file "$PWD/i3/*" $i3_dir
    link_file "$PWD/i3/scripts/*" $i3_extra_dir
    link_file "$PWD/polybar/*" $polybar_dir
    link_file "$PWD/polybar/scripts/*" $polybar_extra_dir

    echo "Done Setting Up i3WM"
}

function install_mpv() {
    echo "Setting Up MPV"
    if [[ ! -e "/bin/mpv" ]]; then
        echo "MPV not installed"
        echo "Installing MPV"
        package_install mpv
    fi

    mpv_dir="$HOME/.config/mpv"
    link_file "$PWD/mpv/*" $mpv_dir

    echo "Done Setting Up MPV"
}

function install_picom() {
    echo "Setting Up picom"
    if [[ ! -e "/bin/picom" ]]; then
        echo "Picom is not installed"
        echo "Installing Picom"
        package_install picom
    fi

    picom_dir="$HOME/.config/picom"
    mkdir -p $picom_dir

    link_file "$PWD/picom/*" $picom_dir
}

function install_qtile() {
    echo "Setting Up QTile"
    if [[ ! -e "/bin/python3" ]];then
        echo "Pyhton3 Not installed"
        echo "Installing Python"
        package_install python
        package_install python-pip
    fi

    if [[ ! -e "/bin/qtile" ]];then
        echo "QTile Not installed"
        echo "Installing QTile"
        package_install qtile
        echo "Installing psutil"
        pip install psutil
        echo "Installing lm_sensors"
        package_install lm_sensors
    fi

    # Install FlatRemix
    echo "Flat Remix"
    cwd=$PWD
    cd /tmp
    git clone 'https://github.com/daniruiz/flat-remix-gtk.git'
    cd flat-remix-gtk
    make
    sudo make install
    cd ..
    git clone 'https://github.com/daniruiz/flat-remix.git'
    cd flat-remix
    make
    sudo make install
    cd ..

    # Dynamic Colors
    # Installing OpenCv
    echo "Installing OpenCv"
    pip install opencv-python
    pip install json
    echo "Installing DominantColors"
    git clone 'https://github.com/roshanrane24/DominantColors.git'
    cd DominantColors
    pip install setuptools wheel sklearn numpy
    python setup.py bdist_wheel
    pip install dist/*.whl

    qtile_dir="$HOME/.config/qtile"
    qtile_fun_dir="$qtile_dir/myFunctions"
    mkdir -p $qtile_dir
    mkdir -p $qtile_fun_dir

    link_file "$PWD/qtile/*.py" $qtile_dir
    link_file "$PWD/qtile/myFunctions/*.py" $qtile_fun_dir

    echo "Finish Setting Up QTile"
}

function install_rofi() {
    echo "Setting Up Rofi"
    if [[ ! -e "/bin/rofi" ]]; then
        echo "Rofi Not Installed"
        echo "Installing Rofi"
        package_install rofi
    fi

    rofi_dir="$HOME/.config/rofi"
    link_file "$PWD/rofi/*" $rofi_dir

    echo "Done Setting Up Rofi"
}

function install_tmux() {
    echo "Setting Up TMUX"
    if [[ ! -e "/bin/tmux" ]]; then
        echo "TMUX not installed"
        echo "Installing Tmux"
        package_install tmux
    fi

    tmux_pm="$HOME/.tmux/plugins"
    mkdir -p $tmux_pm
    git clone 'https://github.com/tmux-plugins/tpm' $HOME/.tmux/plugins/tpm

    link_file ".tmux.conf" $HOME

    echo "Done Setting UP Tmux"
}

function install_vim() {
    echo "Setting Up Vim"
    printf "[Vim/NeoVim]:"
    vn=`read`
    case $vn in
        vim|Vim|VIM|v)
            vimPath="$HOME/.vim"
            # Plug
            curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
                https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
            link_file "$PWD/nvim/init.vim" "$vimPath/vimrc"
            ;;
        neo|neovim|Neovim|NeoVim|nv|n|NEOVIM|nvim)
            vimPath="$HOME/.config/nvim"
            # Plug
            sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
                https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

            link_file "$PWD/nvim/init.vim" $vimPath
            ;;
        *)
            echo "Not a Valid Choice"
            install_vim
    esac
}
function install_zsh() {
    if [[ ! -e "/bin/zsh" ]]; then
        echo "ZSH is not installed"
        echo "Installing ZSH"
        package_install zsh
    fi

    link_file "$PWD/.zshrc" "$HOME"

    shell_dir="$HOME/.config/shell-files"
    link_file "$PWD/shell-files/*" $shell_dir

    zinit_dir="$HOME/.zinit"
    mkdir -p $zinit_dir
    git clone https://github.com/zdharma/zinit.git

    echo "Zshrc Config Setup Complete"
}

# Tools
function package_install() {
    if [[ -n $(pacman -V 2> /dev/null) ]]; then
        $(sudo pacman -Sy --noconfirm $1)
    elif [[ -n $(apt -v 2> /dev/null) ]]; then
        $(sudo apt install $1 -y)
    else
        echo "No Known Package Manager Found."
        exit
    fi
}

function link_file(){
    if [[ -e  $2 ]]; then
        echo "$2 File Already Exist"
        printf "Do you want to replace file with new link? [y/N]"
        confirm=`read`

        case $confirm in
            Y|y|yes|Yes|YES)
                rm -f $2
                ln $1 $2
                ;;
            N|n|no|No|NO)
                echo "$2 file unchanged"
                return
                ;;
            *)
                echo "$2 file unchanged"
                return
                ;;
        esac
    else
        ln $1 $2
    fi
}

main_menu
