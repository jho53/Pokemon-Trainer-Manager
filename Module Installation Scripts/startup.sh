#!/bin/bash
read -n1 -r -p "Press space to continue..." key

if [ "$key" = '' ]; then
    pip install pygame
    pip install pillow
else
    exit
fi
