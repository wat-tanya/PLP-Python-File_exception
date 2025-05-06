def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            contents = file.read()

        # Modify the contents (e.g., convert to uppercase)
        modified_contents = contents.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_contents)

        print(f"Modified content has been written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"❌ Error: Could not read the file '{filename}'.")

# Run the function
read_and_modify_file()
