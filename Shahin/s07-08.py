# 5/5/2020


name_with_j = []
name_with_j2 = 0
names = ['Joe', 'John', 'Kate', 'Marry', 'Jemmes']

names[0]
names[-1]
names[1:3]
len(names)

for name in names:
	if name[0] == 'J' and 'o' in name:
		name_with_j.append(name)

# print(name_with_j)

name_with_j2 = [ name for name in names if name[0] == 'J' and 'o' in name ]
# print(name_with_j2)

# print([ name for name in names if name[0] == 'J' and 'o' in name ])

# for name in names: 
# 	if name == 'John': 
# 		print('hello')

[name for name in names if name[0] == 'J' and 'o' in name ]

# print ([a+b for a in 'mug' for b in 'lid' if b == 'l' ])
# x = []
# for a in 'mug':
# 	for b in 'lid':
# 		if b == 'l':
# 			x.append(a+b)

# print(x)


x = 10

# if x > 0:
# 	print('postive')
# elif x == 0:
# 	print('zero')
# else:
# 	print('negative')

# # a, i, u, o, e
# counter = 0
# total = 0
# names = ['John', 'Jim', 'Kate']
# for name in names:
# 	counter = 0
# 	for ch in name: 
# 		if ch == 'a':
# 			counter += 1
# 		elif ch == 'e':
# 			counter += 1
# 		elif ch == 'i':
# 			counter += 1
# 		elif ch == 'o':
# 			counter += 1
# 		elif ch == 'u':
# 			counter += 1
# 	# print(name, '-->', counter)
# 	total += counter

# print('Total Vowels', total)

# # a, i, u, o, e
# counter = 0
# total = 0
# names = ['John', 'Jim', 'Kate']
# for name in names:
# 	counter = 0
# 	for ch in name:
# 		if ('a' in ch) or ('e' in ch) or ('i' in ch) or ('o' in ch) or ('u' in ch):
# 			counter += 1
		
	# print(name, counter)

	

# # a, i, u, o, e
# counter = 0
# total = 0
# names = ['John', 'Jim', 'Kate']
# for name in names:
# 	counter = 0
# 	for ch in name:
# 		if ch in 'aioue':
# 			counter += 1
# 	print(name, counter)

# a, i, u, o, e
# counter = 0
# total = 0
# names = ['John', 'Jim', 'Kate']
# for name in names:
# 	counter += name.count('o')
# 	counter += name.count('i')
# 	counter += name.count('e')
# 	counter += name.count('u')
# 	counter += name.count('a')
# 	print(name, counter)
# 	counter = 0

# c = 0
# names = ['John', 'Jim', 'Kate']
# s = ''.join(names)
# c += s.count('a') 
# c += s.count('i')
# c += s.count('e')
# c += s.count('o')
# c += s.count('u')

# print('aioue', c)


names = ['John', 'Jim', 'Kate']
t = 0
for name in names:
	for ch in name:
		if ch in 'aioue':
			t += 1

print('aioue', t)


