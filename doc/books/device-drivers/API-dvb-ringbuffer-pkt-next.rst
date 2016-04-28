.. -*- coding: utf-8; mode: rst -*-

.. _API-dvb-ringbuffer-pkt-next:

=======================
dvb_ringbuffer_pkt_next
=======================

*man dvb_ringbuffer_pkt_next(9)*

*4.6.0-rc5*

Get the index of the next packet in a ringbuffer.


Synopsis
========

.. c:function:: ssize_t dvb_ringbuffer_pkt_next( struct dvb_ringbuffer * rbuf, size_t idx, size_t * pktlen )

Arguments
=========

``rbuf``
    Ringbuffer concerned.

``idx``
    Previous packet index, or -1 to return the first packet index.

``pktlen``
    On success, will be updated to contain the length of the packet in
    bytes. returns Packet index (if >=0), or -1 if no packets available.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
