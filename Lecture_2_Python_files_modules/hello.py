# #def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return


def new_string(symbol, count):    
    return symbol * count    


возможность передачи любого кол-ва арг-w в функции, поетому пред описанием '*' - *params

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w'))