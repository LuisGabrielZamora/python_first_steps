from typing import List

names: List[str] = ['Juan', 'Karla', 'Ricardo', 'Maria']

# Print names with range
print(f'{names[0:2]}')

# Print names list
for name in names:
    print(f'{name}')

# Add new value to list
names.append('Lorenzo')
print(names)

# Insert in a specific index
names.insert(1, 'Octavio')
print(names)

# Get total values for the list
print(f'Total de la lista: {len(names)}')

# Delete last value if is not necesary
names.append('Otro')
print(names)
names.pop()
print(names)

# Clear list
names.clear()
print(names)

# Delete list in memory
del names