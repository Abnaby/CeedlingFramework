# Automate Unit Test Process based on Ceedling Framwork  

## Getting Started
---

First make sure Ruby and python is installed on you system 
``` 
λ ruby --version 
ruby 2.7.8p225 (2023-03-30 revision 1f4d455848) [x64-mingw32]
```
``` 
λ python --version
Python 3.10.4
```
If not Installed follow [embetronicx](https://embetronicx.com/tutorials/unit_testing/unit-testing-in-c-part-3-ceedling-installation/) to install framework and [python.org](https://www.python.org/) for python.

Second Run Command 
```
λ git clone https://github.com/Abnaby/CeedlingFramework.git
```
you will find this file hierarchy, you can delete all of them expect `makefile`, `*.py`, and`.cfg`   files.
```
Ceedling_UnitTest/
├── img/
├── makefile
├── findSourceFiles.py
├── editYml.py
├── gcovr.cfg
└── yml.py
```
## Tunnable Makefile Parameters
---
to specify the project name add it in makefile variable: 
```makefile 
    PROJ_NAME = MY_PROJ
```
If the project source file exist in another directory you can add it in 
```
    PROJ_DIR :=  
```
modules to be excuted from testing process `Can redefine it later in makfile inside PROJ_NAME`
```
    EXCLUDED_MODULES :=
```
to List of unit test suufix e.g. unit_test unit-test 
```
UNIT_TEST_POSS_SUFFIXES := unit_test unit-test
```
to add a Coverage output path e.g. add an `html` folder in the same directory of project creation.
```
COVERAGE_OUTPUT_PATH := html
```
to add make program name
```
MAKE = mingw32-make.exe
```
## Creating A Project
---
in the same directory name `Ceedling_UnitTest` run shell then write 
```
λ make create_project && cd PROJ_NAME
```
Output 
```
*******************************************************
*            PROJECT NAME : MY_PROJ
*            START TIME   : 12 : 43: 04
*******************************************************
Welcome to Ceedling!
      create  v1_Project/project.yml

Project 'v1_Project' created!
 - Execute 'ceedling help' from v1_Project to view available test & build tasks

                EVERYTHING GENERATED
```

## Creating A New Module From Scratch 
---
to make a new module from scratch:
* Makesure you are in `PROJ_NAME` dir, run `pwd` cmd
```
λ make create_modules 
```
You will be asked to enter the module names with `,` as separator for example
```
Enter modules name: a,b,c
```
Output will be 
```
    Creating a,b,c ***********
    File src/a.c created
    File src/a.h created
    File test/test_a.c created
    Generate Complete
    File src/b.c created
    File src/b.h created
    File test/test_b.c created
    Generate Complete
    File src/c.c created
    File src/c.h created
    File test/test_c.c created
    Generate Complete
```
and the output hierarchy will be in 
```
Ceedling_UnitTest/
├── img/
├── PROJ_NAME
│   ├── src/
│   │   ├── a.c
│   │   ├── a.h
│   │   ├── b.c
│   │   ├── b.c
│   │   ├── c.c
│   │   └── c.c
│   ├── test/
│   │   ├── test_a.c
│   │   ├── test_b.c
│   │   └── test_c.c
│   ├── gcovr.cfg
├── makefile
├── findSourceFiles.py
├── editYml.py
├── gcovr.cfg
└── yml.py
```

## Execlude Module From Testing process 
---
If I need to execlude the module from testing process e.g. `test_b` add it in `makefile`
> Make sure the edits happen in `makefile` inside the PROJ_NAMEs
```
EXCLUDED_MODULES := test_b
```
## Remove The full Project
---
```
 λ make remove_project
```
you will be asked to enter the `PROJ_NAME`
```
    Enter project name: `PROJ_NAME`
```
Output 
```
Removing PROJ_NAME ***********
Folder PROJ_NAME removed
```
if you got error 
```
rm: cannot remove 'PROJ_NAME': Device or resource busy
Folder `PROJ_NAME` Content removed
```
The folder content was deleted but you are inside the `PROJ_NAME` in terminal
```
    cd .. 
    mingw32-make.exe remove_project
```

## Run Unit Tests 
---
Just 
```
    make test
```

## Run Coverage 
---
Just 
```
    make coverage
```

## Known issues
---
- The Project creation where `make create_project` and main `SourceFiles` project `must be in the same directory`
```
    G:/
    ├── Ceedling_UnitTest/
    │  ├── PROJ_NAME
    │  ├── makefile
    │  ├── *.py
    │  ├── project.yml
    │  └── *.cfg
    └── SourceFiles
```
## Contributing  
Bug reports, feature requests, and so on are always welcome. Feel free to leave a note in the Issues section.
