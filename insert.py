import pymysql


# 插入操作（任务输入）
def insert_A (message,id ):
	conn = pymysql.connect ( host='localhost', user='root', password='qwe1234..', db='user', port=3306, charset='utf8' )

	cur = conn.cursor ( )

	sql_insert = "insert into users values ('%s', '%d')"%(message,id)

	cur.execute ( sql_insert )

	conn.commit ( )

	cur.close ( )

	conn.close ( )


# 带信息查重的插入操作（任务输入）
def insert_B ( messgae, id):
	conn = pymysql.connect ( host='localhost', user='root', password='qwe1234..', db='user', port=3306, charset='utf8' )

	cur = conn.cursor ( )

	sql_insert = "insert into users values ('%s', %d)" % (message,id)

	sql_query = "select count(*) from users where id = '%s'" % (id)

	cur.execute ( sql_query )

	conn.commit ( )

	data = cur.fetchone ( )

	if data [ 0 ] == 1:

		print ( "信息已存在, 不可重复插入" )

	else:

		cur.execute ( sql_insert )

		conn.commit ( )

	cur.close ( )

	conn.close ( )



#天数签到为1，未签到为0

# 插入操作（签到输入）
def insert_c (day_count,id ):
	conn = pymysql.connect ( host='localhost', user='root', password='qwe1234..', db='user', port=3306, charset='utf8' )

	cur = conn.cursor ( )

	sql_insert = "insert into days values ('%d', '%d')"%(day_count,id)

	cur.execute ( sql_insert )

	conn.commit ( )

	cur.close ( )

	conn.close ( )


# 带信息查重的插入操作(签到输入)
def insert_D ( day_count, id):
	conn = pymysql.connect ( host='localhost', user='root', password='qwe1234..', db='user', port=3306, charset='utf8' )

	cur = conn.cursor ( )

	sql_insert = "insert into days values ('%d', %d)" % (message,id)

	sql_query = "select count(*) from days where id = '%d'" % (id)

	cur.execute ( sql_query )

	conn.commit ( )

	data = cur.fetchone ( )

	if data [ 0 ] == 1:

		print ( "信息已存在, 不可重复插入" )

	else:

		cur.execute ( sql_insert )

		conn.commit ( )

	cur.close ( )

	conn.close ( )
