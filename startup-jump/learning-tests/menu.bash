#!/bin/bash

# options=("matthew" "mark" "luke" "john")
# select name in ${options[@]}
# do
#     echo "$name selected"
# done

options=("mathew" "mark" "luke" "john" "ok")
select name in ${options[@]}
do
    case $name in
    mark)
    echo "Mark selected"
    ;;

    mathew)
    echo "Mathew selected"
    ;;

    luke)
    echo "luke selected"
    ;;

    john)
    echo "john selected"
    ;;

    ok)
    echo "all g"
    ;;

    *)
    echo "Please provide number between 1 and 4"
    esac
done