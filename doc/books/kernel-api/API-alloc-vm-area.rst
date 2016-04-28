.. -*- coding: utf-8; mode: rst -*-

.. _API-alloc-vm-area:

=============
alloc_vm_area
=============

*man alloc_vm_area(9)*

*4.6.0-rc5*

allocate a range of kernel address space


Synopsis
========

.. c:function:: struct vm_struct * alloc_vm_area( size_t size, pte_t ** ptes )

Arguments
=========

``size``
    size of the area

``ptes``
    returns the PTEs for the address space


Returns
=======

NULL on failure, vm_struct on success

This function reserves a range of kernel address space, and allocates
pagetables to map that range. No actual mappings are created.

If ``ptes`` is non-NULL, pointers to the PTEs (in init_mm) allocated
for the VM area are returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
