import os
import sys
import yaml
################################### ENABLE_DEBUG_SEC #########################
DEBUG_ENB = True
################################### END OF DEBUG SEC #########################

# Parent directory path
if DEBUG_ENB == True:
    parent_dir = 'G:/COURSES/UnitTest/Ceedling/proj/'
else:
    parent_dir = ''


# List to store found .c files
found_files = []

################################### PROGRAM VAR : DON'T EDIT ANYTHING BELOW THIS LINE #########################

OUTPUT_FILE = 'output.txt'
UNIT_TEST_DIR_PATHS_FILE_NAME = 'unit_test_paths.txt'
SRC_FILE_DIR_PATHS_FILE_NAME = 'src_file_paths.txt'

UNIT_TEST_PATHS = []
SRC_FILE_PATHS = []

UNIT_TEST_DIR_WORD = {"unit_test", "unit_tests", "unit-test", "unit-tests"}


def isUnitTestDir(param_path):
    for word in UNIT_TEST_DIR_WORD:
        if word in param_path:
            return True
    return False


def fillUnitTestPaths(param_foundFiles):
    # Extract directory paths and add to UNIT_TEST_PATHS if it's a unit test directory
    for path in param_foundFiles:
        # Extract directory path
        dir_path = '/'.join(path.split('/')[:-1]) + '/'
        if isUnitTestDir(dir_path):
            UNIT_TEST_PATHS.append(dir_path)
        else:
            SRC_FILE_PATHS.append(dir_path)


"""
Recursively search for .c files within the parent directory
"""


def extractPathsFromDir(copy_parentDir):
    # Recursively search for .c files within the parent directory
    for root, dirs, files in os.walk(copy_parentDir):
        for file in files:
            if file.endswith('.c'):  # Check if the file has a .c extension
                # Append the absolute path of the .c file to the list
                found_files.append(os.path.join(root, file))
    return 0


"""
This function takes a list of file paths and replaces backslashes with forward slashes in each path.
"""


def editPath(param_originalPath):
    for i in range(len(param_originalPath)):
        param_originalPath[i] = param_originalPath[i].replace('\\', '/')


def remove_leading_hyphen(found_files):
    for i in range(len(found_files)):
        # Remove leading '-' character
        # print("found_files[i] = " + found_files[i])
        if found_files[i].startswith('-'):
            found_files[i] = found_files[i][1:].strip()


# Example usage:
remove_leading_hyphen('unit_test_paths.txt')

##########################################  ERROR VAR #######################################################
NO_ERROR = 0
INVALID_PATH = 1
NoFilesFound = 2
##########################################  MAIN #############################################################
if __name__ == '__main__':
    if DEBUG_ENB == False:
        parent_dir = sys.argv[1]
        if len(parent_dir) == 0:
            print(INVALID_PATH)
            sys.exit(1)
    parent_dir = parent_dir.replace('\\', '/')
    extractPathsFromDir(parent_dir)
    editPath(found_files)
    if not found_files:
        print(NoFilesFound)
    else:
        fillUnitTestPaths(found_files)
        # Write the list of found .c files to a YAML file
        # with open(OUTPUT_FILE, 'w') as txt_file:
        #     yaml.dump(found_files, txt_file)
        # with open(UNIT_TEST_DIR_PATHS_FILE_NAME, 'w') as txt_file:
        #     yaml.dump(UNIT_TEST_PATHS, txt_file)
        # with open(SRC_FILE_DIR_PATHS_FILE_NAME, 'w') as txt_file:
        #     yaml.dump(SRC_FILE_PATHS, txt_file)
        with open(OUTPUT_FILE, 'w') as fp:
            for item in found_files:
                # write each item on a new line
                fp.write("%s\n" % item)
        with open(UNIT_TEST_DIR_PATHS_FILE_NAME, 'w') as fp:
            for item in UNIT_TEST_PATHS:
                # write each item on a new line
                fp.write("%s\n" % item)
        with open(SRC_FILE_DIR_PATHS_FILE_NAME, 'w') as fp:
            for item in SRC_FILE_PATHS:
                # write each item on a new line
                fp.write("%s\n" % item)
        print(NO_ERROR)
