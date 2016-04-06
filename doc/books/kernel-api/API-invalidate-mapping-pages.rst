
.. _API-invalidate-mapping-pages:

========================
invalidate_mapping_pages
========================

*man invalidate_mapping_pages(9)*

*4.6.0-rc1*

Invalidate all the unlocked pages of one inode


Synopsis
========

.. c:function:: unsigned long invalidate_mapping_pages( struct address_space * mapping, pgoff_t start, pgoff_t end )

Arguments
=========

``mapping``
    the address_space which holds the pages to invalidate

``start``
    the offset 'from' which to invalidate

``end``
    the offset 'to' which to invalidate (inclusive)


Description
===========

This function only removes the unlocked pages, if you want to remove all the pages of one inode, you must call truncate_inode_pages.

``invalidate_mapping_pages`` will not block on IO activity. It will not invalidate pages which are dirty, locked, under writeback or mapped into pagetables.
