# def chap(name):
#     for i,ch in enumerate(name):
#         print(i,ch)
#     return len(name)
# print(chap("fateme"))

# def power(base,expon):
#     print(base**expon)
# power(expon=10,base=2)

# def mutliply(, *args):
#     sumproduct = 1
#     sum = 0
#     for i in args:
#         sum+=i
#         sumproduct*=i
#     return sum,sumproduct,sum,sumproduct,sum,sumproduct
# sum, sumproduct , *args = mutliply(5,4,2,9,6)
# print("sum=",sum)
# print("sumproduct=",sumproduct)
# print("args=",args)

def showst (**kwargs):
    for key,value in kwargs.items():
        print(key," = ",value)
st = {
    "name":"fateme",
    "family":"hedaiat",
}
print(st)
showst(name="behzad",family="bayat",position="teacher")