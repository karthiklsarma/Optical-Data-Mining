import cPickle
from sklearn.ensemble import RandomForestClassifier
from _elementtree import dump
#df = pd.read_csv("../train_data.txt")
#print(df.head())
#print df.ix[0]

file = open("../train_data_new.txt",'r')
labelfile = open("../train_label_new.txt",'r')
label = []
for line in labelfile.readlines():
    label.append(float(line))
alldata = file.readlines()
input = []
for line in alldata:
    line = line.split(',')
    line = map(lambda x: float(x), line)
    input.append(line)


testfile = open("../test_data_new.txt",'r')
test = []
for line in testfile.readlines():
    line = line.split(',')
    line = map(lambda x: float(x), line)
    input.append(line)

clf = RandomForestClassifier(n_estimators=1000)
model = clf.fit(input, label)
with open('rf','wb') as f:
    cPickle .dump(model, f)

with open('rf','rb') as f:
    model = cPickle.load(f)
    
preds = model.predict(test)
print preds

target = open('RandomForestOut.txt', 'w')
lstout = []
lstout = str(preds).strip('[*]').split('.')
for line in lstout:
    valStr = line.strip()
    if(valStr != '\t' and valStr !=''):
        target.write(valStr+'\n')
target.close()

'''
def calcerror(actual, predicted):
    correct = 0
    incorrect = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct = correct + 1
        else:
            incorrect = incorrect + 1
    print correct, incorrect
    
calcerror(label, preds)
'''


    
