#!/bin/bash

# refer from: https://www.cnblogs.com/zqb-all/p/9786836.html
com() {
	ports_USB=$(ls /dev/ttyUSB*)
	ports_ACM=$(ls /dev/ttyACM*)  #arduino
	ports="$ports_USB $ports_ACM"
        datename=$(date +%Y%m%d-%H%M%S)
        echo "$datename"
	select port in $ports;do
		if [ "$port" ]; then
                        echo "You select the choice '$port'"
                        minicom -D "$port" -C $gws/log/"$datename".log "$@"
                        break
		else
                        echo "Invaild selection"
                fi
	done
}