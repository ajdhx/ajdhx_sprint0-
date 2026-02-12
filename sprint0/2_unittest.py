import operator
import unittest


class TestOperator(unittest.TestCase):

    def test_adding(self):
        self.assertEqual(operator.add(1, 2), 3)

    def test_subtracting(self):
        self.assertEqual(operator.sub(3, 2), 1)


if __name__ == '__main__':
    unittest.main()

# Changes made:
# - Renamed class 'testOperator' to 'TestOperator' (CamelCase for classes).
# - Reordered imports.
# - Removed extra blank lines within class.
# - Added spaces around operators.