.. -*- coding: utf-8; mode: rst -*-

.. _API-locks-mandatory-area:

====================
locks_mandatory_area
====================

*man locks_mandatory_area(9)*

*4.6.0-rc5*

Check for a conflicting lock


Synopsis
========

.. c:function:: int locks_mandatory_area( struct inode * inode, struct file * filp, loff_t start, loff_t end, unsigned char type )

Arguments
=========

``inode``
    the file to check

``filp``
    how the file was opened (if it was)

``start``
    first byte in the file to check

``end``
    lastbyte in the file to check

``type``
    ``F_WRLCK`` for a write lock, else ``F_RDLCK``


Description
===========

Searches the inode's list of locks to find any POSIX locks which
conflict.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
