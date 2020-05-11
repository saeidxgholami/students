import csv


def read(filename):
	with open(filename) as f:
		data = csv.reader(f, skipinitialspace=True)
		return list(data)



def read_dict(filename):
	with open(filename) as f:
		data = csv.DictReader(f, skipinitialspace=True)
		return list(data)



# row is a list
def write(filename, rows):
	with open(filename, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(rows)



