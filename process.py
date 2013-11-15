import csv
import sys
from scipy import misc
import math

# Config options
header_line = False
accurate = False

def hypergeometric_distribution(N,K,n,k):
	numerator_1 = misc.comb(K,k).tolist()
	numerator_2 = misc.comb(N-K,n-k).tolist()
	denominator = misc.comb(N,n).tolist()
	return ((numerator_1 * numerator_2) / (denominator))

# Round up to the nearest odd number so that the number of
# calculations will always be balanced
def calculate_sample_size(size, fraction):
	res = int(math.ceil(size * fraction))
	if res % 2 == 0:
		res += 1
	return res

def process_arguments(arguments):
	global header_line, accurate
	for argument in arguments[1:]:
		if argument == "-header":
			header_line = True
		if argument == "-accurate":
			accurate = True

def calculate_bayesian_probability(prior, experimental):
	return (prior * experimental) / ((prior * experimental) + ((1 - prior) * (1- experimental)))


def process_line(values, line_number):
	if len(values) < 3:
		print >> sys.stderr, "Fatal error: Line", line_number, "does not have enough values on it"
		print >> sys.stderr, "Format for each line should be: [control-peptide-value],[shaved-peptide-value],[bayesian-prior-value]"
		print >> sys.stderr, "e.g. "
		print >> sys.stderr, "15,30,0.5"
	control_peptides = int(values[0])
	shaved_peptides = int(values[1])
	bayesian_prior = float(values[2])
	total_size = control_peptides + shaved_peptides
	sample_size = calculate_sample_size(total_size, 0.4)
	fifty_percent_cutoff = int(math.ceil(float(sample_size) / 2))
	total_probability = 0

	for i in range(fifty_percent_cutoff, sample_size + 1):
		total_probability += hypergeometric_distribution(total_size,control_peptides,sample_size,i)

	experimental_probability = 1 - total_probability
	final_probability = calculate_bayesian_probability(bayesian_prior, experimental_probability)

	print control_peptides, ",", shaved_peptides, ",", bayesian_prior, ",", experimental_probability, ",", final_probability

if (len(sys.argv) < 2):
	print "Usage:", sys.argv[0], "[csv-file]"
	exit()

process_arguments(sys.argv)

try:
	csv_file = open(sys.argv[1], "rU")
except:
	print "Could not find the specified input csv file:", sys.argv[1]
	exit()

line_at = 0
for line in csv.reader(csv_file, delimiter=','):
	if line_at == 0 and header_line:
		pass
	else:
		process_line(line, line_at)
	line_at += 1