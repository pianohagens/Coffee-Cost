# Project:      Redo-Lab 3 (HagensPianoLab03redo.py)
# Name:         Piano Hagens
# Date:         10/11/2016
# Description:  ProgramsA will calculate sales coffee at $10.50/lb + shipping $.86/lb + $1.50 fixed cost. 
#               ProgramsB will calculate how much need to save per month in order to reach $1,125,000 at age 68.           

# ProgramsA will calculate sales coffee at $10.50/lb + shipping $.86/lb + $1.50 fixed cost.
def mainA():
    print("------------- Lab 3 A: Coffee's Cost------------- ")
    print()
    # Display the price, per pound shipping price, and the overhead shipping price.
    print("Konditorei coffee Price perpound: $ 10.50")
    print("Shipping cost for perpound: $ 0.86")
    print("Any overhead shipping cost: $ 1.50")
    print()
    
    # Let users enter a quantity use flt DataType    
    fltQutPound = float(input("Enter coffee weight that you want to purchase: "))

    # Calculate the total = fltQutPound * (10.50 + 0.86) + 1.50
    total = fltQutPound * (10.50 + 0.86) + 1.50
    
    print("---------------------------------")
    # Display the order detail with the total    

    # Display the quantity
    print("You have entered", fltQutPound, "pounds") 

    # Display the total cost with shipping
    print("Here is your order detail:", fltQutPound,"x(10.50+0.86)+1.50=",total,"dollars") 

    # Display the total
    print("Here is your order detail: ",total,"dollars")

# Call mainA function
mainA()

