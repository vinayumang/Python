#Q)Based on sweetness and sourness, which taste category does each fruit belong to?

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data = {
    'fruit_name':['mango','orange','guava','lemon','mausambi','apple','grapes'],
    'sweetness':[10,5,8,2,1,10,6],
    'sourness':[0,5,1,8,10,0,4],
    'class':[1,0,1,2,2,1,1]
}
df = pd.DataFrame(data)
X = df[['sweetness','class']]
model = KMeans(n_clusters=3,random_state=42)
model.fit(X)
df['cluster'] = model.labels_
print(df)
plt.scatter(X['sweetness'],X['class'])
plt.xlabel('sweetness')
plt.ylabel('sourness')
plt.show()