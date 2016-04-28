.. -*- coding: utf-8; mode: rst -*-

.. _API-sk-stream-wait-connect:

======================
sk_stream_wait_connect
======================

*man sk_stream_wait_connect(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
