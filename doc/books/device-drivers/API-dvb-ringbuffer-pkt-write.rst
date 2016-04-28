.. -*- coding: utf-8; mode: rst -*-

.. _API-dvb-ringbuffer-pkt-write:

========================
dvb_ringbuffer_pkt_write
========================

*man dvb_ringbuffer_pkt_write(9)*

*4.6.0-rc5*

Write a packet into the ringbuffer.


Synopsis
========

.. c:function:: ssize_t dvb_ringbuffer_pkt_write( struct dvb_ringbuffer * rbuf, u8 * buf, size_t len )

Arguments
=========

``rbuf``
    Ringbuffer to write to.

``buf``
    Buffer to write.

``len``
    Length of buffer (currently limited to 65535 bytes max). returns
    Number of bytes written, or -EFAULT, -ENOMEM, -EVINAL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
