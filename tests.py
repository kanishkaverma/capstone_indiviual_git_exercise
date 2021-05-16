import unittest
from insertion_sort import insertion_sort
import random



integer_list = list(range(1000)) 
random.shuffle(integer_list) 
sorted_list = integer_list
#sorted list for tests 
sorted_list.sort()

class Test_sort(unittest.TestCase):

    """Test for insertion sort""" 
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(integer_list), sorted_list, "Test insertion sort")


if __name__ == "__main__": 

    unittest.main()