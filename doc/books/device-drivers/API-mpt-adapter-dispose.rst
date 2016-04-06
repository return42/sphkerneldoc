
.. _API-mpt-adapter-dispose:

===================
mpt_adapter_dispose
===================

*man mpt_adapter_dispose(9)*

*4.6.0-rc1*

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

This routine unregisters h/w resources and frees all alloc'd memory associated with a MPT adapter structure.
