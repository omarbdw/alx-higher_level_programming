#!/bin/bash
size=$(curl -s "$1" | wc -c)
echo $size
