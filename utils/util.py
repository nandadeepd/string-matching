import os, numpy
from matplotlib import pyplot as plt

class FileManipulation(object):

    def __init__(self, path):
        self.path = path
        self.content = list()
    
    def get_file_contents(self):
        return self.content
    
    def read_file(self):
        with open(self.path, 'r') as f:
            self.content.extend(f.read().split("\n"))

class Plotter(object):

    def plot_text_time(self, experiment, times, lengths):
        plt.plot(times, lengths)
        plt.xlabel("Time"); plt.ylabel("Text Length")
        plt.savefig("./metrics/" + str(experiment) + ".png")

        
    
def main():
    # a test driver 
    # path = "sample.txt"
    # fm = FileManipulation(path)
    # fm.read_file(); print(fm.get_file_contents())

    p = Plotter()
    p.plot_text_time(2, [4, 5, 6, 7], [100, 200, 500, 600])

if __name__ == "__main__":
    main()