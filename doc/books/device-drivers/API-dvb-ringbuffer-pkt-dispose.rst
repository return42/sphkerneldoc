
.. _API-dvb-ringbuffer-pkt-dispose:

==========================
dvb_ringbuffer_pkt_dispose
==========================

*man dvb_ringbuffer_pkt_dispose(9)*

*4.6.0-rc1*

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
