
.. _API-truncate-inode-pages-range:

==========================
truncate_inode_pages_range
==========================

*man truncate_inode_pages_range(9)*

*4.6.0-rc1*

truncate range of pages specified by start & end byte offsets


Synopsis
========

.. c:function:: void truncate_inode_pages_range( struct address_space * mapping, loff_t lstart, loff_t lend )

Arguments
=========

``mapping``
    mapping to truncate

``lstart``
    offset from which to truncate

``lend``
    offset to which to truncate (inclusive)


Description
===========

Truncate the page cache, removing the pages that are between specified offsets (and zeroing out partial pages if lstart or lend + 1 is not page aligned).

Truncate takes two passes - the first pass is nonblocking. It will not block on page locks and it will not block on writeback. The second pass will wait. This is to prevent as much
IO as possible in the affected region. The first pass will remove most pages, so the search cost of the second pass is low.

We pass down the cache-hot hint to the page freeing code. Even if the mapping is large, it is probably the case that the final pages are the most recently touched, and freeing
happens in ascending file offset order.

Note that since ->``invalidatepage`` accepts range to invalidate truncate_inode_pages_range is able to handle cases where lend + 1 is not page aligned properly.
