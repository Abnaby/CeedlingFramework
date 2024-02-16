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


def update_yaml_with_paths(yaml_file, unitTest_PathFile,src_PathFile):
    # Load the YAML file with comments and document markers
    yaml = ruamel.yaml.YAML()
    with open(yaml_file, 'r') as file:
        data = yaml.load(file)

    # Load the unit test paths
    unit_test_paths = []
    unit_src_paths = []
    with open(unitTest_PathFile, 'r') as file:
        for line in file:
            unit_test_paths.append(line.strip())
    with open(src_PathFile, 'r') as file:
        for line in file:
            unit_src_paths.append(line.strip())       

    # Update the YAML data with the unit test paths
    if ':paths' in data and ':test' in data[':paths']:
        data[':paths'][':test'] += unit_test_paths
    else:
        data[':paths'] = {':test': unit_test_paths}
    
    # Update the YAML data with the src file paths
    if ':paths' in data and ':source' in data[':paths']:
        data[':paths'][':source'] += unit_src_paths
    else:
        data[':paths'] = {':source': unit_src_paths}
    

    # Write the updated YAML back to the file while preserving comments and markers
    with open(yaml_file, 'w') as file:
        yaml.dump(data, file)
        
if __name__ == '__main__':
    txtFileIsExist = checkFileExistance(FILE_NAME_UNIT_TST)
    ymlFileIsExist = checkFileExistance(FILE_NAME_YML)
    if (txtFileIsExist == 1 and ymlFileIsExist == 1):
        update_yaml_with_paths(FILE_NAME_YML, FILE_NAME_UNIT_TST,"src_file_paths.txt")
