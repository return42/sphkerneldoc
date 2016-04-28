.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc-rcu-alloc:

=============
ipc_rcu_alloc
=============

*man ipc_rcu_alloc(9)*

*4.6.0-rc5*

allocate ipc and rcu space


Synopsis
========

.. c:function:: void * ipc_rcu_alloc( int size )

Arguments
=========

``size``
    size desired


Description
===========

Allocate memory for the rcu header structure + the object. Returns the
pointer to the object or NULL upon failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
