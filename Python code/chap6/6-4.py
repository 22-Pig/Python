from math import sqrt

def dis(x1,y1,x2,y2): #求平 面上两点距离
    print("x1={},y1={},x2={},y2={}".format(x1,y1,x2,y2)) 
    return sqrt((x1-x2)**2+(y1-y2)**2)

print(dis(1,3,y2=5,x2=4))
