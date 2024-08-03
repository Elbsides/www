#!/bin/bash
INKSCAPE="/Applications/Inkscape.app/Contents/MacOS/inkscape"
filename=$1
sizes="200 268 335 376 418 600 627 630 675 720 800 900 1080"
if [[ -f $filename ]]; then
    for size in $sizes; do
	$INKSCAPE --export-height=$size --export-filename="${filename%.*}.$size.png" "$filename"
	$INKSCAPE --export-height=$size --export-background=white --export-filename="${filename%.*}.$size.white.png" "$filename"
	$INKSCAPE --export-height=$size --export-background=black --export-filename="${filename%.*}.$size.black.png" "$filename"
    done
fi
