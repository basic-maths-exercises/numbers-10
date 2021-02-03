try:
    from AssCheck import funcchecks as fc
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AssCheck"])
    from AssCheck import funcchecks as fc

import unittest
from main import *

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_isInNaturals(self) :
        inputs, outputs = [], [] 
        for i in range(20) :
            a, b = np.random.randint(0,20), np.random.randint(0,20) 
            inputs.append((a,b,))
            if a-b>0 : outputs.append(1) 
            else : ouptuts.append(0) 
        assert( fc.check_func( 'isInNaturals', inputs, outputs ) ) 
