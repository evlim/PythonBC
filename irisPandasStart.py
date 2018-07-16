# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

""" Input data """
f_in = open('irisData.csv','r')
data = f_in.readlines()
f_in.close()  
 
""" Strip and split each row of data """
for i in range(len(data)):
    data[i] = data[i].strip().split(',')

colHeadings = [x.strip() for x in data[0]]
del data[0]

""" Read column heading data from first row, then delete the row """
species = [x[0] for x in data]
SepalLengthIn = [float(x[1].strip()) for x in data]
SepalWidthIn = [float(x[2].strip()) for x in data]
PetalLengthIn = [float(x[3].strip()) for x in data]
PetalWidthIn = [float(x[4].strip()) for x in data]
color = ['r' if x == 'Iris-setosa' else 'b' if x =='Iris-versicolor' else 'g' for x in species]
        
""" create variables for accessing the Figure adn Axes sub-objects """
fig,ax = plt.subplots()

""" Axes sub-object properties and methods """
ax.scatter(SepalLengthIn,PetalLengthIn,c=color, alpha=0.5,s=75)
ax.xaxis.set_label_text('Petal Length(in)', fontsize = 16)
ax.yaxis.set_label_text('Sepal Length (in)', fontsize = 16)
ax.xaxis.set_tick_params(labelsize=14)
ax.yaxis.set_tick_params(labelsize=14)
ax.axhline(1.0)
ax.axhline(1.9)

""" Figure sub-object properties and methods """
fig.suptitle('Sepal Length versus Petal Length', fontsize = 20)
fig.set_size_inches(10,7)
fig.savefig('sepLenPetLen.jpg')

""" Display graph """
plt.show()