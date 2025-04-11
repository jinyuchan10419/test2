def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y
x, y = map(int, input("x y 형태로 입력하세요: ").split())
print("x =", x)
print("y =", y)

print(multiply(x,y))
print(divide(x,y))