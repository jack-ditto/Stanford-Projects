#!/usr/bin/python

import csv

def read_wfile(word, year_range, wfile):
	''' Returns the counts and years for the word
	
	** Keywords **
	word -- A string containing only upper and lower case letters
	year_range -- A list of exactly two numbers. These specify the date range.
	wfile -- A string giving the name of a one_gram csv file
	
	'''
	
	f = open(wfile, 'rb')
	csv_reader = csv.reader(f, delimiter = '\t') # words are separated by tabs, so \t used
	
	years = []
	counts = []
	
	for row in csv_reader:
		
		year = int(row[1])
		
		if (row[0] == word):
			if (year <= year_range[1]) and (year >= year_range[0]):
				years.append(int(row[1]))
				counts.append(int(row[2]))
	
	f.close()		
	return years, counts
	

def read_total_counts(tfile):
	''' Returns a dict with keys being year and value being total words
	
	** Keywords ##
	tfile -- name of total_counts csv file
	
	'''
	
	
	input_file = open(tfile, "rb")
	csv_reader = csv.reader(input_file, delimiter=",")
	
   # csv_reader.next()
	total_during_year = {}
	for row in csv_reader:
		try:
			year = int(row[0])
			count = int(row[1])
			total_during_year[year] = count
		except:
			pass
			
	input_file.close()    
	return total_during_year

