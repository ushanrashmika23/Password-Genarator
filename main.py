import sys
from random import randint
import clipboard as clip

charList="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%&"
password=''

print("Password Generator Started.")
print("Generating...")

try:
	charCount=int(sys.argv[1])
	for i in range(charCount):
		index=randint(0,(len(charList)-1))
		password=password+charList[index]
	clip.copy(password)
	print("Password copied to clipboard.")
	print("Password is : "+password)
except:
	print("Error while generating !!! \n[*] Check and run again main.py as this,\n 	 python main.py countOfCharactors")

