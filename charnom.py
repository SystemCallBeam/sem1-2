import subprocess
import base64

def decode_base64(encoded_message):
    return base64.b64decode(encoded_message).decode('utf-8')

def extract_calculation(decoded_message):
    parts = decoded_message.split()
    for i, part in enumerate(parts):
        if part == "is" and i+1 < len(parts) and i+3 < len(parts):
            return parts[i+1], int(parts[i+3])
    return None, None

def perform_calculation(text, multiplier):
    return text * multiplier

def run_exe(input_data):
    # Replace 'your_program.exe' with the actual name of your executable
    process = subprocess.Popen(['your_programshanomkaimook.exe'], 
                               stdin=subprocess.PIPE, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE,
                               text=True)
    stdout, stderr = process.communicate(input=input_data)
    return stdout.strip()

def main():
    with open("output.txt", "w") as output_file:
        while True:
            encoded_message = input("Enter the encoded message (or 'quit' to exit): ")
            if encoded_message.lower() == 'quit':
                break
            
            decoded = decode_base64(encoded_message)
            text, multiplier = extract_calculation(decoded)
            
            if text and multiplier:
                calculated = perform_calculation(text, multiplier)
                result = run_exe(calculated)
                print(f"Result: {result}")
                output_file.write(f"{result}\n")
            else:
                print("Invalid input")

if __name__ == "__main__":
    main()