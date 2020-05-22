#part1
number=int(input(["Enter a number between 1-9:"]))

for i in range(1,11):
  print(number,"X",i,"=",i*number)
print("\n")

#part2
numbers=[]
for i in range(1,21):
   if i%2==1:
     numbers.append(i**2)
   else:
     numbers.append(i**3)
print(numbers)
print("\n")

#part3
word=input("Please type a word:")
print(word,"------>",word[::-1],"\n")

#part4
even_numbers=[]
odd_numbers=[]
for i in range(2,201,2):
   even_numbers.append(i)
for i in range(1,202,2):
   odd_numbers.append(i)
print(even_numbers)
print(odd_numbers)

#part5
numb=list(input("Enter a 8 digit number:"))
i=input("Enter the number that will be counted")
print(numb)
print(numb.count(i))

#part6
n=input("Enter a number:")
print(n,"-->")
digit_sum=0

for i in range(len(n)):
   digit_sum=digit_sum+int(n[i])
print(digit_sum)

if len(str(digit_sum))>1:
   digit_sum2=0
   m=str(digit_sum)
   for i in range(len(m)):
     digit_sum2=digit_sum2+int(m[i])
   print(digit_sum2)
if digit_sum2>9:
   digit_sum2=digit_sum2%10+digit_sum2//10
   print(digit_sum2)
#part7
number1=int(input("to find greatest common divisor enter the first number:"))
number2=int(input("Enter the second number:"))
r=1
if number2>number1:
   while r!=0:
     r=number2%number1
     number2=number1
     number1=r
   print("Greatest common divisor:",number2)
if number1>number2:
   while r!=0:
     r=number1%number2
     number1=number2
     number2=r
   print("Greatest common divisor:",number1)

#part8
for i in range(1,51):
   if i%15==0:
     print("fizzbuzz")
   elif i%5==0:
     print("buzz")
   elif i%3==0:
     print("fizz")
   else:print(i)
