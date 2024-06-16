#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'

alias yay='paru'

RED="\e[0;31m"
GREEN="\e[0;32m"
YELLOW="\e[0;33m"
BLUE="\e[0;34m"
ENDCOLOR="\e[0m"

extend_prompt()
{
	# GIT STUFF

	branch=''

	if [ -d .git ]; then
		branch_name=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
		if [ $? -ne 0 ]; then
			branch="-(${YELLOW}no-branches-yet${ENDCOLOR})"
		else
			if [ $branch_name = 'HEAD' ]; then # this is detached head state
				hash=$(git rev-parse --short HEAD 2>/dev/null)
				branch="-(${RED}detached-at-${hash}${ENDCOLOR})"
			else
				branch="-(${GREEN}$branch_name${ENDCOLOR})"
			fi
		fi
	fi

	# PYTHON ENV STUFF

	venv_info=''

	if [ ! -z $VIRTUAL_ENV ]; then
		venv_info="-(${BLUE}${VIRTUAL_ENV##*/}${ENDCOLOR})"
	fi

	echo -e "${branch}${venv_info}"
}

PS1='╭──[\u@\h]-[\W]$(extend_prompt)\n╰────\$ '

export VIRTUAL_ENV_DISABLE_PROMPT=1

