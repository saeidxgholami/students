import mycsv
import calc



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

x = mycsv.read('bmi.csv')
print(x)