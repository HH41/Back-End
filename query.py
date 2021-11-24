import pymysql


# （任务）查询操作
def select_1( ):
	conn = pymysql.connect ( host='localhost', user='root', password='qwe1234..', db='user', port=3306, charset='utf8' )

	cur = conn.cursor ( )

	sql = "select * from users"

	cur.execute ( sql )

	conn.commit ( )

	data = cur.fetchall ( )

	for item in data:

		print ( item )

	cur.close ( )

	conn.close ( )

#（签到）查询操作
def select_2 ( ):
	conn = pymysql.connect ( host='localhost', user='root', password='qwe1234..', db='user', port=3306, charset='utf8' )

	cur = conn.cursor ( )

	sql = "select * from days"

	cur.execute ( sql )

	conn.commit ( )

	data = cur.fetchall ( )

	for item in data:

		print ( item )

	cur.close ( )

	conn.close ( )
