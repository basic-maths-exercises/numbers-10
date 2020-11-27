import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_isInNaturals(self) :
        for i in range(20) :
            a, b = np.random.randint(0,20), np.random.randint(0,20) 
            if a-b>0 : self.assertTrue( isInNaturals(a, b)==1, "Your function is not working" )
            else : self.assertTrue( isInNaturals(a, b)==0, "Your function is not working" )
