# # # # pow=[x for x in range(1,11)]
# # # # # print(pow)
# # # # def sum(a,b):
# # # #     c=a*b
# # # #     print(c)

# # # # sum(5,3)
# # # # def factorial(n):
# # # #     n=(int(input='enter'))
# # # #     if n==1:
# # # #      return 1
# # # #     else:
# # # #        return(n*factorial(n-1))

# # # # print('factorial is',factorial(6))
# # # a=(input=(int))
# # a=lambda a,b,c:print(a+b+c)
# # a(2,2,2)
# cube= lambda x:(x**3)
# print(cube(3))
nums=[1,2,3,4,5]
def square(n):
    return (n*n)

result=list(map(square,nums))
print((result))