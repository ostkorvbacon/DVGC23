import unittest
from canlib import canlib, Frame
from faultfunctions import faultfunction

if __name__ == '__main__': # pragma: no cover
    from faultfunctions import faultfunction
    unittest.main()
else:
    from faultfunctions.faultfunction import corrupt

