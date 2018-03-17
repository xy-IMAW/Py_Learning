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
    #建立模型
    knn_model=KNeighborsClassifier(n_neighbors=k)
    #训练模型
    knn_model.fit(X_train,y_train)
    #测试模型
    y_pred=knn_model.predict(X_test)
    #计算准确率
    acc=accuracy_score(y_test,y_pred)

    models_list.append(knn_model)
    acc_results.append(acc)

   # print('k={},准确率={:.2f}'.format(k,acc))    

''' #可视化不同的k值对结果的影响
plt.figure(figsize=(8,8))
plt.plot(acc_results)
# 标题
plt.title('kNN with different k values')
# x轴
plt.xlabel('k value')
plt.xticks(range(len(k_list)), k_list)
# y轴
plt.ylabel('accuracy')
plt.ylim([0.8, 1.0])
plt.show() '''

#找出最优的k值所对应的model
best_k_idx=np.argmax(acc_results)
best_model=models_list[best_k_idx]

#持久化模型
model_file='Biomechanical features of orthopedic patients/model.pkl'
with open(model_file,'wb')as f:
    pickle.dump(best_model,f)

#随机选择n个病人的数据
n=100
flag=0
random_sample_data=all_data.sample(n)
#print(random_sample_data)

with open(model_file,'rb')as f:
    trained_model=pickle.load(f)
    x=random_sample_data.iloc[:,-1].values
    y=trained_model.predict(random_sample_data.iloc[:,:6].values)
    print('实际患病情况:\n{}'.format(x))
    print('预测患病情况:\n{}'.format(y))
    
    for i in range(len(x)):
        if(x[i]==y[i]):
            flag=flag+1
    print ('实际预测率={}'.format(flag/n))