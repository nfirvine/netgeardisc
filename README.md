netgeardisc
===========

Discovers Netgear swtiches.

Broadcasts a magic packet that Netgear switches listen for in a loop.  They
reply with a packet using their management IP.  These packets match the
following Wireshark query::

    udp.srcport == 64515
