# Define a dictionary to hold variables
variables = {}

# Function to process the 'let' command (e.g., let x = 5)
def process_assignment(line):
    # Strip spaces and split by '='
    parts = line.replace('let ', '').split('equal')
    var_name = parts[0].strip()
    value = parts[1].strip()
    variables[var_name] = int(value)  # Store the variable in the dictionary

# Function to process the 'print' command
def process_write(line):
    # Remove 'write' keyword and strip spaces
    content = line.replace('write: ', '').strip()
    
    # Check if the content is a string literal
    if content.startswith('"') and content.endswith('"'):
        print(content[1:-1])  # Print the string without quotes
    else:
        # Handle the case where the content is a variable
        print(variables.get(content, "Null"))  # Print the variable value
# eee
def process_addition(line):
    parts = line.replace('add: ', '').split()
    try:
        result = sum(int(x) if x.isdigit() else variables.get(x, 0) for x in parts)
        print(f"Answer: {result}")
    except Exception as e:
        print(f"Error: {e}")
# eee
def process_subtraction(line):
    parts = line.replace('subtract: ', '').split()
    try:
        # Start with the first value
        result = int(parts[0]) if parts[0].isdigit() else variables.get(parts[0], 0)
        for part in parts[1:]:
            value = int(part) if part.isdigit() else variables.get(part, 0)
            result -= value  # Subtract each value
        print(f"Answer: {result}")
    except Exception as e:
        print(f"Error in subtraction: {e}")


# Main function to interpret the program
def interpret_program(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()  # Remove leading/trailing spaces
        if line.startswith('let'):
            process_assignment(line)  # Process variable assignment
        elif line.startswith('write'):
            process_write(line)  # Process print command
        elif line.startswith('add'):
            process_addition(line)  # Process addition command

# Run the interpreter on a given program file
if __name__ == "__main__":
    file_name = 'program.txt'  # Name of the file to run
    interpret_program(file_name)
