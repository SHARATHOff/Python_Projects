import csv
fp = open(r'C:\Users\SHARATH BALAN\Documents\Programming\Python_Projects\shet.csv','w')

fps = csv.writer(fp)
fps.writerows(['hai','18','sharath',['hai','18','sharath'],['hai','18','sharath'],['hai','18','sharath']])
fp.close()

