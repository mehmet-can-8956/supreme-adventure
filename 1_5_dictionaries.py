#part1#
sevendays={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
print(sevendays,"\n")
number=input("Enter the numbers of the days which will be deleted:")
sil1=int(number[0])
sil2=int(number[1])
del sevendays[sil1]
del sevendays[sil2]
print(list(sevendays.values()))

#part2#
print("\n")
personnel={"John":["male",25],"Lisa":["female",28],"Linda":["female",31],"Michael":["male",41]}
print(personnel,"\n")

#part3
personnel.update({"Michael":{"sex":"male","age":41,"child":{"Karen":["female",12],"Greg":["male",7]}},
"Linda":{"sex":"female","age":31,"child":{"Susan":["female",6]}}})
print(personnel,"\n")

#part4
print(list(personnel["Michael"]["child"]))
print("\n")


