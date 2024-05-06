#!/bin/sh -e

# hacksaw + shotgun utility script for screenshot

selection=$(hacksaw -f "-i %i -g %g")

if [ $# -gt 0 ]; then
  if [ $1 = '-s' ]; then
    case $# in
      2)shotgun $selection "$2";;
      1)shotgun $selection "SS$(date +%d-%m-%YT%R:%S).png";;
    esac
  fi
else
  shotgun $selection - | xclip -t 'image/png' -selection clipboard
fi
