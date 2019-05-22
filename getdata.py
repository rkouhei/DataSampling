import ui, threading
import getgps, getdatetime

# インスタンス作成
g_gps = getgps.getgps_text()
g_date = getdatetime.getdt()

def getdata(i) :
	global con_flag
	
	if con_flag :
		t = threading.Timer(i, getdata, args=[i])
		t.start()
		g_date.newdt(view) # 時間取得
		g_gps.newgps(view) # 位置情報取得
		
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
