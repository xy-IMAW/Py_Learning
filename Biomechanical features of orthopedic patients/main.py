import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pickle


#data.csv
data_file='Biomechanical features of orthopedic patients/data.csv'
all_data=pd.read_csv(data_file)
#print('dataframe',all_data)
#print( all_data.head())  #查看前面几项
#print(all_data.info())     #查看数据详情
#print(all_data.describe())     #数据统计
#数据特征关系可视化
#sns.pairplot(data=all_data,hue='class')
#plt.show()

#数据处理
#将类别转化为编码
all_data['lable']=all_data['class'].map({'Abnormal':1,'Normal':0})
X=all_data.iloc[:,:6].values#总样本个数x.shape[0]=310,每个样本的维度x.shape[1]=6
y=all_data['lable'].values
#分割训练集和测试集
#1/3的样本作为测试样本，用于测试学习
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=1/3,random_state=10)
#print(X_train.shape[0],X_test.shape[0])训练集样本数206，测试解样本数104

#数据分析，使用简单的kNN模型
#建立一个模型
knn_model=KNeighborsClassifier()
#训练模型
knn_model.fit(X_train,y_train)
#在测试集上测试模型
y_pred=knn_model.predict(X_test)
#计算预测准确率
acc=accuracy_score(y_test,y_pred)
print('预测准确率：{:.2f}'.format(acc))

#测试不同的k值
k_list=[1,5,10,15,20]
acc_results=[]
models_list=[]

for k in k_list:
    