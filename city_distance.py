
import numpy as np

class Distance:
	def __init__(self, first_latitude, first_longitude, second_latitude, second_longitude):
		self.first_latitude = first_latitude if isinstance(first_latitude, float) else None
		self.first_longitude = first_longitude if isinstance(first_longitude, float) else None
		self.second_latitude = second_latitude if isinstance(second_latitude, float) else None
		self.second_longitude = second_longitude if isinstance(second_longitude, float) else None

	def calculate_distance(self):
		print(self.first_longitude, self.first_latitude, self.second_latitude, self.second_longitude)
		if not (self.first_longitude and self.first_latitude and self.second_latitude and self.second_longitude):
			return 0, 'Invalid inputs', None

		r = 6371
		phi1 = np.radians(self.first_longitude)
		phi2 = np.radians(self.second_latitude)
		x = self.second_latitude - self.first_longitude
		delta_phi = np.radians(x)
		
		delta_lambda = np.radians(self.second_longitude - self.first_longitude)
		a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) *   np.sin(delta_lambda / 2)**2
		res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
		
		return 1, 'Distance calculated', np.round(res, 2)


def main():
	first_city = input("City 1: ")
	second_city = input("City 2: ")

	first_city = first_city.split(',')
	first_latitude = float(first_city[0])
	first_longitude = float(first_city[1])

	second_city = second_city.split(',')
	second_latitude = float(second_city[0])
	second_longitude = float(second_city[1])

	status, message, result = Distance(first_latitude, first_longitude, second_latitude, second_longitude).calculate_distance()
	if status == 1:
		print('Output: City 1 and City 2 are {} km apart'.format(result))


if __name__ == '__main__':
	main()

