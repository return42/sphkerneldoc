
.. _API-sk-rmem-alloc-get:

=================
sk_rmem_alloc_get
=================

*man sk_rmem_alloc_get(9)*

*4.6.0-rc1*

returns read allocations


Synopsis
========

.. c:function:: int sk_rmem_alloc_get( const struct sock * sk )

Arguments
=========

``sk``
    socket


Description
===========

Returns sk_rmem_alloc
