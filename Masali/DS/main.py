
from collections import Counter

import matplotlib.pyplot as plt 

import mycsv
import calc



def create_bmi():
	people = mycsv.read_dict('biostats.csv')
	data = []
	for person in people:
		name = person.get('Name')
		height = calc.meter(int(person.get('Height (in)')))
		weight = calc.kg(int(person.get('Weight (lbs)')))
		bmi = calc.bmi(height, weight)
		bmi_status = calc.bmi_status(bmi)


		data.append([name, height, weight, bmi, bmi_status])

	# create csv with desired fields
	header = ["Name", "Height(M)", "Weight(KG)", "BMI", "BMI_Status"]
	data.insert(0, header)
	mycsv.write('bmi.csv', data)



def draw_char(x, y):
	fig, axs = plt.subplots()
	axs.bar(x, y)
	fig.suptitle('BMI Status')
	plt.show()

def main():
	bmi_status_list = []
	
	data = mycsv.read_dict('bmi.csv')
	for record in data:
		bmi_status_list.append(record.get('BMI_Status'))

	bmi_status_count = Counter(bmi_status_list) 
	bmi_status_total = sum(bmi_status_count.values())
	bmi_status_per = {}

	for bmi_name, bmi_val in bmi_status_count.items():
		bmi_status_per[bmi_name] = round((100 / bmi_status_total) * bmi_val)

	x = bmi_status_per.keys()
	y = bmi_status_per.values()

	draw_char(x, y)

main()