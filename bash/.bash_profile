#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

export PATH=$PATH:~/.cargo/bin

if [[ -z $DISPLAY ]] && [[ $(tty) = '/dev/tty1' ]]; then
	pgrep qtile || startx
fi

