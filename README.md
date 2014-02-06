## Repository for the Cell Shaving program.

This program calculates the probability of a protein being surface-exposed based on the number of peptides identified by cell shaving proteomics utilising a false positive control strategy. It will calculate a probability based purely on the number of peptides found in the shaved fraction “shaved peptides” and on the number of peptides found in the control fraction “control peptides”. Additionally a final adjusted probability integrating prior bioinformatic data (later referred to as the Bayesian) can be calculated provided the probability the protein is surface-exposed (typically by software such as PSORTb, LocateP, SURFG+, etc.

The program takes as an argument the comma separated values (csv) file as input, and outputs a csv file containing the results.  An optional -header argument can be provided that makes the program ignore the first line of the csv file (used if the file contains a header line).

The csv file should contain three columns.  The first is the number of Control Peptides in the sample, the second is the number of Shaved Peptides in the sample, and the third is the Bayesian prior you have calculated for the sample.

The output will contain 5 columns, the first three as in the input file, plus the Calculated Experimental Probability, as well as the Calculated Bayesian Probability from the prior and the experimental probability.

Examples of these files can be seen in example1.csv and example2.csv.


## Windows

First, download https://github.com/mehwoot/cellshaving/raw/master/cell_shaving.zip and unzip the file.

You should now have a folder called "cellshaving".

Open command prompt and change directory to the upzipped folder

```cd cellshaving```

You should now be able to run the program by

```process.exe example1.csv -header```

You can write the output of the program to a file like so:

```process.exe example1.csv -header > output.csv```


## OSX / Linux

First ensure you have python installed.

```python --version```

Should output "Python 2.7.5" or something similiar.  If you do not have python installed, download it from http://python.org/download/

Now, download the code by running

```
git clone git@github.com:mehwoot/cellshaving.git
cd cellshaving
```

You should now be able to run the program by

```python process.py example1.csv -header```

You can write the output of the program to a file like so:

```python process.py example1.csv -header > output.csv```

## Help

Any questions about the operation of the program can be directed to robinson.gareth@gmail.com.  Any questions about the scientific implications should be directed to xx
