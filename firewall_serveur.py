import socket
import logging
import ipaddress

logging.basicConfig(filename='firewall_socket.log',level=logging.INFO)

class Firewall_serveur:
    def __init__(self,host='127.0.0.1',port=65432):
        self.host=host
        self.port=port
        self.rules=[{'action','allow','protocol':'TCP','port':80,'ip_adress':"192.168.1.0/24"},
                    {'action','block','protocol':'TCP','port':22,'ip_adress':"10.0.0.0/8"},
                    {'action','allow''protocol':'ICMP'}]
        self.statisics={'allow':0,'block':0,'protocols':{},'ports':{}}
