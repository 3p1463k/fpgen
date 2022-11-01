#! /bin/bash

echo "Enter projectname : "
read varname

echo "Do you wish to install this program?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) mkdir varname; exit;;
        No ) exit;;
    esac
done

#echo Creating directories in:  $(pwd)
#mkdir backend
# cp  backend
