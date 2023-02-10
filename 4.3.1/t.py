# importing matplotlib 
import matplotlib.pyplot as plt
  
  
# making a simple plot
x =[1, 2, 3, 4, 5]
y =[1, 2, 1, 2, 1]
  
# creating error
y_errormin =[0.1, 0.5, 0.9,
             0.1, 0.9]
y_errormax =[0.2, 0.4, 0.6, 
             0.4, 0.2]
  
x_error = 0.5
y_error =[y_errormin, y_errormax]
  
# ploting graph
plt.plot(x, y)
plt.errorbar(x, y,
             yerr = y_error,
             xerr = x_error, 
             fmt ="o")
plt.show()