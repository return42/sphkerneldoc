
.. _API-sk-wmem-alloc-get:

=================
sk_wmem_alloc_get
=================

*man sk_wmem_alloc_get(9)*

*4.6.0-rc1*

returns write allocations


Synopsis
========

.. c:function:: int sk_wmem_alloc_get( const struct sock * sk )

Arguments
=========

``sk``
    socket


Description
===========

Returns sk_wmem_alloc minus initial offset of one
