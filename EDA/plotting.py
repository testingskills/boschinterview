import matplotlib.pyplot as plt

class Plotting:
    """
    A class representing ploting functions for EDA.
    """
    def __init__(self):
        """
        Initializes an plot count object.
        """
        self.count = 1
    def add_plot(self, input: dict, title: str):
        ''' 
        Creates plot single bar plot from a dictionary with title mentioned
        Parameters:
            input (dict): plot data
            title (str): Title of string.
        '''
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
        ''' 
        Creates box plot from a dictionary with title mentioned
        Parameters:
            input (dict): box plot data
            title (str): Title of string.
        '''
        plt.boxplot(input.values(),labels=input.keys())
        plt.title(title)
        plt.show()

    def addlabels(self,x,y):
        ''' 
        Creates labels on bars of plot
        Parameters:
            x (int): x coordinate
            y (int): y coordinate and value of the bar to be written on the bar data.
        '''
        for i in range(len(x)):
            plt.text(i,y[i]+10,y[i])
        

