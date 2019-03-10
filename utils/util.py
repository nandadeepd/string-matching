import os, numpy, pandas as pd
from matplotlib import pyplot as plt

class FileManipulation(object):

    def __init__(self, path):
        self.path = path
        # self.content = list()
    
    def get_file_contents(self):
        return self.content
    
    def read_file(self):
        with open(self.path, 'r') as f:
            content = f.read()
        return content

    
    # def read_csv_into_pandas(self):

# class Plotter(object):

#     def plot_text_time(self, experiment, times, lengths):
#         plt.plot(times, lengths)
#         plt.xlabel("Time"); plt.ylabel("Text Length")
#         # plt.savefig("./metrics/" + str(experiment) + ".png")
#         plt.show()

#     def sample_plot(self):
#         times = [1, 5, 3, 2, 6, 7, 8, 9, 10]
#         lengt = [50, 100, 40, 60 , 80 , 90, 300, 60, 500]
#         self.plot_text_time(experiment=1, times=times, lengths=lengt)


        
    
def main():
    # a test driver 
    # path = "sample.txt"
    # fm = FileManipulation(path)
    # fm.read_file(); print(fm.get_file_contents())

    p = Plotter()
    p.sample_plot()

if __name__ == "__main__":
    main()