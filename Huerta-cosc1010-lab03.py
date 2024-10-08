# Julian Huerta
# UWYO COSC 1010
# 09/26/2006
# Lab 03 
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here



# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list

states_list = ["wyoming" , "Colorado", "Montana"]

#print the entire list

print(states_list)

#now print the first element in the list

print(states_list[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)

print(states_list[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided

location = f"{states_list[1]} is south of {states_list[0]}"

print(location)

print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list

states_list.append("Washington")

states_list.append("Oregon")

states_list.append("California")

print(states_list)

#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 

states_list[-2]= "Maine"

print(states_list)

#Insert the state Texas to be the third element in the list, again printing your list

states_list.insert(2, "Texas")

print(states_list)

#Using the `del` statement remove the fourth item from the list, print your list 

del states_list[3]

print(states_list)

#Remove Texas using its value, print the list

states_list.remove("Texas")

print(states_list)

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 

print(sorted(states_list))


#Permanently sort your list in reverse order, printing it out

states_list.sort(reverse=True)

print(states_list)

#Using the reverse method reverse the list and print it

states_list.reverse()

print(states_list)