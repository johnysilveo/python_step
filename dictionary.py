my_dict = {'a': 1, 'b': 2}                              # Create a dictionary with two pairs

print("print(my_dict['a'])                             # Get value by key (raises error if not found)")
print(my_dict['a'])                                    # Get value by key (raises error if not found)

print("print(my_dict.get('c', 0))                      # Safely get value or return 0 if key missing")
print(my_dict.get('c', 0))                             # Safely get value or return 0 if key missing

print("my_dict['c'] = 3                                 # Add or update key 'c' with value 3")
my_dict['c'] = 3                                        # Add or update key 'c' with value 3

print("del my_dict['b']                                 # Delete key 'b' from dictionary")
del my_dict['b']                                        # Delete key 'b' from dictionary

print("print(my_dict.pop('x', 'not found'))            # Remove key 'x' or return fallback value")
print(my_dict.pop('x', 'not found'))                   # Remove key 'x' or return fallback value

print("print(my_dict.popitem())                        # Remove and return the last item")
print(my_dict.popitem())                               # Remove and return the last item

print("print('a' in my_dict)                           # Check if key 'a' exists in dictionary")
print('a' in my_dict)                                  # Check if key 'a' exists in dictionary

print("print(len(my_dict))                             # Get number of key-value pairs")
print(len(my_dict))                                    # Get number of key-value pairs

print("my_dict.clear()                                  # Clear all key-value pairs")
my_dict.clear()                                        # Clear all key-value pairs

print("new_dict = my_dict.copy()                        # Copy the dictionary")
new_dict = my_dict.copy()                              # Copy the dictionary

print("my_dict.update({'x': 10, 'y': 20})              # Merge another dictionary")
my_dict.update({'x': 10, 'y': 20})                     # Merge another dictionary

print("pairs = [('name', 'Bob'), ('age', 30)]          # List of key-value tuples")
pairs = [('name', 'Bob'), ('age', 30)]                 # List of key-value tuples

print("person = dict(pairs)                            # Create dictionary from tuples")
person = dict(pairs)                                   # Create dictionary from tuples

print("keys = ['a', 'b']                                # List of keys")
keys = ['a', 'b']                                       # List of keys

print("values = [1, 2]                                  # List of values")
values = [1, 2]                                         # List of values

print("zipped = dict(zip(keys, values))               # Create dict from zipped keys and values")
zipped = dict(zip(keys, values))                       # Create dict from zipped keys and values

print("print(my_dict.keys())                           # View all keys")
print(my_dict.keys())                                  # View all keys

print("print(my_dict.values())                         # View all values")
print(my_dict.values())                                # View all values

print("print(my_dict.items())                          # View all key-value pairs")
print(my_dict.items())                                 # View all key-value pairs

print("for key, value in my_dict.items():              # Loop through key-value pairs")
for key, value in my_dict.items():                     # Loop through key-value pairs
    print(f"{key} = {value}")                          # Print key and value

print("for key in my_dict:                             # Loop through keys only")
for key in my_dict:                                    # Loop through keys only
    print(key)                                         # Print key

print("for value in my_dict.values():                  # Loop through values only")
for value in my_dict.values():                         # Loop through values only
    print(value)                                       # Print value

print("for key in sorted(my_dict.keys()):              # Loop through sorted keys")
for key in sorted(my_dict.keys()):                     # Loop through sorted keys
    print(f"{key}: {my_dict[key]}")                    # Print key and value

print("squares = {x: x*x for x in range(5)}            # Dictionary comprehension")
squares = {x: x*x for x in range(5)}                   # Dictionary comprehension
print(squares)                                         # Show result
