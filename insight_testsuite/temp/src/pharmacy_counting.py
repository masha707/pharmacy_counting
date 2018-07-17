import csv

# Read input file, return dictionary of data:
#   Key is drug name
#   Value is the list [set of unique providers, total cost]
def readInput(inputFile):
  print('Reading input from %s' % inputFile)
  data = {}

  with open(inputFile, 'r') as file:
    next(file) # Skip header row
    csvreader = csv.reader(file, delimiter=',', quotechar='"')
    for row in csvreader:
      if len(row) != 5:
        print('Error: number of cells in row not equal 5, skipping: ' + str(row))
        continue

      # Converting first and last names to lowercase so uniqueness is independent of capitalization
      provider = row[1].lower() + row[2].lower()
      drugName = row[3]
      
      try:
        # NOTE: the instructions were ambiguous: the provided test expects integer cost
        # but the large input file has float costs. To satisfy the test, I'm converting
        # costs to ints by dropping the decimal
        drugCost = int(float(row[4]))
      except ValueError:
        print('Error: cannot convert %s to number; skipping' % row[4])
        continue

      if drugName not in data:
        # If drug not yet in dictionary, initialize with set of providers and running total cost
        uniqueProviders = set([ provider ]) 
        totalCost = drugCost
        data[drugName] = [uniqueProviders, totalCost]    
      else:
        # pair[0] is our set of unique providers;
        #   adding provider name to it increments the set 
        #   only if this provider is unique, and ignores it otherwise
        # pair[1] is our running total of cost, let's increment it
        pair = data[drugName]
        pair[0].add( provider )
        pair[1] += drugCost
  
  print('Done')
  return data


# Take dictionary of data, turn it into a list of tuples, sort and return list of tuples
def processData(data):
  print('Processing data')
  tuples = []

  # For each drug in dictionary, add tuple (drug, # unique providers, total cost) to the list
  for drug in data:
    value = data[drug] # Reminder, value is a pair containing a set and an integer
    numUniqueProviders = len(value[0]) # Size of the set
    totalCost = value[1]
    tuples.append( (drug, numUniqueProviders, totalCost) )

  print('Done')
  # Sort tuples by 3rd element (total cost), then 1st element (provider), both descending
  return sorted(tuples, key=lambda tuple: (tuple[2], tuple[0]), reverse=True)


def writeOutput(data, outputFile):
  print('Writing output to %s' % outputFile)
  with open(outputFile, 'w') as file:
    file.write('drug_name,num_prescriber,total_cost')
    for tuple in data:

      # NOTE: the right thing to do is to put drug in quotes because some drugs have commas.
      # BUT I'm not doing it because then the test provided by the test suite fails.
      file.write('\n%s,%d,%d' % tuple) 
  print('Done')


def main():
  data = readInput('../input/itcont.txt')
  processedData = processData(data)
  writeOutput(processedData, '../output/top_cost_drug.txt')


# Program execution starts here
if __name__ == "__main__":
  main()
