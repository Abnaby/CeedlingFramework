<<<<<<< HEAD
"# Ceedling_UnitTest" 


## Getting Started
First make sure Ruby is installed on you system 
``` 
ruby --version 
ruby 2.7.8p225 (2023-03-30 revision 1f4d455848) [x64-mingw32]
```
If not Installed follow [embetronicx](https://embetronicx.com/tutorials/unit_testing/unit-testing-in-c-part-3-ceedling-installation/) to install framework.

Second Run Command 
```
git clone https://github.com/Abnaby/Ceedling_UnitTest.git
```
you will find this file hierarchy, you can delete all of them expect `makefile`, `findSourceFiles.py` and `yml.py`
=======
# Automate Unit Test Process based on Ceedling Framwork  
## Getting Started
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
git clone https://github.com/Abnaby/CeedlingFramework.git
```
you will find this file hierarchy, you can delete all of them expect `makefile`and `*.py` files.
>>>>>>> 1cc6d87 (Automate Unit Test Process V0.1 - Under Development -)
```
Ceedling_UnitTest/
├── img/
├── makefile
├── findSourceFiles.py
<<<<<<< HEAD
└── yml.py
```

## Tunnable Parameters"
=======
├── editYml.py
└── yml.py
```

## Tunnable Parameters
>>>>>>> 1cc6d87 (Automate Unit Test Process V0.1 - Under Development -)
to specify the project name add it in makefile variable: 
```makefile 
    PROJ_NAME = 
```
If the project source file exist in another directory you can add it in 
```
    PROJ_DIR :=  
```
## Creating A Project
in the same directory name `Ceedling_UnitTest` run shell then write 
```
    make create_project && cd PROJ_NAME
```
Output 
```
Welcome to Ceedling!
    create  PROJ_NAME/project.yml
Project 'PROJ_NAME' created!
 - Execute 'ceedling help' from PROJ_NAME to view available test & build tasks
Project PROJ_NAME created
```

## Creating A New Module From Scratch 
to make a new module from scratch:
* Makesure you are in `PROJ_NAME` dir, run `pwd` cmd
```
    make create_modules 
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
│   ├── makefile
├── makefile
└── yml.py
```

## Execlude Module From Testing process 
If I need to execlude the module from testing process e.g. `test_b` add it in `makefile`
```
EXCLUDED_MODULES := test_b
```
## Remove The full Project
<<<<<<< HEAD
makesure you are at  `Ceedling_UnitTest` run cmd 
```
    mingw32-make.exe remove_project
=======
makesure you are at  `Ceedling_UnitTest`
```
    make remove_project
>>>>>>> 1cc6d87 (Automate Unit Test Process V0.1 - Under Development -)
```
you will be asked to enter the `PROJ_NAME`
```
    Enter project name: `PROJ_NAME`
```
Output 
```
Removing UART_BOOTLOADER ***********
Folder UART_BOOTLOADER removed
```
if you got error 
```
rm: cannot remove 'PROJ_NAME': Device or resource busy
Folder `PROJ_NAME` Content removed
```
The folder content was deleted but you are inside the `PROJ_NAME` in terminal
```
    cd .. 
<<<<<<< HEAD
    mingw32-make.exe remove_project
=======
    make remove_project
>>>>>>> 1cc6d87 (Automate Unit Test Process V0.1 - Under Development -)
```