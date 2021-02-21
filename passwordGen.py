import hashlib
import random

# Moved to start so it could be initalized before the if-elseif-else block starts
password=""

# added some hashing algorithms in addition to the original because i thought they made good password generators
algorithm = input("MD5[M], SHA256[S], or default[D]?")

# wanted to make sure program catches lowercase letters
algorithm = algorithm.upper()

# original generation algorithm
if(algorithm == "" or algorithm[0] == "D"):
    print("How long do you want your generated password to be? ",end="")
    long=int(input())
    cont=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","/","*","!","_","&","=","+","-","(","[","|",")","]"]
    for i in range(long):
        count=random.randrange(0,73,1)
        password=password+cont[count]
# MD5 and SHA stuff
else:
    word = input("Enter a word or phrase!")
    if(algorithm[0] == "M"):
        hash_object = hashlib.md5(word.encode())
        password = hash_object.hexdigest()
    
    if(algorithm[0] == "S"):
        hash_object = hashlib.sha256(word.encode("utf-8"))
        password = hash_object.hexdigest()
print(password)
