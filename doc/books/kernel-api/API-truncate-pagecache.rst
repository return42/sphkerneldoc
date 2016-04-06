
.. _API-truncate-pagecache:

==================
truncate_pagecache
==================

*man truncate_pagecache(9)*

*4.6.0-rc1*

unmap and remove pagecache that has been truncated


Synopsis
========

.. c:function:: void truncate_pagecache( struct inode * inode, loff_t newsize )

Arguments
=========

``inode``
    inode

``newsize``
    new file size


Description
===========

inode's new i_size must already be written before truncate_pagecache is called.

This function should typically be called before the filesystem releases resources associated with the freed range (eg. deallocates blocks). This way, pagecache will always stay
logically coherent with on-disk format, and the filesystem would not have to deal with situations such as writepage being called for a page that has already had its underlying
blocks deallocated.
