import csv  
from collections import defaultdict

total=0
categories=defaultdict(int)
with open('donorschoose-org-1apr2011-v1-projects.csv', 'rb') as f:
  reader = csv.reader(f)
  fields = reader.next()
  #print fields
  for row in reader:
    total += 1
    categories[row[27]] += 1

print "Total projects:", total
print "Minimal poverty: %s (%s%%)" % (categories["minimal"], 100*categories["minimal"]/total)
print "Low poverty: %s (%s%%)" % (categories["low"], 100*categories["low"]/total)
print "High poverty: %s (%s%%)" % (categories["high"], 100*categories["high"]/total)
print "Unknown poverty: %s (%s%%)" % (categories["unknown"], 100*categories["unknown"]/total)
