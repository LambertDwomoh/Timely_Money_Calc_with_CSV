#!/usr/bin/env python
# coding: utf-8

# In[4]:


from datetime import datetime
import pandas as pd

dt_string = str(input('Start date and Time in dd/mm/yyyy hh/mm/ss 24 hr format'))
try:
    dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
    #print("dt_object1 =", dt_object1)
except ValueError:
    print("Incorrect format")

dt_string1 = str(input('End date and Time in dd/mm/yyyy hh/mm/ss 24 hr format'))
try:
    dt_object2 = datetime.strptime(dt_string1, "%d/%m/%Y %H:%M:%S")
    #print("dt_object2 =", dt_object2)
except ValueError:
    print("Incorrect format")
    

diff = dt_object2.timestamp() - dt_object1.timestamp()
print("Difference is :",diff)
# this Difference is in Seconds


hrs_spent = diff/3600
print("Hours Spent on a Task ", hrs_spent)

money_earned = (diff*5)/3600
print("Money Earned :", money_earned)

# intialise data of lists.
data = {'Start Time':[dt_object1],
        'End Time':[dt_object2],
        'Hours_Spent':[hrs_spent],
        'Rate':[5],
        'Money Earned':[money_earned]}
 
# Create DataFrame
df = pd.DataFrame(data)

export_csv = df.to_csv(r"D:\\PyPower\\file.csv", mode ='a', index = False,header = False)
# Close the csv file running this code -----VERY IMPORTANT

# Apply header=False when you have already created the file

#you can Manually add column names to csv




# In[ ]:


12/12/2019 09:00:00
13/12/2019 10:00:00

