#Pyfancy 0.2.5 by Cosmic Open Source Projects learn more at https://github.com/ilovecode1/pyfancy

documentation = ("Type documentation() for help or go to https://github.com/ilovecode1/pyfancy!")

def documentation(input=None):
	
	if (input == None):
		
		print('''BLUE\nprint (pyfancy.BLUE + "Hello Blue!" + pyfancy.END)\nGREEN\nprint (pyfancy.GREEN + "Hello Green!" + pyfancy.END)\nYELLOW\nprint (pyfancy.YELLOW + "Hello Yellow!" + pyfancy.END)\nRED\nprint (pyfancy.RED + "Hello Red!" + pyfancy.END)\nPINK\nprint (pyfancy.PINK + "Hello Pink!" + pyfancy.END)\nLIGHTBLUE\nprint (pyfancy.LIGHTBLUE + "Hello Lightblue!" + pyfancy.END)\nLIGHTGREEN\nprint (pyfancy.LIGHTGREEN + "Hello Lightgreen!" + pyfancy.END)\nLIGHTRED\nprint (pyfancy.LIGHTRED + "Hello Lightred!" + pyfancy.END)\nLIGHTGREY\nprint (pyfancy.LIGHTGREY + "Hello Lightgrey!" + pyfancy.END)\nDARKGREY\nprint (pyfancy.DARKGREY + "Hello Darkgrey!" + pyfancy.END)\nCYAN\nprint (pyfancy.CYAN + "Hello Cyan!" + pyfancy.END)\nPURPLE\nprint (pyfancy.PURPLE + "Hello Purple!" + pyfancy.END)\nBOLD\nprint (pyfancy.BOLD + "Hello Bold!" + pyfancy.END)\nUNDELINE\nprint (pyfancy.UNDERLINE + "Hello Underline!" + pyfancy.END)\nREVERSE\nprint (pyfancy.REVERSE + "Hello Reverse!" + pyfancy.END)\nSTRIKETHROUGH\nprint (pyfancy.STRIKETHOUGH + "Hello Strikethough!" + pyfancy.END)\nINVISABLE\nprint (pyfancy.INVISABLE + "Hello Invisable!" + pyfancy.END)''')
    
    else:
    	
    	print(input + " is not avalible!")

class pyfancy:

	END = '\033[0m'
	PURPLE='\033[35m'
        CYAN='\033[36m'
        LIGHTGREY='\033[37m'
        DARKGREY='\033[90m'
        LIGHTRED='\033[91m'
        LIGHTGREEN='\033[92m'
        LIGHTBLUE='\033[94m'
        PINK='\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	REVERSE='\033[07m'
        STRIKETHROUGH='\033[09m'
        INVISABLE='\033[08m'
        
        
def demo():
	print(pyfancy.RED + "HELLO RED!" + pyfancy.END)