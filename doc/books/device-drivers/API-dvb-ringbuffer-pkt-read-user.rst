
.. _API-dvb-ringbuffer-pkt-read-user:

============================
dvb_ringbuffer_pkt_read_user
============================

*man dvb_ringbuffer_pkt_read_user(9)*

*4.6.0-rc1*

Read from a packet in the ringbuffer.


Synopsis
========

.. c:function:: ssize_t dvb_ringbuffer_pkt_read_user( struct dvb_ringbuffer * rbuf, size_t idx, int offset, u8 __user * buf, size_t len )

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

unlike ``dvb_ringbuffer_read``, this does NOT update the read pointer in the ringbuffer. You must use ``dvb_ringbuffer_pkt_dispose`` to mark a packet as no longer required.


Description
===========

returns Number of bytes read, or -EFAULT.
