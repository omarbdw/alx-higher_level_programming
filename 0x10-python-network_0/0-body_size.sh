#!/bin/bash
size=$(curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r')
echo $size
