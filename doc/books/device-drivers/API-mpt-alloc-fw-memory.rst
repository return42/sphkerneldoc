.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-alloc-fw-memory:

===================
mpt_alloc_fw_memory
===================

*man mpt_alloc_fw_memory(9)*

*4.6.0-rc5*

allocate firmware memory


Synopsis
========

.. c:function:: int mpt_alloc_fw_memory( MPT_ADAPTER * ioc, int size )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``size``
    total FW bytes


Description
===========

If memory has already been allocated, the same (cached) value is
returned.

Return 0 if successful, or non-zero for failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
