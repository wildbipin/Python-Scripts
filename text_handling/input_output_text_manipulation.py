# import re
# import os
# import fileinput


# input_text = open(r'C:\Users\bipin_akgrhq9\Documents\Cloud DevOps Stuff\Python\text_handling\input_text.txt','r')
# # print(file_text.readlines())


# module_name_version = []
# output_lines = []


# for line in input_text:
#     line = line.strip()
#     if 'pypi' in line:
#         line_parts = line.split()
#         if len(line_parts) >= 3:
#             module_name = line_parts[0]
#             module_version = line_parts[1]
#             module_name_version.append(f"{module_name}={module_version}")


# output_text = open(r'C:\Users\bipin_akgrhq9\Documents\Cloud DevOps Stuff\Python\text_handling\output_text.txt','w')

# for line in output_lines:
#     output_text.write(line + '\n')
# output_text.write(line + '\n')
# for module_version in module_name_version:
#     output_text.write(module_version + '\n')







def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    output_lines = []
    module_versions = []

    for line in lines:
        line = line.strip() #remove any whitespaces
        output_lines.append(line)
        if 'pypi' in line:
            parts = line.split()
            if len(parts) >= 3:
                module_name = parts[0]
                version = parts[1]
                module_versions.append(f"{module_name}={version}")

    with open(output_file, 'w') as file:
        for line in output_lines:
            file.write(line + '\n')
        file.write('\n')
        for module_version in module_versions:
            file.write(module_version + '\n')

if __name__ == "__main__":
    input_file = r'C:\Users\bipin_akgrhq9\Documents\Cloud DevOps Stuff\Python\text_handling\input_text.txt'
    output_file = r'C:\Users\bipin_akgrhq9\Documents\Cloud DevOps Stuff\Python\text_handling\output_text.txt'
    process_file(input_file, output_file)
