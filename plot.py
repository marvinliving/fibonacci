import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('output.csv')

fig = plt.plot(data)

fig.savefig('fibonacci.html')
