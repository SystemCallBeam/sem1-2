import os

# Define the path without additional quotes
path = "C:\\Users\\tkhae\\Desktop\\New folder\\90DAY"  # or your path

files_content = []

# Use os.walk to traverse directories and subdirectories
for root, dirs, files in os.walk(path):
    for filename in filter(lambda p: p.endswith(".txt"), files):
        filepath = os.path.join(root, filename)
        with open(filepath, mode='r', encoding='utf-8') as f:  # Use 'utf-8' encoding to read text files
            files_content.append(f.read())

# At this point, files_content contains the contents of all .txt files
# You can print or process the contents as needed
for content in files_content:
    print(content)
