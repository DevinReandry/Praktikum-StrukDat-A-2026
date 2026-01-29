x = 8   #integer
y = 5.8 #float
z = 4j  #complex
print(type(x))
print(type(y))
print(type(z))

#int
x = 27890
y = 3565627269769696976987711
z = -30000000000

print(type(x))
print(type(y))
print(type(z))

#float
x = 1.8
y = 356562.11
z = -325.7895522

print(type(x))
print(type(y))
print(type(z))

#float angka yang sangat besar
x = 17e4
y = 356562E22554887711
z = -3255.5e22

print(type(x))
print(type(y))
print(type(z))

#complex
x = 7+9j
y = 3j
z = -32j

print(type(x))
print(type(y))
print(type(z))


#ubah tipe data
x = 67
y = 2.9
z = 3j


a = float(x)

b = int(y)

c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#angka random
import random
print(random.renrange(2, 100))