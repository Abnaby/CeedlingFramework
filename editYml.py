"""
Filename: editYml.py
Author: Mohamed Abd El-Naby
Date created:  14-02-2024
Last modified: 18-02-2024
Python Version: V1.0
Description: This script has two missions
    1- update the yml file with extracted paths from findSourceFiles.py script in file unit_test_paths.txt and src_paths.txt 
    2- create configuration file for gcov in file gcovr.cfg to generate coverage HTML. 
"""

import yaml
import ruamel.yaml
import os

################################### PROGRAM VAR : DON'T EDIT ANYTHING BELOW THIS LINE #########################

FILE_NAME_UNIT_TST = "unit_test_paths.txt"
FILE_NAME_YML = "project.yml"
CONFIG_FILE_NAME = "gcovr.cfg"
COVERAGE_FILE_OUTPUT = "html/"


################################### PROGRAM FUNC : DON'T EDIT ANYTHING BELOW THIS LINE #########################
def checkFileExistance(FileName):
    if not os.path.exists(FileName):
        print("File does not exist.")
        return 0
    return 1


def update_yaml_with_paths(yaml_file, unitTest_PathFile, src_PathFile):
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


def makeConfigFile(unitTest_PathFile, src_PathFile, CONFIG_FILE_NAME_param):
    # Load the unit test paths
    unit_test_paths = []
    unit_src_paths = []
    with open(unitTest_PathFile, 'r') as file:
        for line in file:
            unit_test_paths.append(line.strip())
    with open(src_PathFile, 'r') as file:
        for line in file:
            unit_src_paths.append(line.strip())
    with open(CONFIG_FILE_NAME_param, 'w') as file:
        # exlucded modules in gcovr.cfg file
        file.write("# exlucded modules in gcovr.cfg file \n")
        for path in unit_test_paths:
            file.write("exclude = ")
            file.write(path)
            file.write("\n")
        # Add source folder
        file.write("filter = ")
        file.write("src/")
        file.write("\n")
        for path in unit_src_paths:
            file.write("filter = ")
            file.write(path)
            file.write("\n")
        # html-details = yes  # info about each source file
        # output = html/coverage.html
        file.write("html-details = yes  # info about each source file\n")
        file.write("output = ")
        file.write(COVERAGE_FILE_OUTPUT)
        if COVERAGE_FILE_OUTPUT[-1] == '/':
            file.write("coverage.html")            
        else:
            file.write("/coverage.html")
        file.write("\n")

if __name__ == '__main__':
    txtFileIsExist = checkFileExistance(FILE_NAME_UNIT_TST)
    ymlFileIsExist = checkFileExistance(FILE_NAME_YML)
    if (txtFileIsExist == 1 and ymlFileIsExist == 1):
        update_yaml_with_paths(
            FILE_NAME_YML, FILE_NAME_UNIT_TST, "src_file_paths.txt")
        makeConfigFile(FILE_NAME_UNIT_TST, "src_file_paths.txt", CONFIG_FILE_NAME)
