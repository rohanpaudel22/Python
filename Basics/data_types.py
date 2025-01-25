"""
Text type: str
Numeric type: int , float , complex
Sequence types: list , tuple , range
Mapping type: list , tuple , range
Set types: set , frozenset
Boolean Type : bool
Binary types: bytes , bytearray , memoryview
None types : NoneType

"""
# Setting the Data types
"""

a = "Hello World"	#str	
b = 20	#int	
c= 20.5	#float	
d = 1j	#complex	
e = ["apple", "banana", "cherry"]	#List
f = ("apple", "banana", "cherry") #Tuple
g = range(6)	#range	
h = {"name" : "John", "age" : 36}	#dict	
i = {"apple", "banana", "cherry"}	#set	
j = frozenset({"apple", "banana", "cherry"})	#frozenset	
k = True	#bool	
l = b"Hello"	#bytes	
m = bytearray(5)	#bytearray	
n = memoryview(bytes(5))	#memoryview	
o = None	#NoneType

print(a , type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))
print(j, type(j))
print(k, type(k))
print(l, type(l))
print(m, type(m))
print(n, type(n))
print(o, type(o))

"""

# Setting the Specific Data type

a = str("Hello World")	
b = int(20)	
c= float(20.5)		
d = complex(1j)	
e = list(("apple", "banana", "cherry"))
f = tuple(("apple", "banana", "cherry"))
g = range(6)
h = dict(name="John", age= 36)	
i = set(("apple", "banana", "cherry"))		
j = frozenset(("apple", "banana", "cherry"))
k = bool(5)	
l = bytes(5)	
m = bytearray(5)	
n = memoryview(bytes(5))	

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)