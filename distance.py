# Calculate the distribution of distances between schools and donors for all
# donations

import csv  
from collections import defaultdict

from zips import Zip_Codes

project_to_school_zip={}
with open('donorschoose-org-1apr2011-v1-projects.csv', 'rb') as f:
  reader = csv.reader(f)
  fields = reader.next()
  for row in reader:
    project_id=row[0]
    school_zip=row[8]
    project_to_school_zip[project_id] = school_zip

zip = Zip_Codes()
distances = defaultdict(int)
total=0
used=0
no_donor_zipcode=0
with open('donorschoose-org-1apr2011-v1-donations.csv', 'rb') as f:
  reader = csv.reader(f)
  fields = reader.next()
  for row in reader:
    project_id = row[1]
    total+=1
    school_zip = project_to_school_zip[project_id]
    partial_donor_zip = row[6]
    if len(partial_donor_zip) == 0:
      no_donor_zipcode+=1
      continue
    donor_zip_prefix = partial_donor_zip[0:3]
    if school_zip.startswith(donor_zip_prefix):
      distances[0] += 1
      used+=1
      continue
    try:
      donor_zip = zip.get_zip(donor_zip_prefix)
    except:
      print "Can't find zip prefix", donor_zip_prefix
    try:
      distances[int(zip.get_distance(school_zip, donor_zip))] += 1
      used+=1
    except:
      print school_zip, donor_zip

print "No donor zipcode: ", no_donor_zipcode
print "Used: ", used
print "Used %: ", 100*used/total
print "Total: ", total

# Emit raw counts for statistical analysis
with open('raw_counts.txt', 'w') as f:
  for distance,count in distances.items():
    for i in range(1, count):
      f.write("%s\n" % distance)

# Emit bucketed counts for plotting
with open('counts.txt', 'w') as f:
  for distance,count in distances.items():
    f.write("%s %s\n" % (distance, count))
