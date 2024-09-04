
.SILENT:

default:
	python3 -m unittest test.test_parking_lot
	dotnet run --project src/ParkingLot.csproj

python:
	python3 -m unittest test.test_parking_lot

csharp:
	dotnet run --project src/ParkingLot.csproj

coverage:
	pip -q install coverage
	coverage run -m unittest test.test_parking_lot
	coverage report -m --omit=*__init__.py,test_*.py
