#!/bin/bash

#Read in variables from python script
dir=$1
root_dump=$2
hist_dump=$3

#Define C++ script used for histogram extraction
script="/Extract_histos.C"
script_path=$dir$script

#Use ls to get root files in proper directory and read into space deliminated string
files1=($(ls ${root_dump}))
files=$(IFS=' '; echo "${files1[*]}")
#echo $files



#run histogram extraction script
root -l -b -q "$script_path(\"${root_dump}\",\"${hist_dump}\",\"${files}\")"



