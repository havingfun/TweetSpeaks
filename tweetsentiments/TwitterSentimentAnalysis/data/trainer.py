import os
import glob
pathneg = 'neg'
for filename in os.listdir(pathneg):
    with open(pathneg+'/'+filename, 'r') as f:
		data = f.readlines()
		for line in data:
			line = line.rstrip('\n')
			fh = open("trainer.csv", "a")
			fh.write("|negative|,|")
			fh.write(line)
			fh.write("|\n")
			fh.close
pathpos = 'pos'
for filename in os.listdir(pathpos):
    with open(pathpos+'/'+filename, 'r') as f:
		data = f.readlines()
		for line in data:
			line = line.rstrip('\n')
			fh = open("trainer.csv", "a")
			fh.write("|positive|,|")
			fh.write(line)
			fh.write("|\n")
			fh.close