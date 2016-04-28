.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-alloc-frag:

=================
netdev_alloc_frag
=================

*man netdev_alloc_frag(9)*

*4.6.0-rc5*

allocate a page fragment


Synopsis
========

.. c:function:: void * netdev_alloc_frag( unsigned int fragsz )

Arguments
=========

``fragsz``
    fragment size


Description
===========

Allocates a frag from a page for receive buffer. Uses GFP_ATOMIC
allocations.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
