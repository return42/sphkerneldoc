.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-adapter-dispose:

===================
mpt_adapter_dispose
===================

*man mpt_adapter_dispose(9)*

*4.6.0-rc5*

Free all resources associated with an MPT adapter


Synopsis
========

.. c:function:: void mpt_adapter_dispose( MPT_ADAPTER * ioc )

Arguments
=========

``ioc``
    Pointer to MPT adapter structure


Description
===========

This routine unregisters h/w resources and frees all alloc'd memory
associated with a MPT adapter structure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
