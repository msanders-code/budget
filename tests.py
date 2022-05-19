import unittest
import main_prog
from re import compile


class TestMainFunctions(unittest.TestCase):

    def test_date_format(self):
        pattern = compile(r"\d\d/\d\d/\d\d\d\d")
        self.assertTrue(pattern.match(main_prog.get_date()))


if __name__ == "__main__":
    unittest.main()
