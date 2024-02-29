#!/bin/bash
size=$(curl -s -I "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r')
echo $size
