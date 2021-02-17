#/bin/env bash
powermenu () {
action=$(printf "> Shutdown\n> Reboot\n> Lock\n> Logout\n> Sleep\n> Hibernate" | rofi -location 3 -yoffset 22 -width 100 -dmenu -theme lime-amber-menu -no-fullscreen)
action=$(echo "$action" | cut -d' ' -f2)

case "$action" in
	Shutdown)
		confirm=$(printf "Shutdown\nCancel" | rofi -location 3 -yoffset 22 -height 5% -dmenu -theme lime-amber-menu -no-fullscreen)
		case "$confirm" in
			Shutdown)
				systemctl poweroff -i
			;;
			*)
				powermenu
			;;
		esac
	;;
	Reboot)
		confirm=$(printf "Reboot\nCancel" | rofi -location 3 -yoffset 22 -height 100 -dmenu -theme lime-amber-menu -no-fullscreen)
		case "$confirm" in
			Reboot)
				systemctl reboot
			;;
			*)
				powermenu
			;;
		esac
	;;
	Lock)
	~/.config/scripts/i3lockshot.sh
	;;
	Logout)
		confirm=$(printf "Logout\nCancel" | rofi -location 3 -yoffset 22 -dmenu -theme lime-amber-menu -height 15 -no-fullscreen)
		case "$confirm" in
			Shutdown)
				i3-msg exit
			;;
			*)
				powermenu
			;;
		esac
	;;
	Sleep)
	systemctl suspend-then-hibernate
	;;
	Hibernate)
	systemctl hibernate
	;;
esac
}
powermenu
