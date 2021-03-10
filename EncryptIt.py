#!/bin/python3
from pyfiglet import Figlet
import os

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
