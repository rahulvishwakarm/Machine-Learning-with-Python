#Importing the essential library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
def gd(x,y):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    m_curr=c_curr=0
    itera=1000
    n=len(x)
    learning_rate=0.08
    for i in range(itera):
        y_predicted=m_curr*x+c_curr
        #Estimating the cost function
        cost=(1/n)*sum([val**2 for val in (y-y_predicted)])
        md=-(2/n)*sum(x*(y-y_predicted))
        db=-(2/n)*sum(y-y_predicted)
        m_curr=m_curr-learning_rate*md
        c_curr=c_curr-learning_rate*db
        print(m_curr,c_curr,cost)
gd(x,y)
