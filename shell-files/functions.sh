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
