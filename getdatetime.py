import datetime

class getdt :
	
	def newdt(self, view) :
		now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') # 現在時刻を取得
		
		# sender.superview['datetime_text'].text = now # senderを使う場合
		view['datetime_text'].text = now # viewを渡してやる場合
		
		# csv用に辞書作成	
		now_dict = {'time':now}
		return now_dict
