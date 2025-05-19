a = 3 
b = 4.5
c = "hello"
d = {"hello" , 3,4,5,5,5}
e = ("hello",5,5,5,6,6)
f = ["hello",5,5,5,6,6]
g = True 
h = range(5)

print(a,type(a),id(a))
print(b,type(b),id(b))
print(c,type(c),id(c))
print(d,type(d),id(d))
print(e,type(e),id(e))
print(f,type(f),id(f))
print(g,type(g),id(g))
print(h,type(h),id(h))
print(d)
d.update([10,11])
print(d)
f[3]= "hi"
print(f)
