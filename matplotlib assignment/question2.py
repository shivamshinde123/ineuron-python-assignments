import pandas as pd
import matplotlib.pyplot as plt


url="https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv"
titanic = pd.read_csv(url)


## pie chart of male/female population

plt.pie(titanic['sex'].value_counts(),labels=['male','female'],autopct='%1.1f%%',explode=(0,0.1))
plt.show()