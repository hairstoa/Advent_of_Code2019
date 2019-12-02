#----------------------------------------------------------
#  Title:       Santa's Fuel Calcator
#  Programmer:  Adriane
#  Date:        December 1, 2019
#  Notes:       This file requires a text file companion.
#               Text file contains integers seperated by \n. 
#  
#  Description: Fuel is needed for the Santa's space ship to
#  travel. This program calculates the total fuel needed 
#  based on the distance to the modules and the mass of the 
#  fuel being carried. 
#---------------------------------------------------------- 
             
def main():
    #Read ints into a list
    star_distances = read_distances("AoC_1_SantaStars.txt")

    total_fuel = 0
    # Calculate total fuel for each distance to a star
    for distance in star_distances:
        total_fuel += calculate_fuel(distance)
    print("The total fuel needed is: " + str(total_fuel))

#----------------------------------------------------------
#                    calculate_fuel
#  This function calulates the total fuel needed for one
#  module by recursion. The modules passed is divided by
#  3, rounded down, minus two until the result is <= 0.
#  Then the returned calls are summed.  
#
#  Citation: This code was adpated from:
#  Simeon Visser, "Recursive function to calculate Sum?",
#  stackoverflow.com/questions/19966290/
#
#  receives:    int(value)
#  returns:     int (value)
#----------------------------------------------------------
def calculate_fuel(modules):
    modules = (modules // 3) - 2
    if modules <=  0:
       return 0
    else:
        return(modules + calculate_fuel(modules))

#----------------------------------------------------------
#                   read_distances
#  Is passed a string containing the name of a file. A
#  list is created with each element being a line from the
#  file converted into an integer type. 
#   Precondition: the file contains a list of integers 
#   seperated by \n. 
#
#  Citation: This code was adpated from:
#  Konrad Rudolph, "Reading ints line from a file in Python",
#  codereview.stackexchange.com/questions/12443
#
#  receives:    string 
#  returns:     list
#----------------------------------------------------------
def read_distances(filename):
    with open(filename) as f:
        return [int(x) for x in f]

if __name__ == "__main__":
    main()





