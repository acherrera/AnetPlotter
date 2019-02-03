import unittest
from helpers.processing import (process_start, process_normal,
        lower_head, data_tracker)


class TestHelpers(unittest.TestCase):

    def test_process_start(self):

        fake_data = [
            ";MESH:CJX.jpg",
            "G0 F3600 X127.398 Y131.434 Z0.3",
            ]

        tracker = data_tracker(fake_data)
        tracker.index = 1
        process_start(tracker)

        self.assertEqual(tracker.BETTER_START_CODE[0], tracker.new_code[0])
        code_correct = bool("G0 Z0.3" in tracker.new_code[-1])
        self.assertTrue(code_correct)


    def test_process_normal(self):

        fake_data = [
            "G1 X126.148 Y132.046 E0.05638",
            "G0 F3600 X126.148 Y131.741",
            "G1 F3000 X126.356 Y131.437 E0.07126"
            ]
        tracker = data_tracker(fake_data)
        tracker.index = 1
        process_normal(tracker)

        self.assertEqual(tracker.new_code[0:3], tracker.RAISE_COMMANDS)
        code_correct = bool(tracker.current_move() in tracker.new_code[-1])
        self.assertTrue(code_correct)


    def test_lower_head(self):

        fake_data = [
            "G1 X126.148 Y132.046 E0.05638",
            "G0 F3600 X126.148 Y131.741",
            "G1 F3000 X126.356 Y131.437 E0.07126"
            ]

        tracker = data_tracker(fake_data)
        tracker.index = 2
        tracker.head_raised = True
        lower_head(tracker)

        self.assertFalse(tracker.head_raised)
        self.assertEqual(tracker.new_code[0:3], tracker.LOWER_COMMANDS)
        code_correct = bool(tracker.current_move() in tracker.new_code[-1])
        self.assertTrue(code_correct)



if __name__ == "__main__":
    unittest.main(failfast=True)
