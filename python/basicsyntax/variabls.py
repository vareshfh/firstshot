# a=10
# print(type(a),a)
# b=2.54
# print(type(b),b)
# c='salam'
# print(type(c),c)
# d="10dsf"
# print(type(d),d)
# f=["10dsf"]
# print(type(f),f)
# g=('1' , "hgh",'2' , "ihi",[1,2,25])
# g[4].insert(3,2555)
# print(type(g),g)
# h={1:"jjhk",'ali':'ahmadi'}
# print(type(h),h)
# h["gf"] = 3565
# print(h.get("gf"))
# h.update({"gf":6})
# print(h)
l = [1,2,3,3,2,5,6,5,6,4,2]
print(type(l),l)
s = set(l)
print(type(s),s)
s.remove(2)
print(type(s),s)
s.update([0,4,7])
print(type(s),s)
s=s.union([1,9,"h"])
print(type(s),s)