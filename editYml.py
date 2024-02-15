import yaml
import ruamel.yaml
import os

FILE_NAME_UNIT_TST = "unit_test_paths.txt"
FILE_NAME_YML = "project.yml"


def checkFileExistance(FileName):
    if not os.path.exists(FileName):
        print("File does not exist.")
        return 0
    return 1


def editFile(txtFileName, ymlFileName):
    with open(ymlFileName, 'r') as source:
        in_section = False
        section_name = ""
        extracted_lines = []
        for line in source:
            # If line starts a new section
            if line.strip().startswith(":"):
                section_name = line.strip()
                in_section = True
                extracted_lines.append(line)
                print(f"Section: {section_name}")
                if ":load_paths" in section_name:
                    print("key is :loaannnnnnnnnnnnnnnnnnnnd_paths")
                    break
            # If line contains a key-value pair
            elif in_section:
                # Remove comments from the line
                line = line.split("#")[0].strip()
                # Handle anchor references
                if "*" in line:
                    line = line.replace("*", "&")
                # Load the line as YAML data
                data = yaml.safe_load(line)
                # If the line represents a dictionary
                if isinstance(data, dict):
                    # Print the key-value pairs
                    for key, value in data.items():
                        print(f"Key: {key}, Value: {value}")
                        extracted_lines.append(line)
            # If line is empty or contains only comments, it indicates the end of the section
            if line.strip() == "" or line.strip().startswith("#"):
                in_section = False
        # Write extracted lines to the new YAML file
    with open("new_file.yml", 'w') as destination:
        for line in extracted_lines:
            destination.write(line)

    return 0

def update_yaml_with_paths(yaml_file, paths_file):
    # Load the YAML file with comments and document markers
    yaml = ruamel.yaml.YAML()
    with open(yaml_file, 'r') as file:
        data = yaml.load(file)

    # Load the unit test paths
    unit_test_paths = []
    with open(paths_file, 'r') as file:
        for line in file:
            unit_test_paths.append(line.strip())

    # Update the YAML data with the unit test paths
    if ':paths' in data and ':test' in data[':paths']:
        data[':paths'][':test'] += unit_test_paths
    else:
        data[':paths'] = {':test': unit_test_paths}

    # Write the updated YAML back to the file while preserving comments and markers
    with open(yaml_file, 'w') as file:
        yaml.dump(data, file)
        
if __name__ == '__main__':
    txtFileIsExist = checkFileExistance(FILE_NAME_UNIT_TST)
    ymlFileIsExist = checkFileExistance(FILE_NAME_YML)
    if (txtFileIsExist == 1 and ymlFileIsExist == 1):
        update_yaml_with_paths('project.yml', 'unit_test_paths.txt')
        # editFile(FILE_NAME_UNIT_TST, FILE_NAME_YML)
        f = open(FILE_NAME_UNIT_TST, "r")
        # with open('project.yml', 'r') as file:
        #     data = yaml.safe_load(file)
        # print(data)
        # # for x in f:
        # #     print(x)
