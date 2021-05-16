import random
from insertion_sort import insertion_sort

# list of ints from 1 to 999 which is then shuffled.
integer_list = list(range(1000)) 
random.shuffle(integer_list)

"""main method just to print the output of the sorts""" 
def main(): 
    insertion_sort(integer_list)
    print(integer_list)

if __name__ == "__main__": 
    main()