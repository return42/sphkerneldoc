
.. _API-truncate-setsize:

================
truncate_setsize
================

*man truncate_setsize(9)*

*4.6.0-rc1*

update inode and pagecache for a new file size


Synopsis
========

.. c:function:: void truncate_setsize( struct inode * inode, loff_t newsize )

Arguments
=========

``inode``
    inode

``newsize``
    new file size


Description
===========

truncate_setsize updates i_size and performs pagecache truncation (if necessary) to ``newsize``. It will be typically be called from the filesystem's setattr function when
ATTR_SIZE is passed in.

Must be called with a lock serializing truncates and writes (generally i_mutex but e.g. xfs uses a different lock) and before all filesystem specific block truncation has been
performed.
