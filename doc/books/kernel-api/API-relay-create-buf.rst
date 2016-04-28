.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-create-buf:

================
relay_create_buf
================

*man relay_create_buf(9)*

*4.6.0-rc5*

allocate and initialize a channel buffer


Synopsis
========

.. c:function:: struct rchan_buf * relay_create_buf( struct rchan * chan )

Arguments
=========

``chan``
    the relay channel


Description
===========

Returns channel buffer if successful, ``NULL`` otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
