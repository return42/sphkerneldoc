
.. _API-ata-tf-from-fis:

===============
ata_tf_from_fis
===============

*man ata_tf_from_fis(9)*

*4.6.0-rc1*

Convert SATA FIS to ATA taskfile


Synopsis
========

.. c:function:: void ata_tf_from_fis( const u8 * fis, struct ata_taskfile * tf )

Arguments
=========

``fis``
    Buffer from which data will be input

``tf``
    Taskfile to output


Description
===========

Converts a serial ATA FIS structure to a standard ATA taskfile.


LOCKING
=======

Inherited from caller.
