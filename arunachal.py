import pandas as pd
import matplotlib.pyplot as plt
sample = pd.read_csv('sortarunachalfile.csv', index_col=0)
print(sample)
sample2 = sample.iloc[:, [0,1,2,3]]
print(sample2) 
sample3 = sample2.sort_values('GPs connected', ascending = True)
fig = plt.figure(figsize =(40,8))
ax1=fig.add_subplot(1,2,1)
ax1.bar(sample3.index,sample3['GPs connected'])
ax1.set_title('ARUNACHAL PRADESH',fontsize='20')
ax1.set_xlabel('FPOI')
ax1.set_ylabel('GPs connected')
plt.show()