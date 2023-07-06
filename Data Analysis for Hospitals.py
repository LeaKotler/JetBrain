# write your code here
# Stage 2/5
import pandas as pd
pd.set_option('display.max_columns', 8)
general= pd.read_csv('general.csv')
prenatal= pd.read_csv('prenatal.csv')
sports= pd.read_csv('sports.csv')
prenatal.columns = general.keys()
sports.columns = general.keys()
all_db = pd.concat([general,prenatal], ignore_index = True)
all_db = pd.concat([all_db,sports],ignore_index = True)
all_db = all_db.drop(columns = 'Unnamed: 0')
#print(pd.DataFrame.sample(all_db, n=20, random_state=30))

# Stage 3/5
#print (all_db.head(5))
#all_db.dropna(axis = 0, thresh = 1, inplace = True)
all_db.dropna(axis='rows', inplace=True, how='all')
all_db.loc[all_db["gender"] == 'man', "gender"] = 'm'
all_db.loc[all_db["gender"] == 'male', "gender"] = 'm'
all_db.loc[all_db["gender"] == 'woman', "gender"] = 'f'
all_db.loc[all_db["gender"] == 'female', "gender"] = 'f'
all_db['gender'].fillna('f', inplace = True)
all_db['bmi'].fillna(0, inplace = True)
all_db['diagnosis'].fillna(0, inplace = True)
all_db['blood_test'].fillna(0, inplace = True)
all_db['ecg'].fillna(0, inplace = True)
all_db['ultrasound'].fillna(0, inplace = True)
all_db['mri'].fillna(0, inplace = True)
all_db['xray'].fillna(0, inplace = True)
all_db['children'].fillna(0, inplace = True)
all_db['months'].fillna(0, inplace = True)
#print('Data shape:', all_db.shape)
#print(pd.DataFrame.sample(all_db, n=20, random_state=30))


# Stage 4/5


one = all_db['hospital'].value_counts()
two = general.diagnosis.value_counts().loc['stomach']/general.hospital.count()
tree = sports.diagnosis.value_counts().loc['dislocation']/sports.hospital.count()
four = general.age.median()-sports.age.median()
five = all_db.groupby('hospital')["blood_test"].value_counts()

#print(f'The answer to the 1st question is {one.idxmax()}')
#print(f'The answer to the 2nd question is {two.round(3)}')
#print(f'The answer to the 3rd question is {tree.round(3)}')
#print(f'The answer to the 4th question is {four}')
#print(f'The answer to the 5th question is {five.idxmax()[0]}, {five.max()} blood tests')

#Stage 5/5

import matplotlib.pylab as plt

all_db.plot(y="age", kind="hist", bins=[0, 15, 35, 55, 70, 80])
plt.show()
print("The answer to the 1st question: 15 - 35")

all_db.diagnosis.value_counts().plot(kind="pie")
plt.show()
print("The answer to the 2st question: pregnancy")

plt.violinplot(all_db["height"])
plt.show()
print(
    "The answer to the 3rd question: It's because the height of the patients from the sports hospital was measured in feet, and the height of the patients from the general and prenatal hospital were measured in meters."
)

