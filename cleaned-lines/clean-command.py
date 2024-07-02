import re

# Read the input file
with open(r'C:\Users\bipin_akgrhq9\Documents\Cloud DevOps Stuff\Python-Scripts\cleaned-lines\command_history.txt', 'r') as file:
    lines = file.readlines()

# Remove numbering
cleaned_lines = [re.sub(r'^\s*\d+\s+', '', line) for line in lines]

# Write the cleaned lines to a new file
with open(r'C:\Users\bipin_akgrhq9\Documents\Cloud DevOps Stuff\Python-Scripts\cleaned-lines\cleaned_command_history.txt', 'w') as file:
    file.writelines(cleaned_lines)

print("Command history cleaned and saved to 'cleaned_command_history.txt'")
