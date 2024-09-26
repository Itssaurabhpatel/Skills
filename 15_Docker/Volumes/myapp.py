# Prompt the user to enter a name or string to store in the file
add_name = input("Enter a name or string to store in the file: ")

# Ensure the input is not empty before storing
if add_name.strip():
    try:
        with open('user_info', 'a') as file:  # Open in append mode
            file.write(f'{add_name}\n')
        print(f"'{add_name}' has been added to the user_info file.")
    except Exception as e:
        print(f"Error: {e}, {type(e).__name__}")
else:
    print("No name or string was added to the file.")

# Now prompt the user if they want to see all users' names
show_info = input("Do you want to see all users' names? (y/n): ")

if show_info == 'y':
    try:
        with open('user_info', 'r') as file:
            content = file.readlines()
    except Exception as e:
        print(f"Error: {e}, {type(e).__name__}")
    else:
        if content:
            print("Stored user names/strings:")
            for line in content:
                print(f'{line.rstrip()}')
        else:
            print("No user information found.")
elif show_info == 'n':
    print("You chose not to view the user names.")
else:
    print("Invalid input. Please enter 'y' for yes or 'n' for no.")
