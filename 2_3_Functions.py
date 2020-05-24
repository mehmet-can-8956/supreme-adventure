#part1
number=int(input("Enter a number to check if it is prime:"))
def prime(number):
   a="is a Prime number"
   for i in range(2,number):
     if number%i==0:a="is not a Prime number"
   return a
print(number, prime(number))

#part2:each element once to a new list.set() command
list1=list(input("Enter the elements of a list:")) 
print(list1)
new_list2=[]
def arranged_list(list2):
   new_list=list2
   for i in range(len(list2)):
     for y in range (len(new_list)):
       if y!=i:
         if new_list[y]==list2[i]:
           new_list[y]="d"
   for i in range(len(new_list)):
     if new_list[i]!="d":
       new_list2.append(new_list[i])
   return new_list2
print(arranged_list(list1))

#part3
day=int(input("Day of birth:"))
month=int(input("Month of birth:"))
year=int(input("Year of birth:"))

def age(year, month, day):
   from datetime import date 
   today = date.today() 
   age=today.year-year
   if month>today.month:
     age=age-1
   if month==today.month:
     if day>today.day:
       age=age-1
   return age
print(age(year, month, day))

#part4
number=int(input("Enter a number for factoriel:"))

def fact(number):
   fact=1
   for i in range(1,number+1):
     fact=fact*i
   return fact
print(fact(number))

#part5
number=int(input("Enter a number:"))

def perfect(number):
   result="Not Perfect Number"
   a=1
   for i in range(2,number-1):
     if number%i==0:
       a=a+i
   if number==a:
     result="Perfect Number"
   return result
print(number,"is",perfect(number))   

for i in range(1,1000):
   if perfect(i)=="Perfect Number":
     print(i)

#part6
number=int(input("Enter a number:"))

def pascal(number):
   row=[1,1]
   for i in range (number):
     for y in range(i):
       row[i-y+1]=(row[i-y]+row[i-y+1])
     row.append(1)
     print(row[1:])
   return pascal
pascal(number)
