#!/usr/bin/python

import one_gram_reader
import matplotlib.pyplot as plt

def normalize_counts(years, counts, total):
	''' Returns a normalized version of counts
	
	** Keywords **
	years -- A list of years, same as provided by one_gram_reader.read_wfile
	counts -- A list of counts, same as provided by one_gram_reader.read_wfile
	total -- A dictionary of counts during each year, same as provided by one_gram_reader.read_total_counts
	
	'''
	normalized_counts = []
	
	N = len(counts)
	for x in range(N):
		year = years[x]
		total_count = total[year]
		normalized_count = counts[x] / float(total_count)
		normalized_counts.append(normalized_count)
		
	return normalized_counts
		
def plot_words(words, year_range, wfile, tfile):
	''' Creates a graph plotting relative frequency of word to year
	
	** Keywords **
	words -- A list of words
	counts -- A list of two integers
	wfile -- Name of the word csv file
	tfile -- Name of the total csv file
	
	'''
	plt.figure(1)
	plt.clf()
	plt.title('Word Frequency Over Time')
	
	total_counts_dict = one_gram_reader.read_total_counts(tfile)
	for word in words:
		years, counts = one_gram_reader.read_wfile(word, year_range, wfile)
		normalized_counts = normalize_counts(years, counts, total_counts_dict)

		plt.plot(years, normalized_counts)
		
	plt.legend(words)	
	plt.ylabel("Relative Frequency")
	plt.xlabel("Year")
	plt.grid()
	plt.draw()
	plt.show()
		

plot_words(["car", "computer", "dog"], [1800, 2005], "/Users/jackditto/Documents/OneDrive - SA/Nice Scripts/Stanford Projects/Onegram/datafiles3/all_words.csv", "/Users/jackditto/Documents/OneDrive - SA/Nice Scripts/Stanford Projects/Onegram/datafiles3/total_counts.csv")	
	