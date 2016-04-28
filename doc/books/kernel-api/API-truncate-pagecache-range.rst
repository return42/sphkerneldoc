.. -*- coding: utf-8; mode: rst -*-

.. _API-truncate-pagecache-range:

========================
truncate_pagecache_range
========================

*man truncate_pagecache_range(9)*

*4.6.0-rc5*

unmap and remove pagecache that is hole-punched


Synopsis
========

.. c:function:: void truncate_pagecache_range( struct inode * inode, loff_t lstart, loff_t lend )

Arguments
=========

``inode``
    inode

``lstart``
    offset of beginning of hole

``lend``
    offset of last byte of hole


Description
===========

This function should typically be called before the filesystem releases
resources associated with the freed range (eg. deallocates blocks). This
way, pagecache will always stay logically coherent with on-disk format,
and the filesystem would not have to deal with situations such as
writepage being called for a page that has already had its underlying
blocks deallocated.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
