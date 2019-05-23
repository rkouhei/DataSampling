import ui, threading
import getgps, getdatetime, makecsv

# インスタンス作成
g_gps = getgps.getgps_text()
g_date = getdatetime.getdt()
m_csv = makecsv.newcsv()

def getdata(i) :
	global con_flag
	
	if con_flag :
		t = threading.Timer(i, getdata, args=[i]) # スレッドを作り、i秒ごとにデータを取得
		t.start()
		now_dict = g_date.newdt(view) # 時間取得
		gps_dict = g_gps.newgps(view) # 位置情報取得
		m_csv.writecsv(now_dict, gps_dict) # csvファイルに書き込み
		
def hmt(sender) :
	global times
	
	textfield = sender.superview['howmany']
	times = int(textfield.text)
	getdata(textfield)
	
def start(sender) :
	global con_flag
	
	interval = sender.superview['seconds_field']
	i = int(interval.text)
	con_flag = True
	getdata(i)
	
def stop(sender) :
	global con_flag
	
	con_flag = False

if __name__ == '__main__' :
	# UIの設定
	view = ui.load_view()
	view.name = 'Data Sampling'
	view.present('sheet')
