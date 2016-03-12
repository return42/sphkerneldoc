.. -*- coding: utf-8; mode: rst -*-

================
dvb_ringbuffer.h
================



.. _xref_dvb_ringbuffer_pkt_write:

dvb_ringbuffer_pkt_write
========================

.. c:function:: ssize_t dvb_ringbuffer_pkt_write (struct dvb_ringbuffer * rbuf, u8 * buf, size_t len)

    Write a packet into the ringbuffer.

    :param struct dvb_ringbuffer * rbuf:
        Ringbuffer to write to.

    :param u8 * buf:
        Buffer to write.

    :param size_t len:
        Length of buffer (currently limited to 65535 bytes max).
        returns Number of bytes written, or -EFAULT, -ENOMEM, -EVINAL.




.. _xref_dvb_ringbuffer_pkt_read_user:

dvb_ringbuffer_pkt_read_user
============================

.. c:function:: ssize_t dvb_ringbuffer_pkt_read_user (struct dvb_ringbuffer * rbuf, size_t idx, int offset, u8 __user * buf, size_t len)

    Read from a packet in the ringbuffer.

    :param struct dvb_ringbuffer * rbuf:
        Ringbuffer concerned.

    :param size_t idx:
        Packet index as returned by :c:func:`dvb_ringbuffer_pkt_next`.

    :param int offset:
        Offset into packet to read from.

    :param u8 __user * buf:
        Destination buffer for data.

    :param size_t len:
        Size of destination buffer.



Note
----

unlike :c:func:`dvb_ringbuffer_read`, this does NOT update the read pointer
in the ringbuffer. You must use :c:func:`dvb_ringbuffer_pkt_dispose` to mark a
packet as no longer required.



Description
-----------

returns Number of bytes read, or -EFAULT.




.. _xref_dvb_ringbuffer_pkt_read:

dvb_ringbuffer_pkt_read
=======================

.. c:function:: ssize_t dvb_ringbuffer_pkt_read (struct dvb_ringbuffer * rbuf, size_t idx, int offset, u8 * buf, size_t len)

    Read from a packet in the ringbuffer.

    :param struct dvb_ringbuffer * rbuf:
        Ringbuffer concerned.

    :param size_t idx:
        Packet index as returned by :c:func:`dvb_ringbuffer_pkt_next`.

    :param int offset:
        Offset into packet to read from.

    :param u8 * buf:
        Destination buffer for data.

    :param size_t len:
        Size of destination buffer.



Note
----

unlike :c:func:`dvb_ringbuffer_read_user`, this DOES update the read pointer
in the ringbuffer.



Description
-----------

returns Number of bytes read, or -EFAULT.




.. _xref_dvb_ringbuffer_pkt_dispose:

dvb_ringbuffer_pkt_dispose
==========================

.. c:function:: void dvb_ringbuffer_pkt_dispose (struct dvb_ringbuffer * rbuf, size_t idx)

    Dispose of a packet in the ring buffer.

    :param struct dvb_ringbuffer * rbuf:
        Ring buffer concerned.

    :param size_t idx:
        Packet index as returned by :c:func:`dvb_ringbuffer_pkt_next`.




.. _xref_dvb_ringbuffer_pkt_next:

dvb_ringbuffer_pkt_next
=======================

.. c:function:: ssize_t dvb_ringbuffer_pkt_next (struct dvb_ringbuffer * rbuf, size_t idx, size_t * pktlen)

    Get the index of the next packet in a ringbuffer.

    :param struct dvb_ringbuffer * rbuf:
        Ringbuffer concerned.

    :param size_t idx:
        Previous packet index, or -1 to return the first packet index.

    :param size_t * pktlen:
        On success, will be updated to contain the length of the packet in bytes.
        returns Packet index (if >=0), or -1 if no packets available.


