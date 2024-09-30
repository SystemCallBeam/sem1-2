import subprocess
import re

# Path to the .exe program
program_path = "\"C:\\Users\\tkhae\\Desktop\\New folder\\5timeFLAG.exe\""

# Function to run the program and send input
def run_program():
    # Start the program and send input
    process = subprocess.Popen(program_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    return process

def communicate_program(process, input_char):
    """Send a character to the running process and capture the output."""
    # Send the input character to the program and get the output
    process.stdin.write(input_char + '\n')
    process.stdin.flush()  # Ensure the input is sent
    output = process.stdout.readline()  # Read the program's response

    return output

# Function to extract multiplication question from the program output
def parse_multiplication_question(output):
    # Regex pattern to extract the multiplication question (e.g., 113 * 1 = 113)
    pattern = r"(\d+)\s*\*\s*(\d+)\s*=\s*(\d+)"
    match = re.search(pattern, output)
    
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        return num1, num2
    else:
        return None, None

# Main brute-force automation function
def brute_force():
    # Run the program and capture the output
    process = run_program()
    while True:  # Keep running until the program terminates
        
        # Print the program's output
        read_line = process.stdout.readline()
        
        # print(f"Program Output:\n{read_line}")
        
        # Parse the multiplication question from the process
        num1, num2 = parse_multiplication_question(read_line)
        
        if num1 is not None and num2 is not None:
            # Get the ASCII character for the first number (num1)
            ascii_char = chr(num1)
            
            # Repeat the character num2 times
            input_sequence = ascii_char * num2
            # print(f"Entering ASCII({num1}) '{ascii_char}' {num2} times: {input_sequence}")
            
            # Run the program with the generated input sequence
            result = communicate_program(process, input_sequence)
            # print(f"{result}\n")
            
            # Break the loop if we get a final answer or a special message
            # if don't find "enter the character" in result.lower: break?
            if "enter the character" not in result.lower():
                # print(f"{result}\n")
                break
        else:
            print(f"{read_line}")
            break
        
    process.terminate()  

if __name__ == "__main__":
    brute_force()
