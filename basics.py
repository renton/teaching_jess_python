# ****** basics ******

# variable declaration
x = 100     # int
y = 100.0   # float
z = 'butts' # string

# printing to screen
print(x)

# string concatenation
print('lotsa ' + z)

# type casting
print(x + int(y))
print(z + str(y))

# the arithmetic operators you'd expect
a = 1 + 2 * 3 / 4 - 5 ** 2

# python has no brackets. only whitespace!
# if conditions
if (z == 'butts'):
    print 'ITS TRUE'
else:
    print 'ITS FALSE'

# comparison operators you would expect
if (z != 'buttz'):
    print 'z does not equal buttz'

if (x > 1):
    print 'x is greater than 1'

if (x >= 100):
    print 'x is greater than or equal to 100'

# bitwise operator 'and'
if (x == 100 and z == 'butts'):
    print 'everything is right in the universe'

# bitwise operator 'or'
if (x == 9999 or z == 'butts'):
    print 'at least we still have butts'

# ****** python built-in data types (lists, dictionaries, tuples) are VERY powerful ******

# === a list is like an array (it can hold ints, strings, variables, objects etc.) ===
e = [1, 3, 5, 'a', 'b', x]

# looping through an iterable object like an array is easy
for element in e:
    print element

# lists can be accessed by position value
print e[2]          # will print 5
print len(e)        # number of elements in e is 6
e[3] = 'BUTT'       # changing value at 3rd positon of e
e.append('ME TOO')  # adding a new element to end of array
e.sort()            # sorting array

# lots, lots more of standard array operations! splitting, removing, searching etc.

# === dictionaries are associated arrays with unique key=>value pairs ===
f = { 
        'a': 100,
        'b': 'blue',
        'c': x
    }

# access by key not position
print f['b']
f['b'] = 'orange'

# looping through a dict
for key,value in f.items():
    print key, value

# check if a key is set
if 'd' in f:
    print 'd is in f'
else:
    print 'd is not in f'

# === tuples are for ordered items that don't change ===
rgb = (255, 240, 229)

print rgb[1]

# this won't work. can't change tuples
#rgb[1] = 'aa'

# can split tuple up
i, j, k = rgb

print k
