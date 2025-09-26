#!/usr/bin/env sh

printf "Content-Type: text/plain"
printf "\n\n"

PATH_NAME="${REQUEST_URI%%\?*}"

echo $PATH_NAME

case "$PATH_NAME" in
  */) CGI_SCRIPT="./..${PATH_NAME}index.cgi"
      if [ -e "$CGI_SCRIPT" ]; then
        sh "$CGI_SCRIPT"
      else
        printf "404"
      fi
      ;;
esac
