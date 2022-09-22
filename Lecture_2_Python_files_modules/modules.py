# import hello
# print(hello.f(1))   or

#

# import hello
# print(hello('!', 5))


# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))  # output: asdw

def concatenatio(*params):
    res = 0
    for item in params:
        res +=  item
    return res

print(concatenatio('1', '2', '5', '8'))