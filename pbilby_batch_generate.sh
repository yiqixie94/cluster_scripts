#!/bin/bash

while read path
do
  cd $path
  parallel_bilby_generation config.ini
done < "/dev/stdin"

#path=$1
#cd $path
#parallel_bilby_generation config.ini
