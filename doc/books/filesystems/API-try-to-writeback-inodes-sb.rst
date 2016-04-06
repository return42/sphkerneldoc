
.. _API-try-to-writeback-inodes-sb:

==========================
try_to_writeback_inodes_sb
==========================

*man try_to_writeback_inodes_sb(9)*

*4.6.0-rc1*

try to start writeback if none underway


Synopsis
========

.. c:function:: bool try_to_writeback_inodes_sb( struct super_block * sb, enum wb_reason reason )

Arguments
=========

``sb``
    the superblock

``reason``
    reason why some writeback work was initiated


Description
===========

Implement by ``try_to_writeback_inodes_sb_nr`` Returns 1 if writeback was started, 0 if not.
