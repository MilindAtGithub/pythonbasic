# This is the utility to encrypt any user input
from finxencryption.pyfinxencryption import finXEncryption
import  getpass
userinput = getpass.getpass("Enter the password To Encrypt: ")

length = len(userinput)
modulo = length %16
if modulo !=0 :
    divider = int(length/16) + 1
    userinput = userinput.rjust(divider*16 ,' ')

f =finXEncryption()
s = str(f.encryptData(userinput),'utf-8')
print(f"Copy the Encrypted Text: {s}")
#print (str(f.decryptData(s),'utf-8').lstrip())s