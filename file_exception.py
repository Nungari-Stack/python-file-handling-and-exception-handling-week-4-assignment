# file_exception_assignment.py

# --- File Read & Write Challenge ---
def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            lines = infile.readlines()

        # Example modification: add line numbers and convert to uppercase
        modified = [f"{i+1}: {line.upper()}" for i, line in enumerate(lines)]

        with open(output_file, "w") as outfile:
            outfile.writelines(modified)

        print(f"Modified content written to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# --- Error Handling Lab ---
def read_file_with_error_handling():
    filename = input("Enter a filename to read: ")

    try:
        with open(filename, "r") as f:
            print("\nFile contents:")
            print(f.read())

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    finally:
        print("Program finished.")


# Run the functions
modify_file("input.txt", "output.txt")
read_file_with_error_handling()
