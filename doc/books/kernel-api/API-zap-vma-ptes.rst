
.. _API-zap-vma-ptes:

============
zap_vma_ptes
============

*man zap_vma_ptes(9)*

*4.6.0-rc1*

remove ptes mapping the vma


Synopsis
========

.. c:function:: int zap_vma_ptes( struct vm_area_struct * vma, unsigned long address, unsigned long size )

Arguments
=========

``vma``
    vm_area_struct holding ptes to be zapped

``address``
    starting address of pages to zap

``size``
    number of bytes to zap


Description
===========

This function only unmaps ptes assigned to VM_PFNMAP vmas.

The entire address range must be fully contained within the vma.

Returns 0 if successful.
