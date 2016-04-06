
.. _API-relay-file-mmap:

===============
relay_file_mmap
===============

*man relay_file_mmap(9)*

*4.6.0-rc1*

mmap file op for relay files


Synopsis
========

.. c:function:: int relay_file_mmap( struct file * filp, struct vm_area_struct * vma )

Arguments
=========

``filp``
    the file

``vma``
    the vma describing what to map


Description
===========

Calls upon ``relay_mmap_buf`` to map the file into user space.
