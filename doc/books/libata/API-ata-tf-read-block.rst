.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-tf-read-block:

=================
ata_tf_read_block
=================

*man ata_tf_read_block(9)*

*4.6.0-rc5*

Read block address from ATA taskfile


Synopsis
========

.. c:function:: u64 ata_tf_read_block( struct ata_taskfile * tf, struct ata_device * dev )

Arguments
=========

``tf``
    ATA taskfile of interest

``dev``
    ATA device ``tf`` belongs to


LOCKING
=======

None.

Read block address from ``tf``. This function can handle all three
address formats - LBA, LBA48 and CHS. tf->protocol and flags select the
address format to use.


RETURNS
=======

Block address read from ``tf``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
