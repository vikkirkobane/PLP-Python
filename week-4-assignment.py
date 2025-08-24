def modify_file(input_filename, output_filename):
    try:
        # Step 1: Read the contents of the input file
        with open(input_filename, "r") as file:
            content = file.read()
        
        # Step 2: Modify the content (convert to uppercase)
        modified_content = content.upper()
        
        # Step 3: Write the modified content to the output file
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)
        
        print(f"Success! The modified content has been written to {output_filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for the filename
input_file = input("Enter the name of the input file (with extension): ")
output_file = input("Enter the name of the output file (with extension): ")

# Call the function with user-provided filenames
modify_file(input_file, output_file)
