
.. _API-follow-pfn:

==========
follow_pfn
==========

*man follow_pfn(9)*

*4.6.0-rc1*

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
