.. -*- coding: utf-8; mode: rst -*-

.. _API-get-pfnblock-flags-mask:

=======================
get_pfnblock_flags_mask
=======================

*man get_pfnblock_flags_mask(9)*

*4.6.0-rc5*

Return the requested group of flags for the pageblock_nr_pages block
of pages


Synopsis
========

.. c:function:: unsigned long get_pfnblock_flags_mask( struct page * page, unsigned long pfn, unsigned long end_bitidx, unsigned long mask )

Arguments
=========

``page``
    The page within the block of interest

``pfn``
    The target page frame number

``end_bitidx``
    The last bit of interest to retrieve

``mask``
    mask of bits that the caller is interested in


Return
======

pageblock_bits flags


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
