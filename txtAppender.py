import os

dir = input("File directory: ")
files = os.listdir(dir)

print("\n1: " + files[0] + "\n")
print("2: " + files[1]  + "\n") 

while (True):
	title = int(input("Choose the filename pattern for the combined file? Type 1 or 2 \n"))
	if (title == 1) or (title == 2):
		title -= 1
		break

if not os.path.exists(dir + "\\comb\\"):
	os.makedirs(dir + "\\comb\\")

for x in range(0, len(files), 2):
	try:
		f1 = open(dir + "\\" + files[x], 'r')
		f2 = open(dir + "\\" + files[x+1], 'r')
		fc = open(dir + "\\comb\\" + files[x+title], 'x')
		#fc = open(dir + "\\comb" + files[x].rsplit( ".", 1 )[ 0 ] + "-comb.txt" , 'x')
		fc.write(f1.read() + '\n' + f2.read())

	finally:
		f1.close()
		f2.close()
		fc.close()

os.system("pause")
