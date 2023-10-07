pm = 1000000                  #la population de la ville marrakech
pa = 500000                   #la population de la ville agadir
c=0
while pm>pa :	
	pm=pm+50000
	pa=pa+(pa*0.08)
	c=c+1                     

print("le nombre d'anne la population de la ville agadir depassera celle de la ville marrakech est  : ",c)