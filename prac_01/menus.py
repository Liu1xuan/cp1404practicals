name = str(input("Enter name: ")).capitalize()
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
print(MENU)
choice = str(input(">>> ")).upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    name = str(input("Enter name: "))

else:
    print("Finished.")
