#!/usr/bin/env sh

PATH_NAME="${REQUEST_URI%%\?*}"

case "$PATH_NAME" in
  */) CGI_SCRIPT="./..${PATH_NAME}index.cgi"
      if [ -e "$CGI_SCRIPT" ]; then
        "$CGI_SCRIPT"
      else
        printf "Content-Type: text/plain\n\n404"
      fi
      printf "CGI_SCRIPT STATUS: COMPLETED\n" >&2
      ;;
esac
