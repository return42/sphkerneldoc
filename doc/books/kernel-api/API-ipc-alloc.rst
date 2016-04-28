.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc-alloc:

=========
ipc_alloc
=========

*man ipc_alloc(9)*

*4.6.0-rc5*

allocate ipc space


Synopsis
========

.. c:function:: void * ipc_alloc( int size )

Arguments
=========

``size``
    size desired


Description
===========

Allocate memory from the appropriate pools and return a pointer to it.
NULL is returned if the allocation fails


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
