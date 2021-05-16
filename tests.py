import unittest
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
import random



integer_list = list(range(1000)) 
random.shuffle(integer_list) 
 
#sorted list for tests 
sorted_list = integer_list
sorted_list.sort()

class Test_sort(unittest.TestCase):

    """Test for insertion sort""" 
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(integer_list), sorted_list, "Test insertion sort")

    """Test for bubble sort""" 
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(integer_list), sorted_list, "Test bubble sort")


if __name__ == "__main__": 

    unittest.main()