.. -*- coding: utf-8; mode: rst -*-

.. _API-absent-pages-in-range:

=====================
absent_pages_in_range
=====================

*man absent_pages_in_range(9)*

*4.6.0-rc5*

Return number of page frames in holes within a range


Synopsis
========

.. c:function:: unsigned long absent_pages_in_range( unsigned long start_pfn, unsigned long end_pfn )

Arguments
=========

``start_pfn``
    The start PFN to start searching for holes

``end_pfn``
    The end PFN to stop searching for holes


Description
===========

It returns the number of pages frames in memory holes within a range.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
