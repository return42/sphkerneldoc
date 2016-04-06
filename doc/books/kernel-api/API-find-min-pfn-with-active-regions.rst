
.. _API-find-min-pfn-with-active-regions:

================================
find_min_pfn_with_active_regions
================================

*man find_min_pfn_with_active_regions(9)*

*4.6.0-rc1*

Find the minimum PFN registered


Synopsis
========

.. c:function:: unsigned long find_min_pfn_with_active_regions( void )

Arguments
=========

``void``
    no arguments


Description
===========

It returns the minimum PFN based on information provided via ``memblock_set_node``.
