import csv 
import random
import pandas as pd

# fields = ['num0', 'num1', 'sum'] 
# rows = []

# i = 0
# while i != 1000:
#     num0 = random.randint(0,9)
#     num1 = random.randint(0,9)
#     sum = num0 + num1
    
#     ans = [num0, num1, sum]
#     # if ans not in rows:
#     rows.append(ans)
#     i+=1

# print(rows)

# filename = "data.csv" 
# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fields)  
#     csvwriter.writerows(rows)


df = pd.read_csv('data.csv')

X = df[['num0', 'num1']]
y = df[['sum']]

print(X)
print(y)