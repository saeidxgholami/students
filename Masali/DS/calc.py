def bmi(height, weight):
	return round(weight / height ** 2, 2)


def meter(inch):
	return round(inch / 39.37, 2)


def kg(pound):
	return round(pound / 2.205, 2)


def bmi_status(bmi):
	if bmi <= 18.5:
		return 'Underweight'
	elif bmi > 18.5 and bmi < 24.9:
		return 'Normal'
	else:
		return 'Overweight'