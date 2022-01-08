# Scikit-learn

每一行代表一个样本，每一列代表一种特征

(n_samples, n_features)

## 1 模型预处理

### 1.1 获取样本数据

​	datasets 模块主要有两种数据类型。 较小的测试数据集在 sklearn 包里面， 可
以通过 datasets.load\_\*? 查看。 较大的数据集可以根据需要下载。 后者默认情
况下不在 sklearn 包里面； 需要通过 datasets.fetch\_\*?  下载 

1. `datasets.load_`

```python
from sklearn import datasets
import numpy as np

boston = datasets.load_boston()
boston.keys()
# dict_keys(['data', 'target', 'feature_names', 'DESCR'])

X, y = boston.data, boston.target
```

2. `datasets.fetch_`

```python
housing = datasets.fetch_california_housing()
housing.keys()
# dict_keys(['data', 'target', 'feature_names', 'DESCR'])
```



### 1.2 创建实验样本

- ` datasets.make_`

```python
# 创建K-Means数据集合
from sklearn import datasets

# blobs是一个元组
blobs = datasets.make_blobs(200)
X, y = blobs[0], blobs[1]
```



### 1.3  把数据调整为正态分布

- `preprocessing.StandardScaler()`

```python
from sklearn import datasets

boston = datasets.load_boston()
X, y = boston.data, boston.target
X[:, :3].mean(axis=0)  # 前3列的均值 
# array([ 3.59376071, 11.36363636, 11.13677866])

from sklearn import preprocessing

my_scaler = preprocessing.StandardScaler()
my_scaler.fit(X[:, :3])
X = my_scaler.transform(X[:, :3]).mean(axis=0)
X[:, :3].mean(axis=0)
# array([ 6.34099712e-17, -6.34319123e-16, -2.68291099e-15])

my_scaler.fit_transform(X[:, :3])
X[:, :3].mean(axis=0)
# array([ 6.34099712e-17, -6.34319123e-16, -2.68291099e-15])
```



### 1.4 用阈值创建二元特征

- `preprocessing.binarize`（ 一个函数） 

```python
from sklearn import preprocessing
new_target = preprocessing.binarize(boston.target.reshape(-1, 1), 			  											threshold=boston.target.mean())
new_target[0, :5]
# array([[1.], [0.], [1.]])
```

- `preprocessing.Binarizer` （ 一个类） 

```python
from sklearn import preprocessing

bin = preprocessing.Binarizer(boston.target.mean())
new_target = bin.fit_transform(boston.target.reshape(-1, 1))
new_target[0, :5]
# array([[1.], [0.], [1.]])
```



### 1.5 分类变量处理

- `preprocessing.OneHotEncoder`

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

# d = np.hstack((X, y.reshape(-1, 1)))
d = np.column_stack((X, y))

d[:, -1:].shape
# (150, 1)	二维数组
d[:, -1].shape
# (150, )	一维数组

from sklearn import preprocessing

text_encoder = preprocessing.OneHotEncoder()
text_encoder.fit_transform(d[:, -1:]).toarray()[:3]
# array([[1., 0., 0.],
#       [1., 0., 0.],
#       [1., 0., 0.]]
```

- `feature_extraction.DictVectorizer `可以将字符串转换成分类特征 

```python
from sklearn.feature_extraction import DictVectorizer

dv = DictVectorizer()
my_dict = [{'species': iris.target_names[i]} for i in y]
#　[{'species': 'setosa'},
#　 {'species': 'setosa'},
#　 {'species': 'setosa'},

dv.fit_transform(my_dict).toarray()[:3]
# array([[1., 0., 0.],
#       [1., 0., 0.],
#       [1., 0., 0.]]
```



### 1.6 标签特征二元化

- `preprocessing.LabelBinarizer`

```python
from sklearn import datasets as d

iris = d.load_iris()
target = iris.target

from sklearn.preprocessing import LabelBinarizer

label_binarizer = LabelBinarizer()
new_target = label_binarizer.fit_transform(target)
new_target[:3]
# array([[1., 0., 0.],
#       [1., 0., 0.],
#       [1., 0., 0.]]

label_binarizer = LabelBinarizer(neg_label=-1000, pos_label=1000)
label_binarizer.fit_transform(target)[:5]
# array([[ 1000, -1000, -1000],
#        [ 1000, -1000, -1000],
#        [ 1000, -1000, -1000]])
```



### 1.7 处理缺失值

- `preprocessing.Imputer`
  - 均值 `strategy='mean'` （ 默认方法） 
  - 中位数 `strategy='median' `
  - 众数 `strategy='most_frequent' `
  - `missing_values=-1`

```python
from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
iris_X = iris.data
masking_array = np.random.binomial(1, .25, iris_X.shape).astype(bool)
# np.random.binomial(1, .25, iris_X.shape)[:3]
# array([[0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 1, 0, 0]])

# masking_array[:5]
# array([[False, False, False,  True],
#        [False, False, False,  True],
#        [ True,  True, False, False]])

