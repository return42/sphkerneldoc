.. -*- coding: utf-8; mode: rst -*-

.. _API-fence-wait:

==========
fence_wait
==========

*man fence_wait(9)*

*4.6.0-rc5*

sleep until the fence gets signaled


Synopsis
========

.. c:function:: signed long fence_wait( struct fence * fence, bool intr )

Arguments
=========

``fence``
    [in] the fence to wait on

``intr``
    [in] if true, do an interruptible wait


Description
===========

This function will return -ERESTARTSYS if interrupted by a signal, or 0
if the fence was signaled. Other error values may be returned on custom
implementations.

Performs a synchronous wait on this fence. It is assumed the caller
directly or indirectly holds a reference to the fence, otherwise the
fence might be freed before return, resulting in undefined behavior.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
