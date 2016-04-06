
.. _API-relay-file-open:

===============
relay_file_open
===============

*man relay_file_open(9)*

*4.6.0-rc1*

open file op for relay files


Synopsis
========

.. c:function:: int relay_file_open( struct inode * inode, struct file * filp )

Arguments
=========

``inode``
    the inode

``filp``
    the file


Description
===========

Increments the channel buffer refcount.
