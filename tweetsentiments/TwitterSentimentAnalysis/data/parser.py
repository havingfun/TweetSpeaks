fh = open('words.txt','r')
data = fh.readlines()
i=0
for line in data:
	cat = line.split(" ")
	word = cat[2].split("=")[1]
	polarity = cat[5].split("=")[1].rstrip("\n")
	if(polarity=="positive"):
		fx = open('poss.txt','a')
		fx.write(word + ' ')
	elif(polarity=="negative"):
		fx = open('negg.txt','a')
		fx.write(word + ' ')