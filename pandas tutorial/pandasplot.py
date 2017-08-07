import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000),index=np.arange(1000))
print(data)
data = data.cumsum()
data.plot()
plt.show()


# Data Frame
data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list("ABCD")
    )
print(data)
data.cumsum()
data.plot()

# plot methods:
# 'bar', 'hist', 'box', 'kde', 'area', 'scatter', 'hexbin', 'pie' 


ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
# append on ax
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)

plt.show()