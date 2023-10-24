#import matplotlib.pyplot as plt
#x=['Group A','Group B','Group C', 'Group D']
#y=[10,20,5,15]
#plt.plot(x,y,color='red')
#plt.title('title') 
#plt.xlabel('fnaf')
#plt.ylabel('anamatronics')
#plt.show()

import matplotlib.pyplot as plt

labels=['apples','bananas','cherries','dates']
data=[30,25,20,20]

fig,ax=plt.subplots()
ax.pie(data,labels=labels,colors=['purple','green','blue','red'])
plt.title("Fruity")

plt.show()