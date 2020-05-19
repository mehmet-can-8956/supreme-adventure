#part1#
my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]
my_list.sort()
print(my_list[0]+my_list[1])
my_list.reverse()
print(my_list[0]+my_list[1])
print("\n")

#part2#
names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", 
          "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra"]
scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]
name=input("Enter the student\'s name :")
print(name, "\'s score:", scores[names.index(name)], "\n")

#part3#
scores.sort(reverse=True)
print("The maximum score is:",scores[0])
print("Score", scores[0] , "was got by", scores.count(scores[0]), "person")

#part4#
months = [["January",31],["February",28],["March",31],["April",30],["May",31],["June",30], 
["July",31], ["August",31], ["September",30], ["October",31], ["November",30], ["December",31]]
print(months,"\n")

#part5#
spring = months[2:5]
summer = months[5:8]
fall   = months[8:11]
winter = months[-2:]+months[0]

print("spring:", spring)
print("summer:", summer)
print("fall  :", fall)
print("winter:", winter)

#part6#
summer_days=summer[0][1]+summer[1][1]+summer[2][1]
print("Summer days duration:", summer_days)