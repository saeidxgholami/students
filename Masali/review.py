### Variables
age = 10
f = 3.9
s = 'Hello World'

# get types of a var
type(age)  # int


# collections: list, tuple, dict, string
names = ['joe', 'jack', 'jim']
days_of_the_week = ('sun', 'mon', 'tue')
person = {'name': 'John Doe', 'phone': '2234234', 'country': 'uk'}

# --------------------------
### string operations(methods)
s.upper()  # HELLO WORLD
s.lower()  # hello world
s.title()  # Helllo World
s[0]  # H
s[-1] # d
s[4:7]  # o W

s1 = 'jim'
s2 = 'johnson'
# str contactenation
fullname = s1 + ' ' + s2   # jim johnson

'-' * 10
# --------------------------
### List operations (methos)
names[0] # joe
i = names.index('jack')  # 1
names[2] = 'kate'
names.append('Marry')
names.remove('joe')
names.sort()

# --------------------------
### Tuples
days_of_the_week[0]

# --------------------------
### Dict
person['name']  # John Doe
person.get('name')  # John Doe ; if key not found return None
person.keys() # (name, phone, country)
person.values()  
person['children'] = ['kate', 'joe', 'john', 'billy']
person['wife_name'] = 'Marry Doe'

# Control Flow
# if, while, for

my_age = 30
if my_age >= 18:
	print('vote')
else:
	print('you cannot vote')

x = 1

if x > 0:
	print('positive')
elif x < 0:
	print('negative')
else:
	print('zero')


while x < 10:
	# print('hello')
	x = x + 1



t = 0
for ch in 'Message':
	t = t + 1

for item in ['joe', 'jim', 'billy']:
	print(item)

### Function
def add(x, y):
	return x + y

def sub(x, y):
	return  x - y


r = add(2, 3) + sub(2, 3)

### Buil-in Function

print()
input()
sorted()
len()
max()
min()
sum()

print('hello')

