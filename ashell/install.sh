ASHELL_CONFIG_PATH=${HOME}/.config/ashell

[[ -d $ASHELL_CONFIG_PATH ]] || mkdir -p $ASHELL_CONFIG_PATH
[[ -L ${ASHELL_CONFIG_PATH}/config.toml ]] && rm ${ASHELL_CONFIG_PATH}/config.toml

ln -sf $PWD/config.toml $ASHELL_CONFIG_PATH/config.toml
