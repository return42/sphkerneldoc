
.. _API-ata-tf-to-fis:

=============
ata_tf_to_fis
=============

*man ata_tf_to_fis(9)*

*4.6.0-rc1*

Convert ATA taskfile to SATA FIS structure


Synopsis
========

.. c:function:: void ata_tf_to_fis( const struct ata_taskfile * tf, u8 pmp, int is_cmd, u8 * fis )

Arguments
=========

``tf``
    Taskfile to convert

``pmp``
    Port multiplier port

``is_cmd``
    This FIS is for command

``fis``
    Buffer into which data will output


Description
===========

Converts a standard ATA taskfile to a Serial ATA FIS structure (Register - Host to Device).


LOCKING
=======

Inherited from caller.
