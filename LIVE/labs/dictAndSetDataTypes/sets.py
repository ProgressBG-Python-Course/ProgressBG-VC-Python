students = {
	"ivan": 5.50,
	"alex": 3.50,
	"maria": 5.50,
	"georgy": 5.50,
}


for k,v in students.items():
	if v > 4.50:
		print( "{} - {}".format(k, v) )