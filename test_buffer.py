import unittest
from buffer import Buffer

class TestBuffer(unittest.TestCase):
    """
    Unit test suite for Buffer class.
    """

    def test_initialization(self):
        """
        Test Buffer initialization with and without an iterable.
        """
        # Test initialization with an iterable
        buffer = Buffer(3, [1, 2, 3])
        self.assertEqual(len(buffer), 3  )# Buffer should contain 2 elements
        self.assertEqual(buffer.capacity, 3)  # Capacity should be 3
        self.assertEqual(repr(buffer), '1 2 3')  # String representation should match

        # Test initialization without an iterable
        buffer = Buffer(3)
        self.assertEqual(len(buffer), 0)  # Buffer should be empty
        self.assertEqual(buffer.capacity, 3)  # Capacity should be 3
        self.assertEqual(repr(buffer), '')  # String representation should be empty

    def test_initialization_with_over_capacity_iterable(self):
        """
        Test Buffer initialization with an iterable that exceeds capacity.
        """
        with self.assertRaises(ValueError):
            Buffer(3, [1, 2, 3, 4])  # Should raise ValueError

    def test_add_item(self):
        """
        Test adding items to the Buffer and discarding the oldest item when capacity is exceeded.
        """
        buffer = Buffer(3)
        buffer.add(1)
        self.assertEqual(repr(buffer), '1')  # Buffer should contain '1'
        buffer.add(2)
        self.assertEqual(repr(buffer), '1 2')  # Buffer should contain '1 2'
        buffer.add(3)
        self.assertEqual(repr(buffer), '1 2 3')  # Buffer should contain '1 2 3'
        buffer.add(4)
        self.assertEqual(repr(buffer), '2 3 4')  # Buffer should discard oldest item and contain '2 3 4'

    def test_add_invalid_item(self):
        """
        Test adding invalid items to the Buffer.
        """
        buffer = Buffer(3)
        with self.assertRaises(TypeError):
            buffer.add("a")  # Should raise TypeError for non-int/float

    def test_get_item(self):
        """
        Test accessing items in the Buffer using positive and negative indexing.
        """
        buffer = Buffer(3, [1, 2, 3])
        self.assertEqual(buffer[0], 1)  # First item should be 1
        self.assertEqual(buffer[1], 2)  # Second item should be 2
        self.assertEqual(buffer[2], 3)  # Third item should be 3
        self.assertEqual(buffer[-1], 3)  # Last item should be 3
        self.assertEqual(buffer[-3], 1)  # First item should be 1 using negative index

    def test_get_item_out_of_range(self):
        """
        Test accessing an item in an empty Buffer.
        """
        buffer = Buffer(3)
        with self.assertRaises(IndexError):
            _ = buffer[0]  # Should raise IndexError for empty buffer

    def test_str_and_repr(self):
        """
        Test string representations of the Buffer.
        """
        buffer = Buffer(3, [1, 2, 3])
        self.assertEqual(repr(buffer), '1 2 3')  # __repr__ method should match

if __name__ == '__main__':
    unittest.main()
