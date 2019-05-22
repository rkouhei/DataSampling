import location

class getgps_text :
	
	def newgps(self, view) :
		# GPSデータを取得
		location.start_updates()
		gps = location.get_location()
		location.stop_updates()
		
		# visualize all GPSdata
		#gps_text = ''
		#for g in gps :
		#	gps_text = gps_text + str(g) + ':' + str(gps[g]) + '\n'
		#label.text = gps_text
		
		# senderを使う場合
		#sender.superview['alti_text'].text = str(gps['altitude']) # 高度
		#sender.superview['longi_text'].text = str(gps['longitude']) # 経度
		#sender.superview['lati_text'].text = str(gps['latitude']) # 緯度
		
		view['alti_text'].text = str(gps['altitude']) # 高度
		view['longi_text'].text = str(gps['longitude']) # 経度
		view['lati_text'].text = str(gps['latitude']) # 緯度
