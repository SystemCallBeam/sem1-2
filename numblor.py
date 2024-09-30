import random

def create_mapping_table(main_str, sub_str):
    # Create a list of numbers [0-9] and beyond
    numbers = list(range(10))
    random.shuffle(numbers)

    # Split the shuffled numbers into two arrays of size 5
    arr1 = numbers[:5]
    arr2 = numbers[5:]

    # Main number map using the main string (first 10 characters)
    main_mapping = {i: char for i, char in enumerate(main_str)}

    # Sub number map using the sub string (for numbers beyond 10)
    sub_mapping = {i+10: char for i, char in enumerate(sub_str)}
    
    # Function to map the number to the character if in range, else keep the number
    def map_num_to_char(num):
        if num in main_mapping:
            return main_mapping[num]
        elif num in sub_mapping:
            return sub_mapping[num]
        return num

    # Print the formatted array (with space after each number or character)
    def format_array(arr):
        return '[{}]'.format(', '.join(f'{x:>2}' for x in arr))

    # Print the table (5x5) with both original and mapped values
    def print_table(arr1, arr2):
        # Print original number table
        print('   ' + format_array(arr2))
        for i, num1 in enumerate(arr1):
            row = [num1 + num2 for num2 in arr2]
            print(f'{num1:2} {format_array(row)}')

        print("\nMapped Character Table:")
        print('   ' + format_array([map_num_to_char(x) for x in arr2]))
        for i, num1 in enumerate(arr1):
            row = [map_num_to_char(num1 + num2) for num2 in arr2]
            print(f'{map_num_to_char(num1)} {format_array(row)}')

    # Display the original numbers and the mapped table
    print("Original Number Table:")
    print_table(arr1, arr2)

# Example input strings for main and sub mapping
main_str = "1h4t3cOLoR"  # 10 characters for numbers 1-10
sub_str = "jiNgv5"         # 4 characters for numbers 11-14
create_mapping_table(main_str, sub_str)
