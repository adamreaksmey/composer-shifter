import http.client as httplib

def connect(url="www.geeksforgeeks.org",timeout=3):
	connection = httplib.HTTPConnection(url, timeout=timeout)
	try:
		connection.request("HEAD", "/")
		connection.close()
		print("Connection detected!")
		return True
	except Exception as exep:
		print(exep)
		return False


connect("www.geeksforgeeks.org", 3)
