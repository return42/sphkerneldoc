.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-init-dev:

=====================
jbd2_journal_init_dev
=====================

*man jbd2_journal_init_dev(9)*

*4.6.0-rc5*

creates and initialises a journal structure


Synopsis
========

.. c:function:: journal_t * jbd2_journal_init_dev( struct block_device * bdev, struct block_device * fs_dev, unsigned long long start, int len, int blocksize )

Arguments
=========

``bdev``
    Block device on which to create the journal

``fs_dev``
    Device which hold journalled filesystem for this journal.

``start``
    Block nr Start of journal.

``len``
    Length of the journal in blocks.

``blocksize``
    blocksize of journalling device


Returns
=======

a newly created journal_t *

jbd2_journal_init_dev creates a journal which maps a fixed contiguous
range of blocks on an arbitrary block device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
