
.. _API-sb-start-pagefault:

==================
sb_start_pagefault
==================

*man sb_start_pagefault(9)*

*4.6.0-rc1*

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

When a process starts handling write page fault, it should embed the operation into ``sb_start_pagefault`` - ``sb_end_pagefault`` pair to get exclusion against file system
freezing. This is needed since the page fault is going to dirty a page. This function increments number of running page faults preventing freezing. If the file system is already
frozen, the function waits until the file system is thawed.

Since page fault freeze protection behaves as a lock, users have to preserve ordering of freeze protection and other filesystem locks. It is advised to put ``sb_start_pagefault``
close to mmap_sem in lock ordering. Page fault


handling code implies lock dependency
=====================================

mmap_sem -> sb_start_pagefault
