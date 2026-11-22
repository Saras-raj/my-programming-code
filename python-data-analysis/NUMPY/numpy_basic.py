import numpy as np
mera_array = np.array([10,20,30,40])
print(mera_array)
x = np.array([1,2,3,4])
print(x)
print(type(x))


#Zero array
ar_zero = np.zeros(4)
ar_zero1=np.zeros((3,4))
print(ar_zero)
print()
print(ar_zero1)
#Ones array
ar_one=np.ones(4)
print(ar_one)
#empty array
ar_em= np.empty(4)
print(ar_em)
#Range array
ar_rn = np.arange(4)
print(ar_rn)
#Diagonal Array
ar_dia = np.eye(3)
print(ar_dia)
#LineSpace
ar_lin = np.linspace(1,10,num=5)
print(ar_lin)

#RANDOM
#Rand()
var = np.random.rand(4)

print(var)

var1 = np.random.rand(2,5)
print(var1)
#Randn()
var2 = np.random.randn(5)
print(var2)
#Ranf()
var3 = np.random.ranf(4)
print(var3)
#Randint
var4 = np.random.randint(5,20,5)
print(var4)

#DATA TYPE



#ARTHEMATIC OPERATION
var = np.array([1,2,3,4])
varadd = var + 3
print(varadd)
var1 = np.array([1,2,3,4,])
var2 = np.array([5,6,7,8])
varadd = var1+var2
print(varadd)

var = np.array([1,2,3,4])
varadd = var - 3
print(varadd)
var = np.array([1,2,3,4])
varadd = var * 3
print(varadd)
var = np.array([1,2,3,4])
varadd = var % 3
print(varadd)
var = np.array([1,2,3,4])
varadd = np.reciprocal(var)
print(varadd)

#2D Array
var21 = np.array([[1,2,3,4] , [1,2,3,4]])
var22 = np.array([[1,2,3,4] , [1,2,3,4]])

print(var21)
print()
print(var22)
print()

varadd2 = var21 + var22
print(varadd2)

var21 = np.array([[1,2,3,4] , [1,2,3,4]])
var22 = np.array([[1,2,3,4] , [1,2,3,4]])

print(var21)
print()
print(var22)
print()

varadd2 = var21 * var22
print(varadd2)
#ARITHMETIC FUNCATION

#Shape
var = np.array([[1,2,3], [1,2,3]])
print(var)
print()
print(var.shape)

var1 = np.array([1,2,3,4], ndmin=4)
print(var1)
print(var1.ndim)
print()
print(var1.shape)
#Reshape
var2 = np.array([1,2,3,4,5,6])
x = var2.reshape(3,2)
print(x)

#Broadcasting Array
var1 = np.array([1,2,3])
print(var1.shape)
print()
print(var1)
print()


var2 = np.array([[1],[2],[3]])
print(var2.shape)
print()
print(var2)
print()
print(var1+var2)

x = np.array([[1],[2]])
print(x.shape)

y = np.array([[1,2,3],[1,2,3]])
print(y.shape)

print(x+y)
#INDEXING
var = np.array([9,8,7,6])
print(var[1])
print(var[-3])
print(var[-1])

var1 = np.array([[9,8,7],[4,5,6]])
print(var1)
print(var1.ndim)
print()

print(var1[0,2]) 

var2 = np.array([[[1,2],[6,7]]])

print(var2)
print(var2.ndim)
print()
print(var2[0,1,1])
#SLICING
var = np.array([9,8,7,6,5,4,3])

print(var)

print()

print("2 to 5 :" ,var[1:5] )
print("2 to End :",var[1:])
print("start to 5 :",var[:5])

print("stop : ",var[::2])

#ITERATION
var = np.array([9,8,7,6,5,4])
print(var)
print()
for i in var : 
    print(i)

#COPY VS VIEW
var = np.array([1,2,3,4]) 
co = var.copy
print("var :",var)
print("copy :",co)

x = np.array([9,8,7,6,5])
vi = x.view()
print("x : ",x)
print("view :",vi)  

x = np.array([9,8,7,6,5])
vi= x.view()
x[1]=40
print("x :",x)
print("view :",vi)

#JOIN ARRAY
var = np.array([1,2,3,4])
var1 =np.array([9,8,7,6])

ar = np.concatenate((var,var1))
print(ar)

vr=np.array([[1,2],[3,4]])
vr1=np.array([[9,8],[7,6]])

ar_new = np.concatenate((vr , vr1),axis=1)
print(vr)
print()
print(vr1)
print()
print(ar_new)


vr=np.array([[1,2],[3,4]])
vr1=np.array([[9,8],[7,6]])

ar_new = np.concatenate((vr , vr1),axis=0)
print(vr)
print()
print(vr1)
print()
print(ar_new)


