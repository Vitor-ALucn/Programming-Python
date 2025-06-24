from chempy.util import periodic

n = int(input("Enter number to see the table: "))
print("Atomic No. \tName\t\tSymbol\t\tMass")

for i in range(1, n +1):
    print(i, end="\t\t")
    if len(periodic.names[1]) > 7:
        print(periodic.names[i], end="\t")
    else:
        print(periodic.names[i], end="\t\t")
    print(periodic.symbols[i], end="\t\t")
    print(periodic.relative_atomic_masses[i])

# pip install chempy

# This code generates a periodic table of elements up to the specified atomic number `n`.
# It uses the `chempy` library to access the names, symbols, and relative
# atomic masses of the elements. The output is formatted in a tabular structure
# with columns for atomic number, name, symbol, and mass.
# The user is prompted to enter the number of elements they want to see in the table.
# The `periodic` module from `chempy.util` provides the necessary data for the elements.
# The output is printed in a structured format with appropriate spacing.

#Output:
# Enter number to see the table: 10
# No. 	Name		Symbol		Mass
# 1		Hydrogen	H		    1.00794
# 2		Helium		He		    4.002602
# 3		Lithium		Li		    6.941  
# 4		Beryllium	Be		    9.012182
# 5		Boron		B		    10.811
# 6		Carbon		C		    12.0107
# 7		Nitrogen	N		    14.00674
# 8		Oxygen		O		    15.9994
# 9		Fluorine	F		    18.9984032
# 10	Neon		Ne		    20.1797