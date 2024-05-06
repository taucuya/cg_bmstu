#!/bin/bash

export LC_NUMERIC=en_US.UTF-8

var=$(grep -o '[0-9]*%' new.txt)
new_var="${var%?}"
fin_var=$(echo "$new_var" | bc)
printf "%.2f\n" $fin_var