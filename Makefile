#################### USER SPECIFIC #########################
# The name of the project
PROJ_NAME = 

# Project source path (absolute or relative to this Makefile) - used by ceedling for testing
PROJ_DIR := 

# List of modules to exclude from testing
EXCLUDED_MODULES := 

# List of unit test suufix e.g. unit_test unit-test 
UNIT_TEST_POSS_SUFFIXES := 

#################### PROGRAM SPECIFIC #########################
PWD := $(shell pwd)
LAST_FOLDER := $(shell basename "$(PWD)")
SRC_FILES := $(wildcard test/*.c)
$(foreach suffix,$(UNIT_TEST_POSS_SUFFIXES),$(eval SRC_FILES += $(wildcard $(PROJ_DIR)/**/$(suffix)/test_*.c)))
MAKE = mingw32-make.exe
#################### PROGRAM  #########################
.PHONY: run_all_except_task_scheduler
test: run_all_except_task_scheduler
	$(MAKE) EndSchema



coverage :
	@ceedling gcov:all
	@ceedling utils:gcov
	

create_project: init 
	@cd $(PROJ_NAME);\
	python findSourceFiles.py "$(PROJ_DIR)";\
	python editYml.py ;\
	rm -f *.py;\
	rm -f *.txt;
	
init: startSchema # Main project Creation 
	@ceedling new ${PROJ_NAME} ; \
	cp -f Makefile ${PROJ_NAME} ; \
	cp -f *.py ${PROJ_NAME} ; \
	cd ${PROJ_NAME}; \
	python $(CURDIR)/yml.py ;\
	rm -f yml.py;


create_modules:
	@read -p "Enter modules name: " MODULE_NAME; \
    MODULE_NAME=$$(echo $$MODULE_NAME | tr -d ' '); \
    echo "Creating $$MODULE_NAME ***********"; \
    ceedling module:create[$$MODULE_NAME];

remove_project:
	@read -p "Enter project name: " PROJ_NAME; \
	echo "Removing $$PROJ_NAME ***********"; \
	if [ "$$PROJ_NAME" = "${PROJ_NAME}" ]; then \
		if [ "$$PROJ_NAME" = "$(LAST_FOLDER)" ]; then \
			cd ..; \
			rm -rf $$PROJ_NAME; \
			echo "Folder $$PROJ_NAME Content removed"; \
		else \
			rm -rf $$PROJ_NAME; \
			echo "Folder $$PROJ_NAME removed"; \
		fi; \
	else \
		echo "Project name entered does not exist in same directory"; \
	fi
clean-test: # core is for core dumps!
	ceedling clean
	clear


# Define a target to run all tests except specified modules
run_all_except_task_scheduler:
	@echo "Running tests for all modules except $(EXCLUDED_MODULES):";
	@for file in $(SRC_FILES); do \
		module=$$(basename $$file .c); \
		echo "*********************************** Testing $$module ****************************************"; \
		exclude=0; \
		for excluded_module in $(EXCLUDED_MODULES); do \
			if [ $$module = "$$excluded_module" ]; then \
				exclude=1; \
				break; \
			fi; \
		done; \
		if [ $$exclude -eq 0 ]; then \
			echo "Running $$module"; \
			ceedling test:$$module; \
		else \
			echo "Skipping $$module"; \
		fi; \
	done


		


startSchema:
	@echo "****************** START_SCHEMA ******************"

EndSchema:
	@echo "****************** EndSchema ******************"