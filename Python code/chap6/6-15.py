def scope():
    global var1
    var1=1
    print("函数内部打印结果")
    print(var1,var2)

var1=10
var2=20
scope()
print("函数外部打印结果")
print(var1,var2)
