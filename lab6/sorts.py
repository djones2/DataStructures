import random
import time

def selection_sort(list):
    comparisons = 0
    min_index = 0
    while min_index < len(list) - 1:
        start_comp = min_index + 1
        while start_comp < len(list):
            comparisons += 1
            if list[start_comp] < list[min_index]:
                temp = list[start_comp]
                list[start_comp] = list[min_index]
                list[min_index] = temp
            start_comp += 1
        min_index += 1
    return comparisons
    
def insertion_sort(list):
    comparisons = 0
    for i in range(1, len(list)): 
        key = list[i] 
        j = i-1
        while j >=0 and key < list[j]: 
            list[j+1] = list[j] 
            j -= 1
            comparisons += 1
        comparisons += 1
        list[j+1] = key 
    return comparisons
   

""" def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(10) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(100000), 1000)
    #print(randoms)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    print(comps)
    stop_time = time.time()
    print(comps, stop_time - start_time) 

if __name__ == '__main__': 
    main()"""