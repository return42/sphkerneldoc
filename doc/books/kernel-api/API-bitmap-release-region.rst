.. -*- coding: utf-8; mode: rst -*-

.. _API-bitmap-release-region:

=====================
bitmap_release_region
=====================

*man bitmap_release_region(9)*

*4.6.0-rc5*

release allocated bitmap region


Synopsis
========

.. c:function:: void bitmap_release_region( unsigned long * bitmap, unsigned int pos, int order )

Arguments
=========

``bitmap``
    array of unsigned longs corresponding to the bitmap

``pos``
    beginning of bit region to release

``order``
    region size (log base 2 of number of bits) to release


Description
===========

This is the complement to ``__bitmap_find_free_region`` and releases the
found region (by clearing it in the bitmap).

No return value.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
