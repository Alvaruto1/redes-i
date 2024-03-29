#!/usr/bin/env python
from scapy import all
import sys, argparse

#paquetes = all.sniff(iface="wlp3s0",count=4,filter="dst 192.168.0.17 and tcp")

#print(paquetes.summary())


def sniff(red,protocol=[], ipDes='', ipSrc='', num=10):
    destination = 'dst '+ ipDes
    source = 'src ' + ipSrc
    fil=''
    if ipDes == '':
        destination = ''
    else:
        fil += destination
    if ipSrc == '':
        source = ''
    else:
        fil += ' and ' + source
    if protocol != []:
        fil += ' and ' + " and ".join(protocol)
    pockets = all.sniff(iface=red, count=num, filter=fil)
    print("----------------------------------Frames----------------------------------")
    for i,p in enumerate(pockets):
        print("----------------------------------Frame "+str(i+1)+" ----------------------------------")
        print("Source: {}".format(p.src))
        print("Destination: {}".format(p.dst))
        print("Type: {}".format(p.type))
        print("Payload: {}".format(p.payload))
        print("Summary: {}".format(p.summary()))
        print("Datagram:")
        print(all.hexdump(p))

#sniff(red='wlp3s0',ipDes='192.168.0.17', num=2)

parser = argparse.ArgumentParser()
parser.add_argument("-r","--net", help="net name to analize",required=True)
parser.add_argument("-p","--protocols",nargs="*", help="filter by protocols")
parser.add_argument("-s","--source", help="ip source")
parser.add_argument("-d","--destination", help="ip destination")
parser.add_argument("-n","--number", help="number frames")

args = parser.parse_args()
n=10
p=[]
d=''
s=''
if args.number:
    n=int(args.number)
if args.protocols:
    p=args.protocols
if args.source:
    s=args.source
if args.destination:
    d=args.destination

sniff(red=args.net,protocol=p,ipDes=d,ipSrc=s,num=n)






