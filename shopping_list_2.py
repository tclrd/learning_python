#make a list to hold onto our items
items = []
#print out instructions on how to use the app
def show_help():
    print("Welcome to the shopping app!")
    print("""
        Enter 'QUIT' to stop adding items.
        Enter 'HELP' for help.
        Enter 'SHOW' to see your current list.
    """)
def show_list(greeting):
    print(greeting+": "+", ".join(items)+".")

show_help()
print("Happy shopping!")

go = True
while go:
    entry = (raw_input(">> "))
    if (entry.lower() == "help"):
        show_help()
    elif (entry.lower() == "show"):
        show_list("So far we have")
    elif ((entry.lower() == "quit") or (entry.lower() == "done")):
        if (items.__len__() == 0):
            print("Your list is empty!")
            continue
        else:
            go = False
            show_list("Your list for today is")
    else:
        items.append(entry)
