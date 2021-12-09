modprobe virtualcan
python3 -m coverage run -m unittest
python3 -m coverage report
mkdir html_report
python3 -m coverage html -d html_report
