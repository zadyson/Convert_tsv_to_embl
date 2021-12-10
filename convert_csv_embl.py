#!/usr/bin/env python
#
# Convert csv to embl format
# Dr Zoe A. Dyson (zoe.dyson@lshtm.ac.uk)
#
# Documentation - 
#
# Dependencies:
#	 Python2
#
# Last modified - December 10th, 2021
#

# Import required packages
from argparse import (ArgumentParser, FileType)
import os, sys, re, collections, operator

# Version number
__version__='0.0.6'

# Set up argument parser 
def parse_args():
	"Parse the input arguments, use '-h' for help"
	parser = ArgumentParser(description='Quality stats for SNVs called by GHRU mapping pipeline')
	parser.add_argument('--version', action='version', version='GHRU SNV Quality Stats Generator v' + __version__,
		help="Show version number and exit")
	parser.add_argument('--excluded_regions', type=str, required=True,
		help='Path to tsv file of regions to exclude (i.e. phages and repeats). Should not include a header line.')
	parser.add_argument('--output_prefix', type=str, required=True,
		help='Output file prefix')

	return parser.parse_args()


# main function
def main():
	args = parse_args()

	# Output summary file with header
	converted_embl = open(args.output_prefix  + ".embl", "w")

	# Build list of SNVs to exclude
	excluded_regions = open(args.excluded_regions , "r")
	positions_to_exclude = []
	for region in excluded_regions:
		region_coords = region.rstrip().split()
		converted_embl.write("FT   misc_feature    " + region_coords[0]+ ".."+region_coords[1]+ "\n")

	# Close output file for buffering
	converted_embl.close()

# call main function
if __name__ == '__main__':
	main()