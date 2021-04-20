# ~/.profile: executed by Bourne-compatible login shells.

level1() {
    echo 1 > /etc/gamelevel
    /usr/bin/game.py help
}

level2() {
    echo 2 > /etc/gamelevel
    /usr/bin/game.py help
}

if [ "$BASH" ]; then
  if [ -f ~/.bashrc ]; then
    . ~/.bashrc
  fi
fi

CLEAR="\[\033[0m\]"
BLACK="\[\033[0;30m\]"
RED="\[\033[0;31m\]"
GREEN="\[\033[0;32m\]"
YELLOW="\[\033[0;33m\]"
BLUE="\[\033[0;34m\]"
PURPLE="\[\033[0;35m\]"
CYAN="\[\033[0;36m\]"
WHITE="\[\033[0;37m\]"

export PS1=\
"${BLUE}[${CLEAR}"\
"${CYAN}\u${CLEAR}"\
"${CYAN}@${CLEAR}"\
"${CYAN}jedi-trainer${CLEAR} "\
"${GREEN}\w${CLEAR}"\
"${BLUE}]${CLEAR}"\
" ${BLUE}[${CLEAR}"\
"${PURPLE}\$(/usr/bin/game.py check)${CLEAR}"\
"${BLUE}]${CLEAR}"\
"\n\$ "

export QUOTING_STYLE=literal
#bind 'set disable-completion on'

/usr/bin/game.py init
level1
