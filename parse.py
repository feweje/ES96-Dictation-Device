# Script to import information from a .txt file into a .csv spreadsheet 

from sys import argv
import csv
import openpyxl

# Command line inputs are: the current script, the .txt filename from which data will be imported, the .csv file we are writing to

script, txt_file, csv_file = argv

# open the text file, and read into the text file to extract data
text = open(txt_file)
data = text.readlines()

# test function: print the lines read from the text file
print data 

# write to csv
csv = open(csv_file, 'w')
for element in data: 
	csv.write(element)
