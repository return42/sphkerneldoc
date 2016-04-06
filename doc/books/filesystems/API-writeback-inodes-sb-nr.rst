
.. _API-writeback-inodes-sb-nr:

======================
writeback_inodes_sb_nr
======================

*man writeback_inodes_sb_nr(9)*

*4.6.0-rc1*

writeback dirty inodes from given super_block


Synopsis
========

.. c:function:: void writeback_inodes_sb_nr( struct super_block * sb, unsigned long nr, enum wb_reason reason )

Arguments
=========

``sb``
    the superblock

``nr``
    the number of pages to write

``reason``
    reason why some writeback work initiated


Description
===========

Start writeback on some inodes on this super_block. No guarantees are made on how many (if any) will be written, and this function does not wait for IO completion of submitted IO.
