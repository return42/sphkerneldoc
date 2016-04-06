
.. _API-relay-mmap-buf:

==============
relay_mmap_buf
==============

*man relay_mmap_buf(9)*

*4.6.0-rc1*

mmap channel buffer to process address space


Synopsis
========

.. c:function:: int relay_mmap_buf( struct rchan_buf * buf, struct vm_area_struct * vma )

Arguments
=========

``buf``
    relay channel buffer

``vma``
    vm_area_struct describing memory to be mapped


Description
===========

Returns 0 if ok, negative on error

Caller should already have grabbed mmap_sem.
