#!/usr/bin/env sh

printf "Content-Type: text/plain"
printf "\n\n"

printf "METHOD: $REQUEST_METHOD\n"
printf "REQUEST_URI: $REQUEST_URI\n"
printf "PATH_INFO: ${REQUEST_URI%%\?*}"
