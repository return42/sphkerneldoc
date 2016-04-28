.. -*- coding: utf-8; mode: rst -*-

.. _API-sb-end-pagefault:

================
sb_end_pagefault
================

*man sb_end_pagefault(9)*

*4.6.0-rc5*

drop write access to a superblock from a page fault


Synopsis
========

.. c:function:: void sb_end_pagefault( struct super_block * sb )

Arguments
=========

``sb``
    the super we wrote to


Description
===========

Decrement number of processes handling write page fault to the
filesystem. Wake up possible waiters wanting to freeze the filesystem.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
