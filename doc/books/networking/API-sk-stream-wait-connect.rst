
.. _API-sk-stream-wait-connect:

======================
sk_stream_wait_connect
======================

*man sk_stream_wait_connect(9)*

*4.6.0-rc1*

Wait for a socket to get into the connected state


Synopsis
========

.. c:function:: int sk_stream_wait_connect( struct sock * sk, long * timeo_p )

Arguments
=========

``sk``
    sock to wait on

``timeo_p``
    for how long to wait


Description
===========

Must be called with the socket locked.
