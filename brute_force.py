import subprocess

# The path to your executable
program_path = "\"C:\\Users\\tkhae\\Desktop\\New folder\\programingTRYTRYTRY.exe\""

# The list of possible characters (1/33)
possible_chars = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"  # Modify this according to the characters allowed
max_length = 33  # Total characters expected

# Function to run the program and interact with it
def run_program():
    # Run the executable using subprocess
    process = subprocess.Popen(program_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    return process

def communicate_program(process, input_char):
    """Send a character to the running process and capture the output."""
    # Send the input character to the program and get the output
    process.stdin.write(input_char + '\n')
    process.stdin.flush()  # Ensure the input is sent
    output = process.stdout.readline()  # Read the program's response

    return output

# Function to brute-force one character at a time
def brute_force():
    correct_input = ""
    incorrect_char = 0
    process = run_program()
    
    while len(correct_input) < 33:
        
        for char in correct_input:
            
            response = communicate_program(process, char)
        
        for position in range(len(correct_input) + 1, max_length + 1):  # Iterate for each position (1/33)
            
            while True:
                char = possible_chars[incorrect_char]
                
                # Run the program with the current attempt
                response = communicate_program(process, char)
                
                # Check the program's response
                if "correct!" in response.lower():
                    print(f"Correct character at position {position}: {char}")
                    correct_input += char  # Add correct char to our input
                    incorrect_char = 0
                    break
                
                elif "wrong character! try again." in response.lower():
                    incorrect_char += 1
                    break
                
            if incorrect_char != 0:
                break
          
    process.terminate()  
    print(f"Final Correct Sequence: {correct_input}")

# Start the brute-forcing process
brute_force()
