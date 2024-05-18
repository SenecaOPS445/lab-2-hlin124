#!/usr/bin/env python3
#Author: Haley Lin
#Author ID: hlin124
#Date Created 2024/05/18

import sys

if len(sys.argv) == 1:
    timer = 3
elif len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    sys.exit()
    
while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')