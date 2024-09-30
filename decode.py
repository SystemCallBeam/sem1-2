import re
import base64
import subprocess

def extract_encoded_string(text):
    """Extract Base64 encoded string from the input"""
    pattern = r'Question:+\s*([^/]+)'
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()  # Return the Base64 string
    return None

def decode_base64(encoded_string):
    """Decode Base64 string"""
    try:
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    except Exception as e:
        print(f"Error decoding Base64: {e}")
        return None

def parse_decoded_string(decoded_string):
    """Parse the decoded string to find the pattern 'str * number'"""
    pattern = r"'(\w+)' \* (\d+)"
    match = re.search(pattern, decoded_string)
    if match:
        word = match.group(1)  # The 'xxx' string
        times = int(match.group(2))  # The number '69'
        return word, times
    return None, None

def write_to_file(word, times, file_name='output.txt'):
    """Write the string 'xxx' repeated '69' times to a file"""
    with open(file_name, 'a') as f:
        f.write(word * times + '\n')
    print(f"Written '{word}' repeated {times} times to {file_name}")

def run_exe_and_parse():
    """Run the .exe file, parse the output, and input the correct answer."""
    try:
        # Open the .exe as a subprocess
        process = subprocess.Popen(['./shanomkaimook.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        while True:
            # Read output from the program
            output = process.stdout.readline()
            
            if "Question:" in output:
                
                # Extract the Base64-encoded part
                encoded_string = extract_encoded_string(output)
                
                if encoded_string:
                    # Decode the Base64 string
                    decoded_string = decode_base64(encoded_string)
                    
                    if decoded_string:
                        
                        # Parse the decoded string to find the pattern
                        word, times = parse_decoded_string(decoded_string)
                        print(word, times)
                        
                        if word and times:
                            # Write to file
                            write_to_file(word, times)
                            
                            # Input the answer into the program
                            answer = word * times
                            process.stdin.write(answer + '\n')
                            process.stdin.flush()
                        else:
                            print("Pattern 'xxx * 69' not found in the decoded string.")
                    else:
                        print("Failed to decode Base64 string.")
            else:
                # Print any other output
                print(f"Other output: {output}")
                
    except KeyboardInterrupt:
        print("\nProgram stopped.")
    except Exception as e:
        print(f"Error running .exe: {e}")

if __name__ == "__main__":
    run_exe_and_parse()
