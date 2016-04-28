.. -*- coding: utf-8; mode: rst -*-

.. _API-sq-unmap:

========
sq_unmap
========

*man sq_unmap(9)*

*4.6.0-rc5*

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

Unmaps the store queue allocation ``map`` that was previously created by
``sq_remap``. Also frees up the pte that was previously inserted into
the kernel page table and discards the UTLB translation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
