#make a list to hold onto our items
items = []
#print out instructions on how to use the app
print("Welcome to the shopping app!")
print("To use the shopping app, simply type the name of your item below and submit with the return key.")
print("Once finished, type QUIT to exit and view your list!")
print("Happy shopping!")

cont = True
while cont:
  input = raw_input("Item: ")
  if (input.lower() == "quit"):
    cont = False
    print("Your list for today is: " + ", ".join(items))
  else:
    #ask for new items
    items.append(input)
    #add new items to our list

