
.. _API-mpt-alloc-fw-memory:

===================
mpt_alloc_fw_memory
===================

*man mpt_alloc_fw_memory(9)*

*4.6.0-rc1*

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

If memory has already been allocated, the same (cached) value is returned.

Return 0 if successful, or non-zero for failure
