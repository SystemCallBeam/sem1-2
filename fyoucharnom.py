import base64
import subprocess
import re

# Path to the .exe program
PROGRAM_PATH = ".\\shanomkaimook.exe"

# Function to run the external program
def run_program():
    """Starts the external program and returns the process."""
    return subprocess.Popen(PROGRAM_PATH, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Function to communicate with the program
def communicate_program(process, input_char):
    """Send a character to the running process and capture the output."""
    process.stdin.write(input_char + '\n')
    process.stdin.flush()  # Ensure input is sent
    return process.stdout.readline()

# Function to ensure base64 string has correct padding
def add_padding(base64_string):
    """Add necessary padding to base64 string."""
    return base64_string + '=' * (-len(base64_string) % 4)

# Function to extract multiplication questions
def extract_pattern(text):
    """Extract the word and number in the format 'word * number'."""
    match = re.search(r'(\w+) \* (\d+)', text)
    return match.groups() if match else None

# Function to parse multiplication question from the program output
def parse_multiplication_question(output):
    """Extract the number in the format 'Question: <num>/...'."""
    match = re.search(r'Question: ([^/]+)/', output)
    return match.group(1) if match else None

# Function to find text after 'Result:'
def find_txt(input_text):
    """Extract text following 'Result:'."""
    match = re.search(r"Result:\s*(.*)", input_text)
    return match.group(1) if match else None

# Function to extract the hash after 'Correct!'
def get_hash(input_text):
    """Extract hash following 'Correct!'."""
    match = re.search(r"Correct!\s*([a-fA-F0-9]+)", input_text)
    return match.group(1) if match else None

# Main function for brute-forcing
def brute_force():
    """Automates the brute-force process by communicating with the program."""
    process = run_program()

    with open("output.txt", "w") as output_file:
        while True:
            # Read the program's output
            read_line = process.stdout.readline()
            # print(f"Program Output: {read_line.strip()}")

            # Parse the multiplication question
            num1 = parse_multiplication_question(read_line)

            if num1:
                try:
                    # Decode the number from base64
                    ascii_char = base64.b64decode(add_padding(num1)).decode('utf-8')

                    # Extract the text and repeat count
                    txt, num2 = extract_pattern(ascii_char)
                    input_str = txt * int(num2)

                    # Send the input to the program and capture output
                    output_str = communicate_program(process, input_str)

                    # Extract the base32-encoded string and decode it
                    base32_encode = find_txt(output_str)
                    decoded_bytes = base64.b32decode(base32_encode)
                    base32_decode = decoded_bytes.decode('utf-8')

                    # Extract and print the hash
                    hash_value = get_hash(base32_decode)
                    if hash_value:
                        # print(f"Hash: {hash_value}")
                        output_file.write(f"{base32_decode}\n")

                except Exception as e:
                    print(f"Error occurred: {e}")
            else:
                print(f"Unhandled output: {read_line}")
                break

    process.terminate()

if __name__ == "__main__":
    brute_force()

