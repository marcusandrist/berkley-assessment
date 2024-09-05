
.SILENT:

default:
	python3 -m unittest test.test_parking_lot
	dotnet test -v=1 test

coverage:
	pip -q install coverage
	coverage run -m unittest test.test_parking_lot
	coverage report -m --omit=*__init__.py,test_*.py
	dotnet test -v=1 test
