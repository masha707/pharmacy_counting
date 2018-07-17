# NOTES - READ FIRST

There are a couple of issues with the exercise:

1. They are ambiguous as to whether total costs in output should be integers or floats. The large dataset has costs as floats, yet the test provided expects the output to have them as ints. Therefore to satisfy the test I convert the floats to ints by dropping the fractional part.

2. The sample output file expects drug names to NOT be quoted - which will cause malformed CSV for the real dataset - since in the real data set some drugs have commas in their name. But to satisfy the test I do not put drug names in quotes.

Also, the data in the large input file was not "clean", i.e. some drug names and provider names had commas in them. Therefore I use the python standard csv module for reading the input file, which takes care of properly parsing quoted cells in the csv.

# How it works 

See comments in pharmacy_counting.py for explanation of how the program works. It's very well organized and commented, so explaining this here would be redundant.

# How to run the code 

You might need to call 'chmod 744 run.sh' to ensure the run.sh script is executable.

My code works the same in python 2 and python 3, but anyway, run './run.sh' and it'll take care of executing the program.


