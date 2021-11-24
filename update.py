import pymysql


# 修改信息(任务)
def update_into1 (message,id ):
	conn = pymysql.connect ( host='localhost', user='root', password='qwe1234..', db='user', port=3306, charset='utf8' )

	cur = conn.cursor ( )

	sql = "update users set message='%s' where id=%d"%(message,id)

	cur.execute ( sql )

	conn.commit ( )

	cur.close ( )

	conn.close ( )

#修改信息(签到)
def update_into2 (day_count,id ):
	conn = pymysql.connect ( host='localhost', user='root', password='qwe1234..', db='user', port=3306, charset='utf8' )

	cur = conn.cursor ( )

	sql = "update days set day_count=%d where id=%d"%(day_count,id)

	cur.execute ( sql )

	conn.commit ( )

	cur.close ( )

	conn.close ( )

