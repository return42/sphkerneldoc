
.. _API-sget:

====
sget
====

*man sget(9)*

*4.6.0-rc1*

find or create a superblock


Synopsis
========

.. c:function:: struct super_block ⋆ sget( struct file_system_type * type, int (*test) struct super_block *,void *, int (*set) struct super_block *,void *, int flags, void * data )

Arguments
=========

``type``
    filesystem type superblock should belong to

``test``
    comparison callback

``set``
    setup callback

``flags``
    mount flags

``data``
    argument to each of them
