def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError
   """
   # Raise ValueError if list is None type.
   if int_list == None:
      raise ValueError
   # If list is empty, return None.
   elif len(int_list) == 0:
      return None
   # Find max value of list, iteratively.
   else:
      max = 0
      for temp in int_list:
         if temp > max:
            max = temp
      return max


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   # Base case. Empty list. Accounts for final recursion.
   if not int_list:
      return int_list
   else:
      return int_list[-1:] + reverse_rec(int_list[:-1])
   

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if not int_list:
      raise ValueError
   middle_idx = (high + low) // 2
   middle = int_list[middle_idx]
   if middle == target:
      return middle_idx
   elif middle_idx == 0 or low == high - 1: 
      if int_list[high] == target:
         return high
      else:
         return None
   elif middle < target:
      return bin_search(target, middle_idx, high, int_list)
   elif middle > target:
      return bin_search(target, low, middle_idx, int_list)

      