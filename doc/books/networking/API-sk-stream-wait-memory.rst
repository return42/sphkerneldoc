
.. _API-sk-stream-wait-memory:

=====================
sk_stream_wait_memory
=====================

*man sk_stream_wait_memory(9)*

*4.6.0-rc1*

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
