# This is my first Codecool project, the Hello World program
# It shall ask for a name, then write 'Hello XY'
# OR if no name give simply output 'Hello World'
# ===================================================
# 	-=By: Csányi Levente, Codecool BP 1st semester=-

import sys

def HelloSys():
	if len(sys.argv) > 1:
		print("Hello ",sys.argv[1])
	else:
		print("Hello World")

HelloSys()
