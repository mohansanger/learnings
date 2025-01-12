
def print_formatter(number):
   width=len((bin(number))[2:])
   print(width)
   for i in range(1,number+1):
       deci=str(i)
       octa=oct(i)[2:]
       hexa=hex(i)[2:].upper()
       bina=bin(i)[2:]
       print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width),sep=" ")
   

if __name__=="__main__":
    n=int(input("Enter the Number:"))
    print_formatter(n)
