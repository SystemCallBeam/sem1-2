def emoji_to_bit(emoji_string):
    # Define the mapping of emojis to bits
    emoji_bit_map = {
        '😺': '1',
        '😸': '0',
        ' ': ' '
    }
    
    # Convert the emoji string to a list of bits
    bit_string = ''.join(emoji_bit_map[emoji] for emoji in emoji_string if emoji in emoji_bit_map)
    
    return bit_string

# Example usage
emoji_string = "😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😸😺😸😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😺😺😺😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😺😺😸😺😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😸😺😸😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😸😺😸😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😸😸😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😸😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😺😺😸😸😺😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😸😺😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😸😸😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😺😸😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😸😺😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😺😺😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😺😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😺😸😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😸😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😸😺😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😸😺😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😸😺😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😸😺😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😸😺😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😸😺😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😺😸😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😺😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😺😸😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😸😸😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😸😸😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😸😺😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😺😸😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😸😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😺😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😸😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😸😺😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😺😸😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😸😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😺😸😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😸😸😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😸 😺😸😺😸😺😺😺😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😸😸😺 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😸😺😺😸😺😸 😺😺😺😺😸😸😸😸 😺😸😸😺😺😺😺😺 😺😸😸😺😸😸😸😺 😺😸😺😺😸😺😸😸"  # You can replace this with any emoji sequence
bits = emoji_to_bit(emoji_string)  #.replace(" ", "") Remove spaces for simplicity

# Display the result
# print(f"Emoji sequence: {emoji_string}")
print(f"Bit sequence: {bits}")
