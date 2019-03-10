# -*- coding: utf-8 -*-
# @Author: Nandadeep Davuluru
# @Date:   2019-03-10 11:38:34
# @Last Modified by:   nandadeep
# @Last Modified time: 2019-03-10 12:55:43
import os, time
from kmp import KMP 
from naive import NaiveStringMatch
from random import randint
from random import shuffle
from matplotlib import pyplot as plt

PATTERN_SIZE = 4 # hyper-parameter?
DIRECTORY = '/Users/nandadeepd/Desktop/string-matching/'

class Plotter(object):

    def plot_text_time(self, experiment, times, lengths):
        plt.plot(times, lengths, marker='o', color='r')
        plt.xlabel("Time"); plt.ylabel("Text Length")
        plt.savefig(DIRECTORY + "/metrics/" + str(experiment) + ".png")
        # plt.show()

    def sample_plot(self):
        times = [1, 5, 3, 2, 6, 7, 8, 9, 10]
        lengt = [50, 100, 40, 60 , 80 , 90, 300, 60, 500]
        self.plot_text_time(experiment=1, times=times, lengths=lengt)

def pattern_generator(text, total_len):
	len_edge = total_len - PATTERN_SIZE # avoiding out of bounds!
	start_num = randint(0, len_edge)
	end_num = start_num + PATTERN_SIZE # size of the pattern. 
	return start_num, end_num



def main():

	files = [f for f in os.listdir(DIRECTORY + "/datasets/")] # linear time with respect to the files. 
	file_sizes, times = list(), list() # for plots
	# files = shuffle(files)
	shuffle(files)
	for file in files: # linear pass over all files
		

		if "dna" in file:
			experiment = "dna_"
			print("reading file: {}".format(file))
			
			content = ""
			with open(DIRECTORY + "/datasets/" + file, 'rb') as f: # avoiding unicode parse errors
				content = f.read()
			total_len = len(content)
			file_sizes.append(total_len)
			print("file length: {}".format(total_len))
			indices = pattern_generator(content, total_len)
			pattern = content[indices[0]:indices[1]]
			###################### NAIVE TIMER BEGINS ######################
			# start_time = time.time()
			# naive_matcher = NaiveStringMatch(content, pattern)
			# matches = naive_matcher.search()
			# end_time = time.time()t
			###################### NAIVE TIMER ENDS #######################
			###################### KMP TIMER BEGINS ######################
			start_time = time.time()
			kmp_matcher = KMP(pattern, content)
			matches = kmp_matcher.KMPSearch()
			end_time = time.time()
			###################### KMP TIMER ENDS #######################
			times.append(end_time - start_time)
			print(end_time - start_time)
			# print(times, file_sizes)
			# print(pattern)
			# print("matches found at {}".format(naive_matcher.search()))
	p = Plotter()
	p.plot_text_time(experiment="dna_kmp", times=times, lengths=file_sizes)
		# break

	

if __name__ == '__main__':
	main()