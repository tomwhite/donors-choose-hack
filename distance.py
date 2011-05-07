# donors choose local schools

import csv  
from collections import defaultdict

from zips import Zip_Codes

#print Zip_Codes().get_distance('99999', '58368')

project_to_school_zip={}
with open('donorschoose-org-1apr2011-v1-projects.csv', 'rb') as f:
  reader = csv.reader(f)
  fields = reader.next()
  #print fields
  for row in reader:
    project_id=row[0]
    school_zip=row[8]
    project_to_school_zip[project_id] = school_zip

#print project_to_school_zip

#donations=[{"1":{"project_id":"e2d470602cd7e0092b9bac71899ff480", "donor_zip":"19120"}}]]
donations=[]
with open('donorschoose-org-1apr2011-v1-donations.csv', 'rb') as f:
  reader = csv.reader(f)
  fields = reader.next()
  for row in reader:
    project_id = row[1]
    donor_zip = row[6]
    donations.append({"project_id":project_id, "donor_zip":donor_zip})

#print donor_to_project

zip = Zip_Codes()
distances = defaultdict(int)
for donation in donations:
  school_zip = project_to_school_zip[donation["project_id"]]
  donor_zip = donation["donor_zip"]
  distances[int(zip.get_distance(school_zip, donor_zip))] += 1

print distances