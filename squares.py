#for import the file of  functions
from functions import square

for i in range(10):
    print(f"The Square {i} equal {square(i)}")

print("\n")

#we can import with another way like 

import functions 

for i in range(10):
    print(f"The Square {i} equal {functions.square(i)}")