iris_X[masking_array] = np.nan
# iris_X[:3]
# array([[5.1, 3.5, 1.4, nan],
#        [4.9, 3. , 1.4, nan],
#        [nan, nan, 1.3, 0.2]])

from sklearn import preprocessing

impute = preprocessing.Imputer()
iris_X_prime = impute.fit_transform(iris_X)
# iris_X_prime[:3]
# array([[ 5.1,  3.5,  1.4, -1. ],
#       [ 4.9,  3. ,  1.4, -1. ],
#       [-1. , -1. ,  1.3,  0.2]])

# impute = preprocessing.Imputer(strategy='median')
# impute = preprocessing.Imputer(missing_values=-1)  # 缺失值为 —1
```



### 1.8 用管线命令处理多个步骤

- `pipeline.Pipeline`
  - `fit`
  - `transform`
  - `fit_transform`

```python
from sklearn import datasets
import numpy as np

mat = datasets.make_spd_matrix(10)
masking_array = np.random.binomial(1, .1, mat.shape).astype(bool)
mat[masking_array] = np.nan


from sklearn import preprocessing
impute = preprocessing.Imputer()
scaler = preprocessing.StandardScaler()

##############################################

mat_imputed = impute.fit_transform(mat)
mat_imp_scaled = scaler.fit_transform(mat_imputed)

###############################################

from sklearn import pipeline

# 对象名称， 对象 
pipe = pipeline.Pipeline([('impute', impute), ('scaler', scaler)])
new_mat = pipe.fit_transform(mat)

###############################################

np.array_equal(new_mat, mat_imp_scaled)
# True
```



### 1.9 用主成分分析降维

- `decomposition.PCA()`
  - `n_components=2`
  - `n_components=.98`

```python
from sklearn import decomposition

pca = decomposition.PCA()
iris_pca = pca.fit_transform(iris_X)
# iris_pca[:2]
# array([[-2.68420713e+00,  3.26607315e-01, -2.15118370e-02,
#         1.00615724e-03],
#       　[-2.71539062e+00, -1.69556848e-01, -2.03521425e-01,
#         9.96024240e-02]])

# 解释方差比， 各个主成分能表示的变量
pca.explained_variance_ratio_
#　array([0.92461621, 0.05301557, 0.01718514, 0.00518309])

pca = decomposition.PCA(n_components=2)
iris_X_prime = pca.fit_transform(iris_X)
iris_X_prime.shape
# (150, 2)

# 二维数据保留了多少特征
pca.explained_variance_ratio_.sum()
# 0.9776317750248034

# 一开始设置解释变量的比例。 例如， 如果我们想介绍98%的变量
pca = decomposition.PCA(n_components=.98)
iris_X_prime = pca.fit_transform(iris_X)
pca.explained_variance_ratio_.sum()
# 0.9948169145498101
iris_X_prime.shape
# (150, 3)
```



### 1.10 用核PCA实现非线性降维

数据先通过核函数（ kernel function） 转换成一个新空间， 然后再用PCA处理 



## 2 模型后处理

### 2.1 K-fold 交叉验证

```python
N = 1000
holdout = 200

from sklearn.datasets import make_regression

X, y = make_regression(1000, shuffle=True)
X_h, y_h = X[:holdout], y[:holdout]
X_t, y_t = X[holdout:], y[holdout:]

from sklearn.cross_validation import KFold

kfold = KFold(len(y_t), n_folds=4)

output_string = "Fold: {}, N_train: {}, N_test: {}"
for i, (train, test) in enumerate(kfold):
    print(output_string.format(i, len(y_t[train]), len(y_t[test])))
    
# Fold: 0, N_train: 600, N_test: 200
# Fold: 1, N_train: 600, N_test: 200
# Fold: 2, N_train: 600, N_test: 200
# Fold: 3, N_train: 600, N_test: 200

```



### 2.5 网格搜索

- `grid_search.GridSearchCV`

```python
from sklearn.grid_search import GridSearchCV

param_grid = [
    {
        'weights': ['uniform'], 
        'n_neighbors': [i for i in range(1, 11)]
    },
    {
        'weights': ['distance'],
        'n_neighbors': [i for i in range(1, 11)], 
        'p': [i for i in range(1, 6)]
    }
]

knn_clf = KNeighborsClassifier()
from sklearn.model_selection import GridSearchCV

%%time
grid_search = GridSearchCV(knn_clf, param_grid, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)
```



### 2.6 分类性能度量 

- `metrics.confusion_matrix`
- `metrics.precision_score`
- `metrics.recall_score`
- `metrics.f1_score`

```python
from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, y_predict)

from sklearn.metrics import precision_score

precision_score(y_test, y_predict)

from sklearn.metrics import recall_score

recall_score(y_test, y_predict)

from sklearn.metrics import f1_score

f1_score(y_test, y_predict)
```



### 2.7 保存和读取模型

- `externals.joblib`

```python
from sklearn import datasets, tree

X, y = datasets.make_classification()
dt = tree.DecisionTreeClassifier()
dt.fit(X, y)

from sklearn.externals import joblib

joblib.dump(dt, 'dtree.clf')

dt = joblib.load('dtree.clf')
dt.predict(X)
```

