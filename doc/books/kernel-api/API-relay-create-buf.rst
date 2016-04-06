
.. _API-relay-create-buf:

================
relay_create_buf
================

*man relay_create_buf(9)*

*4.6.0-rc1*

allocate and initialize a channel buffer


Synopsis
========

.. c:function:: struct rchan_buf ⋆ relay_create_buf( struct rchan * chan )

Arguments
=========

``chan``
    the relay channel


Description
===========

Returns channel buffer if successful, ``NULL`` otherwise.
