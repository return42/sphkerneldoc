.. -*- coding: utf-8; mode: rst -*-

.. _API-file-update-time:

================
file_update_time
================

*man file_update_time(9)*

*4.6.0-rc5*

update mtime and ctime time


Synopsis
========

.. c:function:: int file_update_time( struct file * file )

Arguments
=========

``file``
    file accessed


Description
===========

Update the mtime and ctime members of an inode and mark the inode for
writeback. Note that this function is meant exclusively for usage in the
file write path of filesystems, and filesystems may choose to explicitly
ignore update via this function with the S_NOCMTIME inode flag, e.g.
for network filesystem where these timestamps are handled by the server.
This can return an error for file systems who need to allocate space in
order to update an inode.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
