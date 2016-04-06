
.. _API-set-pfnblock-flags-mask:

=======================
set_pfnblock_flags_mask
=======================

*man set_pfnblock_flags_mask(9)*

*4.6.0-rc1*

Set the requested group of flags for a pageblock_nr_pages block of pages


Synopsis
========

.. c:function:: void set_pfnblock_flags_mask( struct page * page, unsigned long flags, unsigned long pfn, unsigned long end_bitidx, unsigned long mask )

Arguments
=========

``page``
    The page within the block of interest

``flags``
    The flags to set

``pfn``
    The target page frame number

``end_bitidx``
    The last bit of interest

``mask``
    mask of bits that the caller is interested in
