from sklearn.datasets import load_iris
data = load_iris()
print(data.target[[10, 25, 50]])
# print(data.target[[1,2,3]])
# print(list(data.target_names))
# print(data['data'])
print(data['target'])
'''
- ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
-  ['setosa' 'versicolor' 'virginica']

'''