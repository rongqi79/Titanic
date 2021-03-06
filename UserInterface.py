import pandas as pd;
from sklearn.datasets import load_iris;
import numpy as np;
import util;
from NewClassifier import NewClassifier;
from sklearn.model_selection import train_test_split
from sklearn import preprocessing;

dataSet = input("What's your choice of dataset?\n"
                "1: bank;"
                "2: titanic;"
                "3: iris;"
                )

if dataSet=='1':
    df = pd.read_csv('./bank/bank.csv', delimiter=';')
    data_name='bank'

elif dataSet=='2':
    df = pd.read_csv('titanic_data.csv')
    data_name = 'titanic'
    '''columns = ['Ticket','Cabin','Name']
    df.drop(columns, axis=1, inplace=True)
    def process_ports(df):
        if len(df.Age[df.Embarked.isnull()]) > 0:
            df.loc[(df.Embarked.isnull()), 'Embarked'] = '$'
        le = preprocessing.LabelEncoder()
        df['Embarked'] = le.fit_transform(df['Embarked'])
        return df
    process_ports(df)
    df["Sex"] = df["Sex"].apply(lambda sex: 1 if sex == "male" else 0)'''


elif dataSet=='3':
    iris = load_iris()
    df=pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                 columns=iris['feature_names'] + ['target'])
    data_name = 'iris'
else:
    print("dataset could not be found")


df=util.dataPreprocessing(df)
df=util.featureSelection(df)
X = util.getX(df)
Y = util.getY(df)


#data_train, data_test, target_train, target_test = train_test_split(X, Y,test_size=0.2, random_state=43)
data_train, data_test, target_train, target_test = train_test_split(X, Y,test_size=0.2)


clf=NewClassifier(data_name=data_name)

clf.fit(data_train,target_train)

clf.sortedResult(data_test,target_test)

# m is the number of top algorithms I will choose to get my prediction
m=int(input("the number of algorithms I will choose to get my prediction"))

prediction=clf.multiPredict(data_test,target_test,m)

clf.score(target_test)