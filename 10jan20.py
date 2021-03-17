# X,Y=input().split()
# if int(Y)>int(X):
#     if int(X)+3>int(Y):
#         print("Yes")
#     else:
#         print('No')
# if int(X)>int(Y):
#     if int(Y)+3>int(X):
#         print("Yes")
#     else:
#         print('No')

# import numpy as np
# N=input()
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# TA= np.asarray(A)
# TB= np.asarray(B)

# if np.inner(TA,TB)==0:
#     print('Yes')
# else:
#     print('No')


N=input()
A=list(map(int, input().split()))
B=(2**int(N))/2
print(B)
list1=A[:int(B)]
print(list1)