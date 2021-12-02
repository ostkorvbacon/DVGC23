modprobe virtualcan
python main.py
python3 -m coverage run -m unittest 
python3 -m coverage report
python3 -m coverage html