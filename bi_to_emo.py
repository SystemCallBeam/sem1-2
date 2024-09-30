def binary_to_emoji(binary_string):
    """Convert 8-bit binary string to an emoji by using Unicode points."""
    decimal_value = int(binary_string, 2)  # Convert binary to decimal
    base_emoji_code_point = 0x1F600  # Starting point of emoji range (😀 = U+1F600)
    
    # Add decimal value to the base emoji code point
    emoji_code_point = base_emoji_code_point + (decimal_value % 80)  # Stay within a reasonable emoji range
    return chr(emoji_code_point)

# Example binary strings
binary_strings = ["01000001", "01100101", "00110001", "00000000"]

# Convert each binary string to an emoji
for binary_string in binary_strings:
    emoji_result = binary_to_emoji(binary_string)
    print(f"Binary: {binary_string} -> Emoji: {emoji_result}")
