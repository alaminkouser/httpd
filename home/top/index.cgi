#!/usr/bin/env sh

printf "Content-Type: text/stream\n\n"

COLUMNS=1024 top -b -n 1
