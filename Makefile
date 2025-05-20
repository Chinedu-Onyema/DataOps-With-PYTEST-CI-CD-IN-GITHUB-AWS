# THIS FILE WILL KEEP ALL THE COMPLEX COMMANDS I WILL USE.
# IT IS LIKE A COOK BOOK GUIDE.

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=auction --cov=transform_auction
	python -m pytest -vv test_auction.py
	python -m pytest -vv test_transform_auction.py

lint:
	pylint --disable=R,C auction.py

format:
	black *.py

all: install lint test format