#!/bin/bash

echo "Enter playlist folder"
read folder

for f in "$folder"* ; do
    afplay "$f"
done