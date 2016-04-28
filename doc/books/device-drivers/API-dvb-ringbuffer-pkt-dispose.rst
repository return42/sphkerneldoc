.. -*- coding: utf-8; mode: rst -*-

.. _API-dvb-ringbuffer-pkt-dispose:

==========================
dvb_ringbuffer_pkt_dispose
==========================

*man dvb_ringbuffer_pkt_dispose(9)*

*4.6.0-rc5*

Dispose of a packet in the ring buffer.


Synopsis
========

.. c:function:: void dvb_ringbuffer_pkt_dispose( struct dvb_ringbuffer * rbuf, size_t idx )

Arguments
=========

``rbuf``
    Ring buffer concerned.

``idx``
    Packet index as returned by ``dvb_ringbuffer_pkt_next``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
