#!/bin/bash

echo "Enter playlist folder"
#read folder

for f in ~/Desktop/Other\ Music/* ; do
    afplay "$f"
done