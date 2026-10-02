
# IMPORTING LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# GETTING THE FILE

file = pd.read_csv('Sales.csv')
df = pd.DataFrame(file)



# FINDING THE NULL VALUES IF ANY

a = df.isna().sum()



# CONVERTING TEXT TO DATETIME

df['Date'] = pd.to_datetime(df['Date'])

# GROUPING TOTAL REVENUE BY CATEGORY AND GENDER

a = df.groupby(['Product Category','Gender'])['Total Amount'].sum().reset_index() 

# VISUALIZATION

fig, axis = plt.subplots(nrows = 1 , ncols = 2, figsize = (12,8))
sns.histplot (data = df , x = 'Age' , bins = 15, kde = True, ax = axis[0]  )
sns.barplot(data = a , x = 'Product Category' , y = 'Total Amount' , hue = 'Gender', ax = axis[1])
axis[1].set_title("TOTAL AMOUNT BY CATEGORY & GENDER" , fontsize = 15 , fontweight = "bold")
axis[1].set_xlabel("REVENUE")
axis[1].set_ylabel("CATEGORY & GENDER")
axis[1].grid(True , alpha = .5 , linestyle = '--')
axis[0].set_title("NO. OF CUSTOMER BY AGE" , fontsize = 15 , fontweight = "bold")
axis[0].set_xlabel("AGE")
axis[0].set_ylabel("COUNT OF CUSTOMERS")
axis[0].grid(True , alpha = .5 , linestyle = '--')
fig.suptitle("DASHBOARD" , fontsize = 20 , fontweight = 'bold')


plt.show()

