import matplotlib.pyplot as plt

class Plotting:
    def __init__(self):
        self.count = 1
    def add_subplot(self, input: dict, title: str):
        x , y = [] , []
        input = dict(sorted(input.items(), key=lambda item: item[1], reverse=True))
        for key in input:
            x.append(key)
            y.append(input[key])

        plt.figure(self.count)
        self.count += 1
        plt.bar(x,y, align='center')
        self.addlabels(x,y)
        plt.title(title)
        plt.ylabel('Number of Instances')
        # plt.ylabel('')
        plt.show()
    
    def add_box_plot(self, input, title: str):
        plt.boxplot(input.values(),labels=input.keys())
        plt.title(title)
        plt.show()

    def addlabels(self,x,y):
        for i in range(len(x)):
            plt.text(i,y[i]+10,y[i])
        

