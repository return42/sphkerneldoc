
.. _API-netdev-alloc-frag:

=================
netdev_alloc_frag
=================

*man netdev_alloc_frag(9)*

*4.6.0-rc1*

allocate a page fragment


Synopsis
========

.. c:function:: void ⋆ netdev_alloc_frag( unsigned int fragsz )

Arguments
=========

``fragsz``
    fragment size


Description
===========

Allocates a frag from a page for receive buffer. Uses GFP_ATOMIC allocations.
