from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#Given Data
X = [2.,4.,6.,8.]
Y = [3.,4.,5.,6.]

#I assume our model is linear
#Our goal is to find the most optimized 'a', 'b' to predict(or add new rules) values.
def func_linear(x,a,b):
    return a*x + b

#Distribute them to training set and verification set
X_training = X[:3]
Y_training = Y[:3]
X_verification = X[3]
Y_verification = Y[3]

#If our linear model work well at X_verification, I will use the model for Y_prediction
X_predicton = [10.,12.,14.,16.]
coeff, *_ = curve_fit(func_linear, X_training, Y_training)

#we need to verify our model before predicting
Y_test_prediction = func_linear(X_verification, *coeff)
diff = Y_test_prediction - Y_verification
print('Error of our model is ',diff)

#predicton initiated
Y_prediction = [func_linear(x, *coeff) for x in X_predicton]

#visualize our model
plt.plot(X_training, Y_training, label = 'training')
plt.plot(X_verification, Y_verification, marker = '*', label = 'verification', markersize = 15)
plt.plot(X_verification, Y_test_prediction, marker = 'o', label = 'test_prediction')
plt.plot(X_predicton, Y_prediction, label = 'prediction')
plt.xlabel('features')
plt.ylabel('target values')
plt.title('Simple example of machine learning')
plt.legend()

print('Imagine that features would be components on the image of cat like eyes, nose, mouth...' + \
      '\nAfter training and verification, our model can recognize other cats images as real cats by itself!!')

import webbrowser
ask = input('Do you want to visit my twitter account? y/[n]')
if ask == 'y':
    url = 'https://twitter.com/MayflyPython'
    webbrowser.open_new_tab(url)