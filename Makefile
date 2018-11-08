init:
	pip3 install -r requirements.txt --user

test:
	python3 -m unittest discover . "*_test.py"

.PHONY: init test