import csv, os
from datetime import date

class newcsv :
	
	def __init__(self) :
		global  f_name
		 
		now = date.today()
		f_name = 'log_' + str(now) + '.csv'
		
		if not os.path.isfile(f_name) :
			with open(f_name, mode = 'w') as f :
				writer = csv.writer(f)
				writer.writerow(['time', 'altitude', 'longitude', 'latitude'])
			
	def writecsv(self, now_dict, gps_dict) :
		global  f_name
		
		now_dict.update(gps_dict)
		data_rows = []
		data_rows.append(now_dict)
		parameters = ['time', 'altitude', 'longitude', 'latitude']
		header = dict([(val, val) for val in parameters])
		
		with open(f_name, mode = 'a') as f :
			writer = csv.DictWriter(f, parameters, extrasaction = 'ignore')
			writer.writerows(data_rows)
		
if __name__ == '__main__' :
	a = newcsv()
