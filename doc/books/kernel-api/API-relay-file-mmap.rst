.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-file-mmap:

===============
relay_file_mmap
===============

*man relay_file_mmap(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
