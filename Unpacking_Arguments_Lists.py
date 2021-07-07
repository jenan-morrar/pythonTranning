args = [0, 1, 4, 9]

def unpacking_Argument_List(a,b,c,d):
    print("a = "+ str(a))
    print("b = " + str(b))
    print("c = " + str(c))
    print("d = " + str(d))

def packing_Arguments_List(*data):
    newList = list(data)
    newList[1]= "Asal"
    print(newList)

unpacking_Argument_List(*args)
packing_Arguments_List("Hello","World")

n = int(input())
output=""
if 1 <= n <= 150:
    for i in range(1, n+1):
        output += str(i)
print(output)

