countries = ['Canada', 'US', 'Japan']
print('origin',countries)
# append() Adds an element at the end of the list
countries.append('China')
print(countries,">> append('China')")
# copy() Returns a copy of the list
countries_new = countries.copy()
print(countries_new, ">> copy()")
# count() Returns the number of elements with the specified value
print(countries.count('US'), ">> count('US')")
# extend() Add the elements of a list (or any iterable), to the end of the current list
countries.extend(['India', 'Mexico'])
print(countries, ">> extend(['India', 'Mexico'])")
# index() Returns the index of the first element with the specified value
print(countries.index('China'), ">> index('China')")
# insert() Adds an element at the specified position
countries.insert(3,'Iraq')
print(countries, ">> insert(3, 'Iraq')")
# pop() Removes the element at the specified position
countries.pop(2)
print(countries, ">> pop(3)")
# remove() Removes the item with the specified value
countries.remove('Mexico')
print(countries, ">> remove('Mexico')")
# reverse() Reverses the order of the list
countries.reverse()
print(countries, ">> reverse()")
# sort() Sorts the list
countries.sort()
print(countries,">> sort()")
# clear() Removes all the elements from the list
countries.clear()
print(countries,'>> clear()')

