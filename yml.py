# Define the target string to search for
target_string = "- module_generator"
plugin_string = ":plugins"

# Define the string to add after the target string
new_line = "    - gcov\n"

# Read the content of the project.yml file
with open("project.yml", "r") as f:
    lines = f.readlines()

# Find the index of the target string
index = None
for i, line in enumerate(lines):
    if target_string in line:
        index = i
        break

# If the target string is found, add the new line after it
if index is not None:
    lines.insert(index + 1, new_line)

# Write the modified content back to the file
with open("project.yml", "w") as f:
    f.writelines(lines)
