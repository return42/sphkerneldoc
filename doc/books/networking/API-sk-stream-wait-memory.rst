.. -*- coding: utf-8; mode: rst -*-

.. _API-sk-stream-wait-memory:

=====================
sk_stream_wait_memory
=====================

*man sk_stream_wait_memory(9)*

*4.6.0-rc5*

Wait for more memory for a socket


Synopsis
========

.. c:function:: int sk_stream_wait_memory( struct sock * sk, long * timeo_p )

Arguments
=========

``sk``
    socket to wait for memory

``timeo_p``
    for how long


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
