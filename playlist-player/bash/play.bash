#!/bin/bash

# The bash script version for this project has been abandoned for now due to problems with afplay

echo "Enter playlist folder"
read folder

# for f in "$folder"* ; do
#     echo "$f"
# done

for f in "{$folder}*" ; do
    echo "$f"
done