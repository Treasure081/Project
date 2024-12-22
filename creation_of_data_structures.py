okpa_list=["bambara nut",
           "red oil",
           "maggi",
           "salt",
           "egg"
           ]

#to append an item
print(okpa_list)
okpa_list.append("fish")
print(okpa_list)

#to check for an item in the list
ingredient=input("Enter an ingredient for okpa:")
for item in okpa_list:
    if item==ingredient:
        print(item,"is in the list.")





#Creating a list
numbers=(4,8,12,16,20,24,28)
total=0
for number in numbers:
    total=total+number
    print(total)
