import textwrap

def wrap(string, max_width):
    wrapped_text = ""
    for i in range(0, len(string), max_width):
        wrapped_text += string[i:i+max_width] + "\n"
    return wrapped_text

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


#     def wrap(string, max_width):
#     """
#     Wraps the given string into lines with a maximum width.
    
#     Args:
#     string (str): The input string to wrap.
#     max_width (int): The maximum width of each line.
    
#     Returns:
#     str: The wrapped text.
#     """
#     wrapped_text = ""  # Initialize an empty string to store the wrapped text
#     i = 0  # Initialize the starting index
    
#     # Loop through the string in chunks of max_width
#     while i < len(string):
#         # Get the substring from the current index up to max_width characters
#         line = string[i:i+max_width]
#         # Add the substring and a newline character to the wrapped text
#         wrapped_text += line + "\n"
#         # Move the starting index forward by max_width
#         i += max_width
    
#     return wrapped_text

# if __name__ == '__main__':
#     string = input("Enter the string: ")
#     max_width = int(input("Enter the maximum width: "))
    
#     result = wrap(string, max_width)
#     print(result)