import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import datasets 
from convexHull import myConvexHull

print("------------------------------------")
print("CONVEX HULL 13520060")
print("------------------------------------")

# memilih dataset
print()
print("Dataset yang bisa digunakan :")
print("1. Iris")
print("2. Breast Cancer")
print("3. Wine")
print()

datasetsChoice = int(input("Dataset pilihan : "))

if datasetsChoice == 1 :
    data = datasets.load_iris() 
elif datasetsChoice == 2 :
    data = datasets.load_breast_cancer()
elif datasetsChoice == 3 :
    data = datasets.load_wine()

# membuat dataframe
df = pd.DataFrame(data.data, columns=data.feature_names) 
df['Target'] = pd.DataFrame(data.target) 
df.head()

# memilih input x dan y
print("Attributes:")
for i in range (len(data.feature_names)) :
    print(str(i)+". "+str(data.feature_names[i]))
print()

# diasumsikan input x dan y selalu benar
x = int(input("Nilai x pilihan : "))
y = int(input("Nilai y pilihan : "))

# visualisasi hasil ConvexHull
plt.figure(figsize = (10, 6))
colors = ['blue','red','green', 'purple', 'pink', 'brown', 'orange', 'black', 'beige', 'yellow']

title = str(data.feature_names[x]) + " vs " + str(data.feature_names[y]) 
plt.title(title)
plt.xlabel(data.feature_names[x])
plt.ylabel(data.feature_names[y])

for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[x,y]].values
    hull = myConvexHull(bucket) #fungsi myConvexHull hasil implementasi
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])

plt.legend()
plt.show()