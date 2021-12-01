import unittest
from canlib import canlib, Frame

if __name__ == '__main__': # pragma: no cover
    from corrupt import corrupt
    unittest.main()
else:
    from faultfunctions.corrupt import corrupt