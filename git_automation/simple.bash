#!/bin/bash

convey () {
    say -v $3 $1
    echo $2
}  

new_commit () {
    echo $seperate
    convey "Git status shown below" "GIT STATUS..." "Daniel"
    sleep 1
    git status
    sleep 1
    echo $seperate
    sleep 2
    convey "Enter the file path from current D I R... Also, X to escape the loop -r 10" "File: " "Fiona"
    read file
    while [ "$file" != "x" ]
        do
        file_path=$(/bin/pwd)
        if [ "$file" == "all" ]
            then
            git add .
        else
            git add "$file_path/$file"
            convey "Enter another file to add... Or leave with the lowercase letter x -r 8" "File: " "Daniel"
            read file
        fi
    done
    convey "Enter commit message -r 10" "Commit message: " "Alice"
    read commit_message
    echo "GIT COMMIT..."
    git commit -m "$commit_message"
    sleep 3
    convey "Git status displayed below" $seperate "Moira"
    sleep 1
    echo "GIT STATUS..."
    git status
    echo $seperate
    sleep 2
    convey "Lowercase Y to create another commit... Lowercase N to proceed to pushing changes -r 8" "Create another commit? [y/n]" "Daniel"
    read answer
    if [ "$answer" == "y" ]
        then
        new_commit
    else
        git_push
        say -v Alex -r 230 "Program shutting down, thank you and see you next time"
        afplay /Users/Peregrine/Downloads/winterspell_30s.m4a
    fi

    }

git_push () {
    convey "Push changes... Y or N?" "Push changes? [y/n]" "Fiona"
        read push
        echo $seperate
        if [ "$push" == "y" ]
            then
            convey "Pushing changes" "PUSH CHANGES..." "Karen"
            git push
            sleep 4
            echo $seperate
            git status
        else
            convey "Git push cancelled -r 12" "Git push cancelled" "Karen"
        fi

}
seperate="------------------------------------------------------------------------"

echo """
  ____ ___ _____    ____  ___ ___ _   _ 
 / ___|_ _|_   _|  / ___|/ _ \_ _| \ | |
| |  _ | |  | |   | |  _| | | | ||  \| |
| |_| || |  | |   | |_| | |_| | || |\  |
 \____|___| |_|    \____|\___/___|_| \_|
"""
afplay /Users/Peregrine/Downloads/dana_start.m4a
sleep 1
echo $seperate
convey "Git status shown below" "GIT STATUS..." "Daniel"
sleep 1
git status
sleep 1
echo $seperate
sleep 2
convey "Enter the file path from current D I R... Also, X to escape the loop -r 10" "File: " "Fiona"
read file
while [ "$file" != "x" ]
    do
    file_path=$(/bin/pwd)
    if [ "$file" == "all" ]
        then
        git add .
    else
        git add "$file_path/$file"
        convey "Enter another file to add... Or leave with the lowercase letter x -r 8" "File: " "Daniel"
        read file
    fi
done
convey "Enter commit message -r 10" "Commit message: " "Alice"
read commit_message
echo "GIT COMMIT..."
git commit -m "$commit_message"
sleep 3
convey "Git status displayed below" $seperate "Moira"
sleep 1
echo "GIT STATUS..."
git status
echo $seperate
sleep 2
convey "Lowercase Y to create another commit... Lowercase N to proceed to pushing changes -r 8" "Create another commit? [y/n]" "Daniel"
read answer
if [ "$answer" == "y" ]
    then
    new_commit
else
    git_push
    say -v Alex -r 230 "Program shutting down, thank you and see you next time"
    afplay /Users/Peregrine/Downloads/winterspell_30s.m4a
fi