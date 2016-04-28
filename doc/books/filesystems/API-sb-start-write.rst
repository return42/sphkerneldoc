.. -*- coding: utf-8; mode: rst -*-

.. _API-sb-start-write:

==============
sb_start_write
==============

*man sb_start_write(9)*

*4.6.0-rc5*

get write access to a superblock


Synopsis
========

.. c:function:: void sb_start_write( struct super_block * sb )

Arguments
=========

``sb``
    the super we write to


Description
===========

When a process wants to write data or metadata to a file system (i.e.
dirty a page or an inode), it should embed the operation in a
``sb_start_write`` - ``sb_end_write`` pair to get exclusion against file
system freezing. This function increments number of writers preventing
freezing. If the file system is already frozen, the function waits until
the file system is thawed.

Since freeze protection behaves as a lock, users have to preserve
ordering of freeze protection and other filesystem locks. Generally,
freeze protection should be the outermost lock. In particular, we have:

sb_start_write -> i_mutex (write path, truncate, directory ops, ...)
-> s_umount (freeze_super, thaw_super)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
