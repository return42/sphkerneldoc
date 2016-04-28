.. -*- coding: utf-8; mode: rst -*-

.. _API-vmap:

====
vmap
====

*man vmap(9)*

*4.6.0-rc5*

map an array of pages into virtually contiguous space


Synopsis
========

.. c:function:: void * vmap( struct page ** pages, unsigned int count, unsigned long flags, pgprot_t prot )

Arguments
=========

``pages``
    array of page pointers

``count``
    number of pages to map

``flags``
    vm_area->flags

``prot``
    page protection for the mapping


Description
===========

Maps ``count`` pages from ``pages`` into contiguous kernel virtual
space.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
