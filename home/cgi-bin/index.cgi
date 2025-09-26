#!/usr/bin/env sh

printf "Content-Type: text/plain"
printf "\n\n"

PATH_NAME="${REQUEST_URI%%\?*}"

echo $PATH_NAME

case "$PATH_NAME" in
  */) CGI_SCRIPT="./..${PATH_NAME}index.cgi"
      
      echo $CGI_SCRIPT
      ;;
esac
