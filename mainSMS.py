#!/usr/bin/python

import smsIO
import sms_ssh
import sms_tolk

#Function gets called from smsIO
#by the handler when a GET request has been made. 
def incoming_sms(query) :
	
	#Saves destination phone number
	destination = query[0]
	#Saves source phone number
	originator = query[1]

	#Replaces URL encoded space with actual space.
	r_text = query[2].replace('%20', ' ')
	#Splits the text at '!', (Does IOS use ! anywhere?)
	cmd_msg = r_text.split('!')
	cmd = cmd_msg[1]

	#Takes the host receiver portion of the list.
	cmd_recv_host = cmd_msg[0].replace('text=', '')
	complete_cmd_string = sms_tolk.parse(cmd)

	#Sends a command to a host via SSH and returns the output
	recv_host_output = sms_ssh.ssh_connect(cmd_recv_host, complete_cmd_string)
	
	#SendSMS, user n passw must be passed data with a '=' 
	#Otherwise they are None
	#Last step in the full communication process
	SendSMS(originator, recv_host_output, user = '', passw = '')

if __name__ == "__main__" :
	smsIO.RunServerHTTP(80)
