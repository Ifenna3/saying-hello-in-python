#Ask user for their name
name = input("What is your name ").strip().title()

#Split user's username into first name and last name
first, last = name.split("")

#Different ways of writing your name or anything using the print statement
print(f"Hello, {name}")
print(f"Hello, {first}") # For some reason, this code isn't working
print("Hello, " + name)
print("Hello,", name )



#Remove whitespace from str (Feel free to comment out the function below to understand what the strip does to the code)
#name = name.strip().title()

#Capitalize user's name
#name = name.capitalize() #Only capitalize the first letter in the string
#name = name.title() # capitalize all the first letter when a space is implemented