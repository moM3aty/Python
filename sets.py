# Create An Empty Set
s = set()

# Add to the set 

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) #It 's  not add because we have one element equal 3 before
print (s)
print(f"The set has {len(s)} Elements")

s.remove(2)
print(s)
print(f"The set has {len(s)} Elements")