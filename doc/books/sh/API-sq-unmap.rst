
.. _API-sq-unmap:

========
sq_unmap
========

*man sq_unmap(9)*

*4.6.0-rc1*

Unmap a Store Queue allocation


Synopsis
========

.. c:function:: void sq_unmap( unsigned long vaddr )

Arguments
=========

``vaddr``
    Pre-allocated Store Queue mapping.


Description
===========

Unmaps the store queue allocation ``map`` that was previously created by ``sq_remap``. Also frees up the pte that was previously inserted into the kernel page table and discards
the UTLB translation.
