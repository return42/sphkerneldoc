
.. _API-sb-end-intwrite:

===============
sb_end_intwrite
===============

*man sb_end_intwrite(9)*

*4.6.0-rc1*

drop write access to a superblock for internal fs purposes


Synopsis
========

.. c:function:: void sb_end_intwrite( struct super_block * sb )

Arguments
=========

``sb``
    the super we wrote to


Description
===========

Decrement fs-internal number of writers to the filesystem. Wake up possible waiters wanting to freeze the filesystem.
