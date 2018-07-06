import numpy as np 
import matplotlib.pyplot as plt 

X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
print(X)
print(y)
print("X shape: ", X.shape[0])
one = np.ones((X.shape[0], 1))
print(one)
Xbar = np.c_[(one, X)]
print("Xbar: ",Xbar)
theta = np.linalg.inv(Xbar.T.dot(Xbar)).dot(Xbar.T).dot(y)
print(theta)
theta_0 = theta[0][0]
theta_1 = theta[1][0]
print("Theta_0: ", theta_0)
print("Theta_1: ", theta_1)
predict_1 = theta_0+ theta_1*170
print("Du bao can nang cua thang cao 170cm = ", predict_1)
x0 = np.linspace(145, 185, 2)
print("X0 = ", x0)
y0 = theta_0 + theta_1*x0
#Lay hai toa do bat ki de 
print("y0 = ", y0)
plt.plot(X.T, y.T, "ro")
plt.axis([140, 190, 40, 75])
plt.plot(x0, y0)
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")

plt.show()