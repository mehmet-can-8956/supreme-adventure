#part1#
capital=1000
daily_growth=0.12
period=7
growth_rate=(1+daily_growth)
final_growth_rate=growth_rate**period
total_amount=capital*final_growth_rate
print("total amount :",total_amount,"$","\n")

#part2#
print("""When we buy bitcoin with {} USD at the beginning of the week,
we would earn {:.2f} USD at the end of the week,
with an average gain of 12\%.""".format(capital,total_amount-capital),"\n")

#part3#
f=input("Enter the temperature in Fahrenheit:")
c=(5/9)*(int(f)-32)
text="Temperature (C) : {:.2f}"
print(text.format(c),"\n")

#part4#
number=input("Enter a 3 digit number :")
sum_of_digits=int(number[0])+int(number[1])+int(number[2])
print("The sum of digits in the number is {}".format(sum_of_digits),"\n")

#part5#
first_side=input("Enter the first side\'s length of the triangle :")
second_side=input("Enter the second side\'s length of the triangle :")
hypotenuse=(int(first_side)**2)+(int(second_side)**2)
from math import sqrt
t=sqrt(hypotenuse)
print("The length of the hypotenuse is :", int(t))
