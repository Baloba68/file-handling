def file_read_write():
    try:
        # Ask user for input file name
        input_file = input("Enter the filename to read: ")

        # Open the input file for reading
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content (for example: make everything uppercase)
        modified_content = content.upper()

        # Create a new output file and write modified content
        output_file = "modified_" + input_file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"File has been modified and saved as '{output_file}'")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the function
file_read_write()