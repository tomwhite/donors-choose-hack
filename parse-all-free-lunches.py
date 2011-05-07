import csv
from collections import defaultdict

def poverty_category(num_free_or_reduced_lunches, total_enrollment):
  proportion = 100*num_free_or_reduced_lunches/total_enrollment
  if proportion < 10:
    return "minimal"
  elif 10 <= proportion <= 39:
    return "low"
  else:
    return "high"

total=0
categories=defaultdict(int)
with open('Schools.Mapped.2010_08_20.csv', 'rb') as f:
  reader = csv.reader(f)
  fields = reader.next()
  #print fields
  for row in reader:
    total += 1
    try:
      num_free_or_reduced_lunches = int(row[41])
      total_enrollment = int(row[143])
      #print poverty_category(num_free_or_reduced_lunches, total_enrollment)
      categories[poverty_category(num_free_or_reduced_lunches, total_enrollment)] += 1
    except:
      categories["unknown"] += 1
print "Total schools:", total
print "Minimal poverty: %s (%s%%)" % (categories["minimal"], 100*categories["minimal"]/total)
print "Low poverty: %s (%s%%)" % (categories["low"], 100*categories["low"]/total)
print "High poverty: %s (%s%%)" % (categories["high"], 100*categories["high"]/total)
print "Unknown poverty: %s (%s%%)" % (categories["unknown"], 100*categories["unknown"]/total)
