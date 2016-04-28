.. -*- coding: utf-8; mode: rst -*-

.. _API-filemap-write-and-wait-range:

============================
filemap_write_and_wait_range
============================

*man filemap_write_and_wait_range(9)*

*4.6.0-rc5*

write out & wait on a file range


Synopsis
========

.. c:function:: int filemap_write_and_wait_range( struct address_space * mapping, loff_t lstart, loff_t lend )

Arguments
=========

``mapping``
    the address_space for the pages

``lstart``
    offset in bytes where the range starts

``lend``
    offset in bytes where the range ends (inclusive)


Description
===========

Write out and wait upon file offsets lstart->lend, inclusive.

Note that `lend' is inclusive (describes the last byte to be written)
so that this function can be used to write to the very end-of-file (end
= -1).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
