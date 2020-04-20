names = ['John Doe', 'Jim Harpper', 'Kate Jackson', 'Joe Thompson', 'Bow Jonsson']


first_element = names[0]
third_of = names[0:3]

last_element = names[-3:-1]

all_elements = names[:]  # copy of names
all_elements2 = names[0:len(names)]

even_names = names[::-1]
reverse_list = names[::-1]

names[4:]

last_three = names[-3:]

names = ['John Doe', 'Jim Harpper', 'Kate Jackson', 'Joe Thompson', 'Bow Jonsson']

reverse_list = []
len_names = len(names) - 1

for name in names:
    item = names[len_names]
    reverse_list.append(item)
    len_names -= 1  # len_names = len_names - 1

index = len(names) - 1
rev_list2 = []
while index >= 0:
    rev_list2.append(names[index])
    index -= 1



names = ['John Doe', 'Jim Harpper', 'Kate Jackson', 'Joe Thompson', 'Bow Jonsson']

# who = input('Enter a name to search: ')
who = 'Jim Harpper'


for name in names:
    if name == who:
        # print('found')
        break
else: # no break
    # print('not found')
    pass

found = True
for name in names:
    if name == who:
        found = True
        break
    else:
        found = False

if found == True:
    # print('Found')
    pass
else:
    # print('Not Found')
    pass

names = ['John Doe', 'Jim Harpper', 'Kate Jackson', 'Joe Thompson', 'Bow Jonsson']

names.append('Ivan Jemmes')


names.insert(0, 'Saeid Gholami')


o_number = 0
for name in names:
    for char in name:
        if char == 'o':
            o_number += 1

n = 0
for name in names:
    n += name.count('o')

print(n)