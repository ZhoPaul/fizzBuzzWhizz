
import sys,os
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
import unittest
from project.predication import Times

class TestPredication(unittest.TestCase):
    def test_times(self):
        times3 = Times(3)
        self.assertTrue(times3.predicate(6))
        self.assertFalse(times3.predicate(5))


if __name__ == '__main__':
    unittest.main()