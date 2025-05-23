# THIS FILE WILL KEEP ALL THE COMPLEX COMMANDS I WILL USE.
# IT IS LIKE A COOK BOOK GUIDE.


# install the all the libraries used for this project from the requirements.txt file
install: 
	pip install --upgrade pip &&\
	pip install -r requirements.txt


# Test all the .py files to make sure that they are reusable and work before production
test:   
	python -m pytest -vv --cov=auction --cov=transform_auction
	python -m pytest -vv test_auction.py
	python -m pytest -vv test_transform_auction.py

# Give potential warnings about the logic/code structure in other to prevent future issues in production
lint:
	pylint --disable=R,C *.py || true
# pylint --disable=R,C *.py || true  --- Use the '|| true' fuction to avoid warning errors from make --

# Remove white spaces and other indentation or bad logic/code structure by formating all the .py files
format:
	black *.py

# Automatically run all the functions at once together.
all: install lint test format