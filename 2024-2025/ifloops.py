# first ask the users name and store it for later
name = input(f"hello new user. how would you like me to refer to you? \n\t")

# ask the user for the number of lights nessasary and then multiply if by the cost per light
dynamicLightCount = input(f"welcome {name} \n how many dynamic lights would you like to add? \n\t")

costPerLight = 3

print(f"alright that many lights would cost you {int(dynamicLightCount)*costPerLight}ms of render time :)")