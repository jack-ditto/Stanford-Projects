#!/usr/bin/python
import csv


def read_entire_wfile(wfile):
	''' Returns the counts and years for all words
	
	** Keywords **
	wfile -- string of path of wfile
	
	'''
	
	f = open(wfile, 'rb')
	csv_reader = csv.reader(f, delimiter = '\t')
	csv_reader_list = list(csv_reader)
	counts_list = []
	word_data = {}
	
	for row in csv_reader_list:
		word = row[0]
		
		try:
			next_row = csv_reader_list[csv_reader_list.index(row) + 1]
		except:
			next_row = [None]
		
		if not word == next_row[0]:
			counts_tuple = (int(row[1]), int(row[2]))
			counts_list.append(counts_tuple)
			word_data[word] = counts_list
			counts_list = []
			
		elif word == next_row[0]:
			counts_tuple = (int(row[1]), int(row[2]))
			counts_list.append(counts_tuple)
			
	return word_data
	
