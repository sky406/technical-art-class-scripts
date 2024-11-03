print("hello user and wlecome to the pool party application association")
partyItems = []
print("please list your seven items")

#  this part just loops the input to fill up the party item list 
while len(partyItems)< 7:
    partyItems.append(input(f"item {len(partyItems)+1}: "))

# this part makes sure that the 8th item is inseted before the last item
print("you should add one more item")
partyItems.insert(-1,input(f"what item would that be: " ))

for i in partyItems:
    print(i)