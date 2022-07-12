x = 1

def indetemter (a: str):

    global x
    x = a
    print(a)
indetemter("Word")
print(x)

x = None
def concat(a: str, b: str):
    return a + b

res_1 = concat("qwe", "rty")

print(res_1)

