import requests
import json
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.optimize import curve_fit
from matplotlib.ticker import PercentFormatter

# get all
url = 'http://localhost:5000/waitingminedtimestat'


headers = {'content-type': 'application/json'}
response = requests.get(url, headers=headers)
# print(response.content)
results = json.loads(response.content.decode())

print('count: ', str(len(results)))
print('an example of result:', results[0])

# gas_price of a transaction
x = []

# waiting_time of a transaction
y = []

for row in results:
    gas_price = row['_id']
    waiting_mined_time = row['value']
    if(gas_price <= 50) and (waiting_mined_time <= 1000):
    # if(gas_price <= float("inf")) and (waiting_mined_time <= float("inf")):
        x.append(gas_price)
        y.append(waiting_mined_time)


# get the max of actual cost
print('the max gas price is: ', str(max(x)))
print('the min gas price is: ', str(min(x)))
print('the max waiting mined time is: ', str(max(y)))
print('the min waiting mined time is: ', str(min(y)))

print(len(x))
print(len(y))

# Plot original data
plt.scatter(x, y)
plt.title('Relation between gas price and waiting time')
plt.xlabel('gas price')
plt.ylabel('waiting mined time')

# # Set ranges of x-axis and y-axis
# plt.xlim(0,50)
# # # # plt.xlim(0.2,0.4)
# plt.ylim(0,500)

plt.legend()
plt.show()

#

# # matplotlib histogram
# plt.hist(x, color = 'blue', edgecolor = 'black',
#          bins = int(180/5))

# # seaborn histogram
# sns.distplot(x, hist=True, kde=False, 
#              bins=int(180/5), color = 'blue',
#              hist_kws={'edgecolor':'black'})

plt.hist(x, weights=np.ones(len(y)) / len(y))
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
# Add labels
plt.title('Histogram of waiting mined time')
plt.xlabel('waiting mined time')
plt.ylabel('distribution of waiting mined time')
plt.show()