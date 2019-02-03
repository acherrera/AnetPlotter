"""
    Tests the code editing program to ensure it is working as intended
"""

import unittest
from convert import convert_main



class TestGCODE(unittest.TestCase):

    def test_main(self):

        simple_sample = [
            "G0 F3600 X127.398 Y131.434 Z0.3",
            ";TYPE:FILL",
            "G1 F1500 E0",
            "G0 F3600 X126.148 Y131.741",
            "G1 F3000 X126.356 Y131.437 E0.07126",
                ]

        return_data = convert_main(simple_sample)

        code_correct = bool('G0 Z0.3' in return_data[2])
        self.assertTrue(code_correct)
        self.assertEqual(simple_sample[-1], return_data[-1])
        code_correct = bool('G90' in return_data[-2])
        self.assertTrue(code_correct)



if __name__ == "__main__":
    unittest.main(failfast=True)
