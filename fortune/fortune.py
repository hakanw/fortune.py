#!/usr/bin/env python
# encoding: utf-8
#
# fortune.py – a simple fortune cookie you can place in your .bashrc
#
# Written by Håkan Waara (hwaara@gmail.com) at 10 sept, 2014
#

from glob import glob
import random

def main():
    with open(random.choice(glob('cookiesets/*.txt')), "r") as f:
        print("\n"+random.choice(f.readlines()))

if __name__ == "__main__":
    main()
