#!/usr/bin/env bash

shopt -s nullglob

while inotifywait -qqe modify -e move_self *.tex *.bib; do
    echo -n "Compiling...  "
    >stdout \
    latexmk \
        -f \
        -pdf \
        -interaction=nonstopmode \
        -outdir=target/ \
        main.tex
    echo Done. "($?)"
done
