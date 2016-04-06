
.. _API-pagecache-isize-extended:

========================
pagecache_isize_extended
========================

*man pagecache_isize_extended(9)*

*4.6.0-rc1*

update pagecache after extension of i_size


Synopsis
========

.. c:function:: void pagecache_isize_extended( struct inode * inode, loff_t from, loff_t to )

Arguments
=========

``inode``
    inode for which i_size was extended

``from``
    original inode size

``to``
    new inode size


Description
===========

Handle extension of inode size either caused by extending truncate or by write starting after current i_size. We mark the page straddling current i_size RO so that
``page_mkwrite`` is called on the nearest write access to the page. This way filesystem can be sure that ``page_mkwrite`` is called on the page before user writes to the page via
mmap after the i_size has been changed.

The function must be called after i_size is updated so that page fault coming after we unlock the page will already see the new i_size. The function must be called while we still
hold i_mutex - this not only makes sure i_size is stable but also that userspace cannot observe new i_size value before we are prepared to store mmap writes at new inode size.
