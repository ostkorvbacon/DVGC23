pep8 --first tests/
pep8 --first main.py
python3 main.py
python3 -m coverage run -m unittest
python3 -m coverage report
python3 -m coverage html