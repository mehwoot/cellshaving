import csv
import sys
import math

# Config options
header_line = False
accurate = False


# See function below
def choose(n,k):
    if k == 0:
    	return 1.0
    return float((n * choose(n - 1, k - 1)) / k)

    # 12, 4, 5, 5
# Define our own function so the code doesn't have dependencies people have to install
def hypergeometric_distribution(N,K,n,k):
	# Test if the hypergeometric distribution cannot be calculted for these values
	if ((k > K) or (n-k > N-K) or (n > N)):
		return None 
	numerator_1 = choose(K,k)
	numerator_2 = choose(N-K,n-k)
	denominator = choose(N,n)
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

# Bayes... hooray
def calculate_bayesian_probability(prior, experimental):
	return (prior * experimental) / ((prior * experimental) + ((1 - prior) * (1- experimental)))

def print_header():
	print "Control Peptides,Shaved Peptides,Bayesian Prior,Experimental Probability,Calculated Bayesian Probability"

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

	if total_size < 5:
		if shaved_peptides > control_peptides:
			experimental_probability = 0.9
		if control_peptides > shaved_peptides:
			experimental_probability = 0.1
		if control_peptides == shaved_peptides:
			experimental_probability = 0.5
	else:
		# We produce a result if any of the hypergeometric distributions are valid, but if none are, fall back to the logic outlined above
		valid = False
		for i in range(fifty_percent_cutoff, sample_size + 1):
			current_hypergeometric_distribution = hypergeometric_distribution(total_size,control_peptides,sample_size,i)
			if (current_hypergeometric_distribution == None):
				current_hypergeometric_distribution = 0.0
			else:
				valid = True
			total_probability += current_hypergeometric_distribution
			if valid:
				experimental_probability = 1 - total_probability
			else:
				if shaved_peptides > control_peptides:
					experimental_probability = 0.9
				if control_peptides > shaved_peptides:
					experimental_probability = 0.1
				if control_peptides == shaved_peptides:
					experimental_probability = 0.5

	final_probability = calculate_bayesian_probability(bayesian_prior, experimental_probability)

	print str(control_peptides) + "," + str(shaved_peptides) + "," + str(bayesian_prior) + "," + str(experimental_probability) + "," +  str(final_probability)

if (len(sys.argv) < 2):
	print "Usage:", sys.argv[0], "[csv-file]"
	print "use -header argument after csv-file if the csv file contains a header line"
	sys.exit()

process_arguments(sys.argv)

try:
	csv_file = open(sys.argv[1], "rU")
except:
	print "Could not find the specified input csv file:", sys.argv[1]
	sys.exit()

line_at = 0
print_header()
for line in csv.reader(csv_file, delimiter=','):
	if line_at == 0 and header_line:
		pass
	else:
		process_line(line, line_at)
	line_at += 1