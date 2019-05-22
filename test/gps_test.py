# -*- coding:utf-8 -*-

import ui, location, csv, datetime, time

def New(sender) :
	label = sender.superview['label1']
	now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') # get realtime
	
	# get GPSdata
	location.start_updates() # updata GPSdata 	
	gps = location.get_location() # get GPSdata
	location.stop_updates() # stop updating GPSdata
	
	# visualize GPSdata
	gps_text = ''
	for g in gps :
		gps_text = gps_text + str(g) + ':' + str(gps[g]) + '\n'
		#print(g)
		#print(gps[g])
	label.text = now + '\n' + gps_text # Substitute GPSdata for UITextView
	
	# Edit GPS data and savd in csv file
	gps_dict = {'time':now} # Type dictionary
	gps_dict.update(gps) # Enter acquisition time first, then add GPS data
	
	# Create header for csv file
	gps_rows = []
	gps_rows.append(gps_dict)
	parameters = ['time', 'latitude', 'longitude', 'altitude', 'timestamp', 'horizontal_accuracy', 'vertical_accuracy', 'speed', 'course']
	header = dict([(val, val) for val in parameters])
	
	# Open csv file and write GPS dictionary data
	with open('gps_log.csv', mode = 'w') as f :
		writer = csv.DictWriter(f, parameters, extrasaction = 'ignore')
		writer.writerows(gps_rows)
		
def Add(sender) :
	label = sender.superview['label1']
	now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') # get realtime
	
	# get GPSdata
	location.start_updates() # updata GPSdata 	
	gps = location.get_location() # get GPSdata
	location.stop_updates() # stop updating GPSdata
	
	# visualize GPSdata
	gps_text = ''
	for g in gps :
		gps_text = gps_text + str(g) + ':' + str(gps[g]) + '\n'
	label.text = now + '\n' + gps_text # Substitute GPSdata for UITextView
	
	# Edit GPS data and savd in csv file
	gps_dict = {'time':now} # Type dictionary
	gps_dict.update(gps) # Enter acquisition time first, then add GPS data
	
	# Create header for csv file
	gps_rows = []
	gps_rows.append(gps_dict)
	parameters = ['time', 'latitude', 'longitude', 'altitude', 'timestamp', 'horizontal_accuracy', 'vertical_accuracy', 'speed', 'course']
	header = dict([(val, val) for val in parameters])
	
	# Open csv file and write GPS dictionary data
	with open('gps_log.csv', mode = 'a') as f :
		writer = csv.DictWriter(f, parameters, extrasaction = 'ignore')
		writer.writerows(gps_rows)
		
v = ui.load_view()
v.present('sheet')
