# Exercise a
a = 1
b = 2
c = 5

while a < c:
 a = a + 1
 b = b + c
 print(a,b,c)


# Exercise b 
d = 4
e = 6
f = 7

while d > f:
  d = d + 1
  e = e - 1
  print(d, e, f)

# Exercise c
g = 4
h = 6

while g < h:
  g = g + 1
  print(g,h)


# Exercise d
j = 2
k = 5
n = 9

while j < k:
  m = 6
  while m < n:
    print('Goodbye')
    m = m + 1
  j = j + 1


# Exercise e # Since python is procedural, this resets the values initialized in d
j = 2
k = 5
m = 6
n = 9

while j < k:
  while m < n:
    print('Hello')
    m = m + 1
  j = j + 1


#Exercise f
p = 2
q = 4
while p < q:
  print('Adios')
  r = 1
  while r < q:
    print('Adios')
    r = r + 1
  p = p + 1
