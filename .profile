# ~/.profile: executed by Bourne-compatible login shells.

start() {
    /usr/bin/game.py start
    unset -f start
}

status() {
    /usr/bin/game.py status
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
"${PURPLE}\$(/usr/bin/game.py check)${CLEAR}"\
"\n\$ "

export QUOTING_STYLE=escape
bind 'set disable-completion on'

start