var_1 = np.array([1,2,3,4])
var_2 = np.array([9,8,7,6])


a_new = np.stack((var_1,var_2),axis = 1)
a_new1= np.hstack((var_1,var_2))  # row
a_new2= np.vstack((var_1,var_2))  #column
a_new3= np.dstack((var_1,var_2))  #height


print(a_new)
print()
print(a_new1)
print()
print(a_new2)
print()
print(a_new3)

#Split Array
var = np.array([1,2,3,4,5,6])

print(var)

ar = np.array_split(var , 3)
print()
print(ar)
print(type(ar))

var1 = np.array([[1,2],[3,4],[5,6]])

print(var1)

ar1 = np.array_split(var1,3)
print()
print(ar1)

#Search
var = np.array([1,2,3,4,2,5,6,5,6,7])
#    index      0,1,2,3,4,5,6,7,8,9
x = np.where(var == 2)
print(x)


#Arithmatic Funcation 
# 1 Shuffle
var = np.array([1,2,3,4,5])
np.random.shuffle(var)
print(var)
# 2 Unique
var1 = np.array([1,2,3,4,5,2,5,2,6,2,7])

x=np.unique(var1,return_index=True,return_counts=True)

print(x)
# 3 Resize
var2 = np.array([1,2,3,4,5,6])

y = np.resize(var2,(2,3))

print(y)

var2 = np.array([1,2,3,4,5,6])

y = np.resize(var2,(3,2))

print(y)

#flatten
var2 = np.array([1,2,3,4,5,6])

y = np.resize(var2,(3,2))
print(y)
print()

print(y.flatten())
# Ravel
var2 = np.array([1,2,3,4,5,6])

y = np.resize(var2,(3,2))
print(y)
print()

print("Flatten : ", y.flatten(order="A"))
print("Ravel : " , np.ravel(y,order="C"))


#Insert
var = np.array([1,2,3,4])
print(var)
v = np.insert(var , 2 , 40)
print(v)

var = np.array([1,2,3,4])
print(var)
v = np.insert(var ,(2,4) , 40)
print(v)

var1 = np .array([[1,2,3] , [1,2,3]])
v1 = np.insert(var1 ,2 ,6,axis=0 )
print(v1)

var1 = np .array([[1,2,3] , [1,2,3]])
v1 = np.insert(var1 ,2 ,[22,23,24],axis=0 )
print(v1)

var1 = np .array([[1,2,3] , [1,2,3]])
v1 = np.insert(var1 ,2 ,6,axis=1 )
print(v1)

var = np.array([1,2,3,4])
print(var)
x = np.append(var,6.5)
print(x)

var1 = np.array([[1,2,3],[1,2,3]])
v1 = np.append(var1,[[44,45,23]],axis=0)
print(v1)

#Delete
var1 = np.array([1,2,3,4])
print(var1)
d = np.delete(var1,2)
print(d)

#Matrix
var = np.matrix([[1,2,3],[1,2,3]])

print(var)
print(type(var))

var1 = np.array([[1,2,3],[1,2,3]])

print(var1)
print(type(var1))

var = np.matrix([[1,2,3],[1,2,3]])
var2 = np.matrix([[1,2,3],[1,2,3]])
print(var)
print(type(var))
print()
print(var+var2)

var = np.matrix([[1,2,3],[1,2,3]])
var2 = np.matrix([[1,2,3],[1,2,3]])
print(var)
print(type(var))
print()
print(var-var2)

#Multiplication
var = np.matrix([[1,2],[1,2]])
var2= np.matrix([[1,2],[1,2]])

print(var)
print(type(var))
print()
print(var*var2)
print()
print(var.dot(var2))

var1 = np.array([[1,2,3],[1,2,3]])

print(var1)
print(type(var1))
print()
print(var1*var1)

#Matrix funcation in numpy Array
# 1Transpose
var = np.matrix([[1,2,3],[4,5,6]])
print(var)
print()

print(np.transpose(var))
#2 Swapaxes
var2 = np.matrix([[1,2],[3,4]])
print(var2)
print()
print(np.swapaxes(var2,0,1))
#3 Inverse
var3 = np.matrix([[1,2],[3,4]])
print(var3)
print()

print(np.linalg.inv(var3))
#4 Power
var4 = np.matrix([[1,2],[3,4]])
print(var4)
print()

print(np.linalg.matrix_power(var4,2))
print()
print(np.linalg.matrix_power(var4,0))
print()
print(np.linalg.matrix_power(var4,-2))
print()

#5 Determinante
var5 = np.matrix([[1,2],[3,4,]])
print(var5)
print()
print(np.linalg.det(var5))

var6 = np.matrix([[1,2,3],[3,4,3],[1,2,3]])
print(var6)
print()
print(np.linalg.det(var6))
