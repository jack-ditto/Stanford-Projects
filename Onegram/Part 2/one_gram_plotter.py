#!/usr/bin/python
from one_gram_reader import * 
import matplotlib.pyplot as plt

def total_occurrences(word_data, word):
	''' Returns total occurrences of word
	
	** Keywords **
	word_data -- A dictionary of word to tuples created by read_entire_wfile
	word -- An english word. Not guaranteed to exist in word_data
	
	'''
	if word in word_data:
		total_occurences = 0
		
		for year in word_data[word]:
			total_occurences += year[1]
	
	else:
		return 0
			
	return total_occurences

def count_letters(word_data):
	''' A list of length 26 where the 0th element is the percentage of letters that are a, the 1st element is the percentage of letters that are b, and so forth.
	
	** Keywords **
	word_data -- A dictionary of word to tuples created by read_entire_wfile
	
	'''
	letter_counter = {}
	
	for word, tuple_list in word_data.iteritems():
		for letter in word.lower():
			letter_counter[letter] = letter_counter.get(letter, 0) + total_occurrences(word_data, word)
			
	counts = []
	for letter in "abcdefghijklmnopqrstuvwxyz":
		counts.append(letter_counter.get(letter, 0))

	total = float(sum(counts))
	
	for i in range(len(counts)):
		counts[i] = counts[i] / total
	
	return counts
		

def bar_plot_of_letter_frequencies(word_data):
	''' Returns nothing. Instead, creates a figure similar to that shown in the example.
	
	** Keywords **
	word_data -- A dictionary of word to tuples created by read_entire_wfile
	
	'''
	
	counts = count_letters(word_data)
	objects = list("abcdefghijklmnopqrstuvwxyz")
	
	performance = list(range(26))
	
	plt.bar(performance, counts, width=.7, tick_label=objects)
	plt.show()
	
def plot_aggregate_counts(word_data, words):
	''' Returns nothing. Instead, creates a figure that plots occurrences and rank
	
	** Keywords **
	word_data -- A dictionary of word to tuples created by read_entire_wfile
	words -- A list of words to be annotated
	
	'''
	
	total_occurrences_list = []
	
	for word in word_data:
		total_occurrences_list.append(total_occurrences(word_data, word))
	
	total_occurrences_list = list(reversed(sorted(total_occurrences_list)))
	x_values = list(range(len(total_occurrences_list)))
	plt.loglog(x_values, total_occurrences_list, marker='o', markersize=4, markerfacecolor='red', markeredgecolor='red')

	for word in words:
		word = word.lower()
		x_coord = total_occurrences(word_data, word)
		position = total_occurrences_list.index(x_coord)
		plt.plot(position, x_coord, marker='*', markerfacecolor='green', markeredgecolor='green', markersize=8)
		plt.annotate(word, (position, x_coord), size=9, xytext=(position*1.1, x_coord))
	
	plt.show()


def get_occurrences_in_year(word_data, word, year):
	''' Returns an integer giving the total number of occurrences of the word during the year specified.
	
	** Keywords **
	word_data -- A dictionary of word to tuples created by read_entire_wfile
	word -- A string representing an English word. The word does not necessarily appear in word_data
	year -- An integer representing the year of interest
	
	'''
	tuples_list = word_data.get(word, [])
	for tuple_ in tuples_list:
		if tuple_[0] == year:
			return tuple_[1]

def get_average_word_length(word_data, year):
	''' Returns a floating point number representing the average length of all words during the year specified.
	
	** Keywords **
	word_data -- A dictionary of word to tuples created by read_entire_wfile
	year -- An integer representing the year of interest
	
	'''
	total_occurrences = 0
	for word in word_data:
		total_occurrences += total_occurrences(word_data, word)
		
			
			
		

word_data = read_entire_wfile("/Users/jackditto/Documents/OneDrive - SA/Nice Scripts/Stanford Projects/Onegram/datafiles3/very_short.csv")
print get_occurrences_in_year(word_data, 'wandered', 2005)

	