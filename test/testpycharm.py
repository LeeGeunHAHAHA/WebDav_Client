print("hello world")
a,b,c = map(int, input().split())
print (a,b,c)
dict = {"a":a,"b":b,"c":c}
def test(f,a,b,c):
    return f(a,2)+f(b,2)+f(c,2)
print(test(pow,**dict))
