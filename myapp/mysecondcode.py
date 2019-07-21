#this programe check given number PRIME or not

#num = 407


#take input from the user
 num = int(input("Enter the number: "))

#prime numbers are grater than 1

if num > 1:

  for i in range(2,num):
      if(num % i) == 0:
        print(num,"is not a prime number")
        break
  else:

     print(num,"is a prime number")

# if the number is less than 1 it is not a prime
else:

     print(num,"is not a  prime number")
 

  
