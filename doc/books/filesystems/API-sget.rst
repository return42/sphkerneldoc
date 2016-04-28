.. -*- coding: utf-8; mode: rst -*-

.. _API-sget:

====
sget
====

*man sget(9)*

*4.6.0-rc5*

find or create a superblock


Synopsis
========

.. c:function:: struct super_block * sget( struct file_system_type * type, int (*test) struct super_block *,void *, int (*set) struct super_block *,void *, int flags, void * data )

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
