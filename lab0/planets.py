""" 
Author: Daniel Jones
Date: 4/7/2020
CSC 202
Lab 0
"""

def weight_on_planets():
   # Gather input
   weightOnEarth = input("What do you weigh on earth? \n")
   # Single cast to integer
   weightOnEarth = int(weightOnEarth)
   # Converstions
   weightOnMars = weightOnEarth * 0.38
   weightOnJupiter = weightOnEarth * 2.34
   # Single print() for output
   print("On Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds." % (weightOnMars, weightOnJupiter))


if __name__ == '__main__':
   weight_on_planets()