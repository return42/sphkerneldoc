
.. _API-ata-tf-read-block:

=================
ata_tf_read_block
=================

*man ata_tf_read_block(9)*

*4.6.0-rc1*

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

Read block address from ``tf``. This function can handle all three address formats - LBA, LBA48 and CHS. tf->protocol and flags select the address format to use.


RETURNS
=======

Block address read from ``tf``.
