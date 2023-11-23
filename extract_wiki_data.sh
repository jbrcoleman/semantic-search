#!/usr/bin/env bash
# Download stemmed wikipedia data
wget http://blob.thijs.ai/wiki-summary-dataset/stemmed.tar.gz
# Untar File
tar -xvzf stemmed.tar.gz
#create json file 
jq -Rs '[ split("\n")[] | select(length > 0) | split(" ||| ") | {name: .[0], summary: .[1]} ]' stemmed.txt > stemmed.json