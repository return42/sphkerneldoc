
.. _API-try-to-writeback-inodes-sb-nr:

=============================
try_to_writeback_inodes_sb_nr
=============================

*man try_to_writeback_inodes_sb_nr(9)*

*4.6.0-rc1*

try to start writeback if none underway


Synopsis
========

.. c:function:: bool try_to_writeback_inodes_sb_nr( struct super_block * sb, unsigned long nr, enum wb_reason reason )

Arguments
=========

``sb``
    the superblock

``nr``
    the number of pages to write

``reason``
    the reason of writeback


Description
===========

Invoke writeback_inodes_sb_nr if no writeback is currently underway. Returns 1 if writeback was started, 0 if not.
