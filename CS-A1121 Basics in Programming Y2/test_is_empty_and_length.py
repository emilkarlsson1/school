import unittest

from linked_list import LinkedListException, LinkedList, Empty, Cell


class TestIsEmptyAndLength(unittest.TestCase):
    """Taydenna tahan testit is_empty- ja length-metodeille"""
    def test_is_empty1(self):
        self.assertTrue(Empty.is_empty(Empty()), "Not Empty")

    def test_is_empty2(self):
        self.assertFalse(Cell.is_empty(Cell("asd", Empty())), "Not empty")

    def test_length1(self):

        self.assertEqual(Empty.length(Empty()), 0)

    def test_length2(self):
        empty = Empty()
        cell_1 = Cell('abc', empty)
        cell_2 = Cell(56, cell_1)
        cell_3 = Cell(3, cell_2)
        cell_4 = Cell(6767, cell_3)
        self.assertEqual(Cell.length(cell_4),4)

if __name__ == "__main__":
    unittest.main(verbosity=2)
