.. -*- coding: utf-8; mode: rst -*-

.. _API-vm-map-ram:

==========
vm_map_ram
==========

*man vm_map_ram(9)*

*4.6.0-rc5*

map pages linearly into kernel virtual address (vmalloc space)


Synopsis
========

.. c:function:: void * vm_map_ram( struct page ** pages, unsigned int count, int node, pgprot_t prot )

Arguments
=========

``pages``
    an array of pointers to the pages to be mapped

``count``
    number of pages

``node``
    prefer to allocate data structures on this node

``prot``
    memory protection to use. PAGE_KERNEL for regular RAM


Description
===========

If you use this function for less than VMAP_MAX_ALLOC pages, it could
be faster than vmap so it's good. But if you mix long-life and
short-life objects with ``vm_map_ram``, it could consume lots of address
space through fragmentation (especially on a 32bit machine). You could
see failures in the end. Please use this function for short-lived
objects.


Returns
=======

a pointer to the address that has been mapped, or ``NULL`` on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
