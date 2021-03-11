#!/bin/python3
from pyfiglet import Figlet
import os


'''
EncryptIt is a python hashing program coded by Vu1n3rab1e.

EncryptIt converts text into hash, the speciality of this script is that I've used a new hashing pattern that i made.


METADATA :
I started coding this script by importing pyfiglet module which is used to make the pretty banner of the script. 

The first function I defined is the banner function, in the first line of banner function i declared a variable called custom_fig and set its value to Figlet's graffiti font.
In the second line we are printing the value of text with font set to graffiti.
END OF FUNCTION BANNER

Next we are calling the function banner() with a value "EncryptIt", this will print the banner EncryptIt with the help of pyfiglet module.
In the next three lines we just printed the Version,Authorname, and Disclaimer.


The next 26 lines are the hashing pattern set to variables, as you can see each variable are named alphabets with value of their hash which makes us easy to get the hash value of each letters.


Next we started a while loop so that the code inside the loop again and again and again until the loop is broken.
In the beggining of the while loop, I declared some variables you'll know the use of each when you finish reading this.
First i'll tell you why i put the variables in the starting of the while loop, it is because i can use the value of these variables anywhere in the loop. Suppose i declared a variable in a for loop and you need to use the value of that variable outside the loop if i declared a variable in the for loop then i may not be able to use the value of that variable outside that loop but in fact that i declared the varibles in the beggining of the while loop i can use the value of those variables anywhere in the while loop.


The for loop "for i in invalid:" iterates whatever is in the for loop with each items in the list invalid.
the statement "if i in inp" checks if the value of any item in the invalid list is present in the input or not, if any item in the list invalid is present in the inp (inp is the variable containing the value of input) the statement becomes True and the code inside the if statement executes.

Here in this if statement the value of status is set to "False" and breaks the loop (We used "break" to break the for loop, if we dont break the for loop the loop will continue running until it ends thereby printing multiple eroor statements we coded, we don't need that to happen even if there is one invalid character in the input we are not going to allow the input then why should we run the loop until it ends to find multiple invalid characteres.) and we used "continue" so that we can continue the script.


   



 
'''


def banner(text):
	custom_fig = Figlet(font='graffiti')
	print(custom_fig.renderText(text))

banner("EncryptIt")
print("							V1.0")
print("							Coded by : Vu1n3rab1e")
print("\nDisclimer: The use of LowerCase Letters,Numbers and Symbols are not allowed.\nOnly Input Uppercase Letters.\n")

A = "da8"
B = "8ea"
C = "a9e"
D = "f50"
E = "0d9"
F = "90e"
G = "e9e"
H = "e82"
I = "28e"
J = "ebd"
K = "dc2"
L = "277"
M = "79b"
N = "b7d"
O = "dba"
P = "ada"
Q = "a8e"
R = "ea9"
S = "9ef"
T = "f50"
U = "0d9"
V = "90e"
W = "e9e"
X = "e82"
Y = "28e"
Z = "ebd"


while True:
	output = ""
	inp = ""
	unsupchar = ""
	invalid = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
	status = ""
	inp = input("Enter Sting To Hash : ")
	for i in invalid:
		if i in inp:
			print("The use of LowerCase Letters,Numbers and Symbols are not allowed.")
			status = "False"
			break
			continue


	if "False" in status:
		continue
	else:
		length = len(inp)
	
	for i in range(length):	
		if inp[i] == 'A':
			output += A
			
		elif inp[i] == 'B':
			output += B
		
		elif inp[i] == 'C':
			output += C
		
		elif inp[i] == 'D':
			output += D 
		
		elif inp[i] == 'E':
			output += E
			
		elif inp[i] == 'F':
			output += F
			
		elif inp[i] == 'G':
			output += G
			
		elif inp[i] == 'H':
			output += H
			
		elif inp[i] == 'I':
			output += I
			
		elif inp[i] == 'J':
			output += J
			
		elif inp[i] == 'K':
			output += K
			
		elif inp[i] == 'L':
			output += L
			
		elif inp[i] == 'M':
			output += M
			
		elif inp[i] == 'N':
			output += N
			
		elif inp[i] == 'O':
			output += O
			
		elif inp[i] == 'P':
			output += P
			
		elif inp[i] == 'Q':
			output += Q
			
		elif inp[i] == 'R':
			output += R
			
		elif inp[i] == 'S':
			output += S
			
		elif inp[i] == 'T':
			output += T
			
		elif inp[i] == 'U':
			output += U
			
		elif inp[i] == 'V':
			output += V
			
		elif inp[i] == 'W':
			output += W 
			
		elif inp[i] == 'X':
			output += X
			
		elif inp[i] == 'Y':
			output += Y
			
		elif inp[i] == 'Z':
			output += Z
			
		else:
			print("You have entered an unsupported character.")
			unsupchar = "True"
			break	
	
	if unsupchar == "True":
		continue
	else:
		print("Your Hashed Output  : {}".format(output))
		
	
	repeat = input("\nDo you want to continue ?\nEnter Y/N :  ")
	if repeat == "Y" or repeat == "y" or repeat == "Yes" or repeat == "yes":
		os.system('clear')
		continue
	elif repeat == "N" or repeat == "n" or repeat == "No" or repeat == "no":
		print("Thanks for using EncryptIt.")
		banner("Exiting")
		exit()
	else:
		print("Wrong Input!")
		banner("Exiting")
		exit()
