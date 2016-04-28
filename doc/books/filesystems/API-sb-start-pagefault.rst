.. -*- coding: utf-8; mode: rst -*-

.. _API-sb-start-pagefault:

==================
sb_start_pagefault
==================

*man sb_start_pagefault(9)*

*4.6.0-rc5*

get write access to a superblock from a page fault


Synopsis
========

.. c:function:: void sb_start_pagefault( struct super_block * sb )

Arguments
=========

``sb``
    the super we write to


Description
===========

When a process starts handling write page fault, it should embed the
operation into ``sb_start_pagefault`` - ``sb_end_pagefault`` pair to get
exclusion against file system freezing. This is needed since the page
fault is going to dirty a page. This function increments number of
running page faults preventing freezing. If the file system is already
frozen, the function waits until the file system is thawed.

Since page fault freeze protection behaves as a lock, users have to
preserve ordering of freeze protection and other filesystem locks. It is
advised to put ``sb_start_pagefault`` close to mmap_sem in lock
ordering. Page fault


handling code implies lock dependency
=====================================

mmap_sem -> sb_start_pagefault


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
