def read_and_modify_file(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes the modified content to a new file.
    """
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify content 
        modified_content = content.upper()
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{input_filename}' or write to '{output_filename}'.")

# Ask for filenames
input_file = input("Enter the name of the file to read from: ")
output_file = input("Enter the name of the file to write to: ")

read_and_modify_file(input_file, output_file)
