#part1
degree=input("""Please enter the degree and
press F for F to C
press C for C to F :""")
                
Entered_Type=degree[-1]
new_degree=int(degree[:-1])

if Entered_Type=="f" or Entered_Type=="F":
   c = (5/9) * (new_degree - 32)
   print("\"",new_degree,"F\"   -->   \"{:.1f}C\"".format(c))
elif Entered_Type=="c" or Entered_Type=="C":
   f = ((9/5) * new_degree) + 32
   print("\"",new_degree,"C\"   -->   \"",f,"F\"")
else: print("Please enter correctly")
print("\n")

#part2 Fibonacci numbers from 1 to 50.
print("Fibonacci numbers from 1 to 50")
number1=1
number2=2
fibonacci=[1,1]
while number2 < 51:
    depot=number2+number1
    number1=number2
    fibonacci.append(number2)
    number2=depot
print(fibonacci,"\n")

#part3
service=int(input("What is your year of service:"))
if service > 5:
   salary=int(input("How much is your salary:"))
   bonus=salary*1.05
   print("Your net bonus amount:",bonus)
elif service <= 5:
   print("Sorry you didnt deserve bonus yet")
print("\n")

#part4
age1=int(input("Enter your age please:"))
age2=int(input("Enter your age please:"))
age3=int(input("Enter your age please:"))

if   age1<age2 and age2<age3:
   print("first entered person is youngest, third entered person is oldest")
elif age1<age3 and age3<age2:
   print("first entered person is youngest, second entered person is oldest")
elif age2<age1 and age1<age3:
   print("second entered person is youngest, third entered person is oldest")
elif age2<age3 and age3<age1:
   print("second entered person is youngest, first entered person is oldest")
elif age3<age1 and age1<age2:
   print("third entered person is youngest, second entered person is oldest")
elif age3<age2 and age2<age1:
   print("third entered person is youngest, first entered person is oldest")
print("\n")

#part5
held=float(input("Enter the number of classes held:"))
attended=float(input("Enter the number of classes attended:"))

attendence=attended/held
print("Your percentage of classes attended {:.2f}".format(attendence))
if attendence<0.75:
   print("You are not allowed to attend the exam")
else:
   print("You are allowed to attend the exam")
print("\n")

#part6
letter=input("Enter a letter from Alphabet please:")

if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
   print(letter,"is a vowel")
elif letter=="y":
   print(letter,"is sometimes a vowel and sometimes a consonant")
else:
   print(letter,"is a constant")

