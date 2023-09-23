get_name = input("Enter a Name: ")
print("""(H)ello
(G)oodbye
(Q)uit
""")
get_choice = input("Enter a Choice: ").upper()

while get_choice != "Q":
    if get_choice == "H":
        print("Hello", get_name)
    elif get_choice == "G":
        print("Goodbye", get_name)
    else:
        print("Invalid message")
    print("""(H)ello
(G)oodbye
(Q)uit
""")

    get_choice = input("Enter a Choice: ").upper()
print("Finished message")
