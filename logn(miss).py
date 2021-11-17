import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar

LOGIN_URL = r'https://passport-api.csdn.net/v1/register/pc/wxapplets/checkLogin'  # 登录csdn的URL
get_url = 'https://i.csdn.net/#/user-center/collection-list?type=1'  # 利用cookie请求访问另一个网址

values = {'IDToken1': '201106******', 'IDToken2': '***********'}
postdata = urllib.parse.urlencode ( values ).encode ( )
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

cookie_filename = 'cookie_jar.txt'
cookie_jar = http.cookiejar.MozillaCookieJar ( cookie_filename )
handler = urllib.request.HTTPCookieProcessor ( cookie_jar )
opener = urllib.request.build_opener ( handler )

request = urllib.request.Request ( LOGIN_URL, postdata, headers )
try:
	response = opener.open ( request )
# print(response.read().decode())
except urllib.error.URLError as e:
	print ( e.code, ':', e.reason )

cookie_jar.save ( ignore_discard=True, ignore_expires=True )  # 保存cookie到cookie.txt中
for item in cookie_jar:
	print ( 'Name = ' + item.name )
	print ( 'Value = ' + item.value )

get_request = urllib.request.Request ( get_url, headers=headers )
get_response = opener.open ( get_request )
print ( get_response.read ( ).decode ( ) )
