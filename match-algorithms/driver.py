# -*- coding: utf-8 -*-
# @Author: Nandadeep Davuluru
# @Date:   2019-03-10 11:38:34
# @Last Modified by:   nandadeep
# @Last Modified time: 2019-03-12 20:42:22
import os, time
from kmp import KMP 
from naive import NaiveStringMatch
from bm import BoyerMoore
from random import randint
from random import shuffle
from matplotlib import pyplot as plt
from timeit import default_timer as timer
import itertools

PATTERN_SIZE = 4 # hyper-parameter?
DIRECTORY = '/Users/nandadeepd/Desktop/string-matching/'

class Plotter(object):

    def plot_text_time(self, experiment, s_times, lengths, color):
        print("-----------------")
        print(s_times, lengths)
        print("-----------------")
        plt.scatter(s_times, lengths, c=["r", "g", "c", "b", "k"])
        plt.xlabel("Time"); plt.ylabel("Text Length")
        plt.savefig(DIRECTORY + "/metrics/" + str(experiment) + ".png")


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
	file_sizes, times, p_times = list(), list(), list() # for plots
	# files = shuffle(files)
	shuffle(files)
	for file in files: # linear pass over all files
		
		# if "url" in file:
		# 	# experiment = "all"
		# 	print("reading file: {}".format(file))
		# 	content = ""
		# 	with open(DIRECTORY + "/datasets/" + file, 'rb') as f: # avoiding unicode parse errors
		# 		content = f.read()
		# 	total_len = len(content)
		# 	print("file length: {}".format(total_len))
		# 	file_sizes.append(total_len)
		# 	pattern = 'jpg'
		# 	print("patter to search for:", pattern)
		# 	start_time = timer()
		# 	naive_matcher = NaiveStringMatch(content, pattern)
		# 	matches = naive_matcher.search()
		# 	print(len(matches))
		# 	end_time = timer()
		# 	times.append((end_time - start_time) )

		if "dna" in file:
			# experiment = "dna_"
			print("reading file: {}".format(file))
			
			content = ""
			with open(DIRECTORY + "/datasets/" + file, 'rb') as f: # avoiding unicode parse errors
				content = f.read()
			total_len = len(content)
			file_sizes.append(total_len)
			print("file length: {}".format(total_len))
			indices = pattern_generator(content, total_len)
			pattern = content[indices[0]:indices[1]]
			print("patter to search for: ", pattern)
			##################### NAIVE TIMER BEGINS ######################
			start_time = time.time()
			naive_matcher = NaiveStringMatch(content, pattern)
			matches = naive_matcher.search()
			print(len(matches))
			end_time = time.time()
			##################### NAIVE TIMER ENDS #######################
			###################### KMP TIMER BEGINS ######################
			# start_time = time.time()
			# kmp_matcher = KMP(pattern, content)
			# matches = kmp_matcher.KMPSearch()
			# end_time = time.time()
			###################### KMP TIMER ENDS #######################
			times.append((end_time - start_time) )
			print((end_time - start_time) * 10)
		print("--------------------------------------------------------------")
	p = Plotter()
	colors = itertools.cycle(5 * ["r", "g", "c", "b", "k"])
	p.plot_text_time(experiment="experiment", s_times=times, lengths=file_sizes, color = next(colors))
		# break

	

if __name__ == '__main__':
	main()