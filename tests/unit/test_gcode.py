"""
    Tests the code editing program to ensure it is working as intended
"""


import unittest
from convert_script_master import (strip_coords, get_distance)



class TestGCODE(unittest.TestCase):

    
    def test_strip_x_y(self):
        # Test that X and Y are removed successfully
        input_data = "G1 X129.096 Y131.938 E0.19141"

        
        self.assertFalse(True)

    def test_distance_measurement(self):
        # Test to make sure the distance measurements are working as expected

        self.assertFalse(True)

    def test_travel_replaced(self):
        # Test the simple case where G0 command is replaced with lift and move

        self.assertFalse(True)


    def test_complex_travel_case(self):
        # Test the case where travel-short_move-travel
        # G0 X0111 Y0111
        # G1 X0112 Y0112
        # G0 X0113 Y0113

        self.assertFalse(True)



if __name__ == "__main__":
    unittest.main(failfast=True)
