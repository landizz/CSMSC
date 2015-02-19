#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from urlparse import urlparse 
import httplib

#!OBS! Everything is to be called from a other file, nothing is called from within. You only call functions, for which there are two so far.
#1. RunServerHTTP(port), which runs a HTTP server on specified port, handles GET requests and sends them to the tolk functions.
#2. SendSMS(username,password,dest,text), which sends a HTTPS GET request when received (SMS Gateway) will send a SMS to whoever we specified it to.


#Class for BaseHTTPRequestHandler, receives HTTP SMS paths and passes them to be processed.
class GetRequestHandler(BaseHTTPRequestHandler) :
	
	#This is specifically for GET requests
	def do_GET(self) : 
		#Import main to call a function everytime a 'GET' request is made.
		import mainSMS
		print "We got a GET"
		#Input the requested GET path of the url to a variable
		get_path = urlparse(self.path)
		#Takes the query part of the string and splits it.
		query_request = get_path.query.split('&')
		#Calls the function which notifies the arrival of a SMS
		mainSMS.incoming_sms(query_request)

#RunServerHTTP start httpd and reports to the handler (GetRequestHandler)
def RunServerHTTP(port) :
	
	#Makes 'httpd' a object, specifices ip:port and the request handler.
	httpd = HTTPServer(('193.10.203.249', port), GetRequestHandler)
	try :	
		#Starts HTTP server to receive SMS from SMS Gateway
		print "Listening on port", port
		httpd.serve_forever()

	#CTRL-C to shutdown HTTP server and the script for the moment.
	except :	
		print "Server shutdown..."
		httpd.server_close()


#Function for sending SMS data back to the SMS gateway for handling
def SendSMS(recv, msg, user = None, passw = None) :
	
	#Specifices settings for the SMS Gateway. NOTE: Can be modified and add other settings, check SMS Gateway API
	php_spec = "sms.php?"
	charset = "charset=UTF-8"
		
	#The URL to connect to
	Gateway_url = "se-1.cellsynt.net"

	#Adds the data to the their respective attribute of the HTTP path.
	username = 'username=' + user
	password = 'password=' + passw
	dest = 'destination=' + recv
	text = 'text=' + msg.replace(' ', '%20')

	
	#Makes the PATH for the GET message
	dest_HTTP_PATH = '/' + php_spec + username + '&' + password + '&' + dest + '&' + charset + '&' + text
	print dest_HTTP_PATH	
	#Working HTTP GET, 'Gateway_url' is the url from which you want to use GET on. NOTE: Tested against 'https://docs.python.org/2/'
	http_connection = httplib.HTTPConnection(Gateway_url)
	
	#Calling a function of the http connection object, from which we use GET with the specified path('dest_HTTP_PATH')
	http_connection.request('GET', dest_HTTP_PATH)

	#Gets the response, used temporarly for testing. Might be useful for checking status of the HTTP receiver. 
	Connection_response = http_connection.getresponse()
	print Connection_response.status, Connection_response.msg
