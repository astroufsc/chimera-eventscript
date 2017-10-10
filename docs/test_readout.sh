#!/bin/bash
if [ "$2" = "zero" ] || [ "$2" = "object" ] ; then
    echo $2
fi

fname_prefix=$(echo $1 | cut -f1 -d-)

echo $fname_prefix

if [ "$fname_prefix" == "align" ] || [ "$fname_prefix" == "skyflat" ]; then
    echo "Skipping image processing of $1."
    exit 0
fi

images_path="$HOME/images/"
last_night=$(gdate -d "12 hours ago" "+%Y%m%d")
ls $images_path/$last_night/$1