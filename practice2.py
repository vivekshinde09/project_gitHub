import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


dataset=pd.read_excel("Titanic.csv.xlsx")
dataset.head(3)


sns.histplot(x="Age", data=dataset)
plt.show()