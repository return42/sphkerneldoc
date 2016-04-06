
.. _API-dvb-ringbuffer-pkt-read:

=======================
dvb_ringbuffer_pkt_read
=======================

*man dvb_ringbuffer_pkt_read(9)*

*4.6.0-rc1*

Read from a packet in the ringbuffer.


Synopsis
========

.. c:function:: ssize_t dvb_ringbuffer_pkt_read( struct dvb_ringbuffer * rbuf, size_t idx, int offset, u8 * buf, size_t len )

Arguments
=========

``rbuf``
    Ringbuffer concerned.

``idx``
    Packet index as returned by ``dvb_ringbuffer_pkt_next``.

``offset``
    Offset into packet to read from.

``buf``
    Destination buffer for data.

``len``
    Size of destination buffer.


Note
====

unlike ``dvb_ringbuffer_read_user``, this DOES update the read pointer in the ringbuffer.


Description
===========

returns Number of bytes read, or -EFAULT.
