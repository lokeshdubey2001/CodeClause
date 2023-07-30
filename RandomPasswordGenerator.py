import string 
import random

print("Hii, seems like you want to generate random password")

def main():

    l=int(input("Please enter length of the password: "))

    lowercase=string.ascii_lowercase

    uppercase=string.ascii_uppercase

    digits=string.digits

    symbols=string.punctuation

    c=lowercase+uppercase+digits+symbols

    r=random.sample(c,l) 

    password="".join(r)

    print(password)
    main()
    
main()