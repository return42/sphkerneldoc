.. -*- coding: utf-8; mode: rst -*-

.. _API-follow-pfn:

==========
follow_pfn
==========

*man follow_pfn(9)*

*4.6.0-rc5*

look up PFN at a user virtual address


Synopsis
========

.. c:function:: int follow_pfn( struct vm_area_struct * vma, unsigned long address, unsigned long * pfn )

Arguments
=========

``vma``
    memory mapping

``address``
    user virtual address

``pfn``
    location to store found PFN


Description
===========

Only IO mappings and raw PFN mappings are allowed.

Returns zero and the pfn at ``pfn`` on success, -ve otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
