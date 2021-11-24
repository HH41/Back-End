import pymysql


# 删除操作
def drop_into ( ):
	conn = pymysql.connect ( host='localhost', user='root', password='qwe1234..', db='user', port=3306, charset='utf8' )

	cur = conn.cursor ( )

	sql = "truncate table users" # 删除users表中的所有数据

	cur.execute ( sql )

	conn.commit ( )

	cur.close ( )

	conn.close ( )
