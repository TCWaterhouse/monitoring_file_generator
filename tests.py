import unittest

from setups import(
    get_setups
)

class TestSetups(unittest.TestCase):
    def test_get_setups(self):
        setup_path = "test/240509 OP MONS.txt"
        self.assertEqual(
            [{'station': '900', 'date': '09.05.24', 'time': '22:32:13'},
            {'station': '880', 'date': '09.05.24', 'time': '22:53:31'},
            {'station': '467', 'date': '09.05.24', 'time': '23:24:24'}],
            get_setups(setup_path)
        )

if __name__ == "__main__":
    unittest.main()