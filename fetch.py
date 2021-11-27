import pymysql


# 获取某一列信息(任务)
@app.route('/fetch_into1',methods=['POST'])
def fetch_into1 (id ):
	conn = pymysql.connect ( host='localhost', user='root', password='qwe1234..', db='user', port=3306, charset='utf8' )

	cur = conn.cursor ( )

	sql = "select * from users"

	cur.execute ( sql )

	conn.commit ( )

	data = cur.fetchall ( )

	for item in data:

		# 将ID号的输入的任务信息 输出

		if item [ 1 ] == id:

			return  jsonipy( item [ 0 ] )

# 获取某一列信息(签到)
@app.route('/fetch_into2',methods=['POST'])
def fetch_into2 (id ):
	conn = pymysql.connect ( host='localhost', user='root', password='qwe1234..', db='user', port=3306, charset='utf8' )

	cur = conn.cursor ( )

	sql = "select * from days"

	cur.execute ( sql )

	conn.commit ( )

	data = cur.fetchall ( )

	for item in data:

		# 将ID号的输入的任务信息 输出

		if item [ 1 ] == id:

			return jsonify( item [ 0 ] )
