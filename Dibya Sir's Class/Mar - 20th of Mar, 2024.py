# Python Sets

# Sets are represented by {}
# Sets are mutable
# Sets can not contain duplicate elements

myset = {'Upa', 'Sagar'}
print("First Print:", myset)

myset.add('Tamang')
print("Second Print:", myset)

myset.remove('Sagar')
print("Third Print:", myset)

myset2 = {'School', 'University', 'Upa'}
print("Set2:", myset2)

union = myset.union(myset2)
print("union:", union)

intersect = myset.intersection(myset2)
print("intersect:", intersect)

# The difference between Set & List is that List can contain duplicates 
# but a Set can not contain duplicates

mylist= ['Upa', 'Sagar', 'Upa']
newset = set(mylist)
print("Set from list: ", newset)

# Python Regular Expressions

# Python comes with a built-in "re"
# match() & search() function in re
# match() only searches at the beginning of the string
# search() only searches at at the entire string
# re.sub() is usesd to search and replace a string based on a regular expression
import re

pattern = r'apple'
text = "I am having my apple & a banana."

print(re.match(pattern, text))
print(re.search(pattern, text))

text2 = re.sub(pattern, 'oranage', text)
print(text2)


































