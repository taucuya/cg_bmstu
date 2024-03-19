#!/bin/bash

if test -f "report-unittesting-latest.txt"; then
    cp report-unittesting-latest.txt report-unittesting-old.txt
fi

if test -f "report-functesting-latest.txt"; then
    cp report-functesting-latest.txt report-functesting-old.txt
fi