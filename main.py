import random


def main(): 

    integer_list = list(range(1000)) 
    shuffle_list = random.shuffle(integer_list) 
    print(integer_list)


if __name__ == "__main__": 
    main()
