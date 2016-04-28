.. -*- coding: utf-8; mode: rst -*-

.. _API-writeback-inodes-sb:

===================
writeback_inodes_sb
===================

*man writeback_inodes_sb(9)*

*4.6.0-rc5*

writeback dirty inodes from given super_block


Synopsis
========

.. c:function:: void writeback_inodes_sb( struct super_block * sb, enum wb_reason reason )

Arguments
=========

``sb``
    the superblock

``reason``
    reason why some writeback work was initiated


Description
===========

Start writeback on some inodes on this super_block. No guarantees are
made on how many (if any) will be written, and this function does not
wait for IO completion of submitted IO.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
