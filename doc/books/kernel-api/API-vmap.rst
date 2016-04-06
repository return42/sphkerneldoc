
.. _API-vmap:

====
vmap
====

*man vmap(9)*

*4.6.0-rc1*

map an array of pages into virtually contiguous space


Synopsis
========

.. c:function:: void ⋆ vmap( struct page ** pages, unsigned int count, unsigned long flags, pgprot_t prot )

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

Maps ``count`` pages from ``pages`` into contiguous kernel virtual space.
