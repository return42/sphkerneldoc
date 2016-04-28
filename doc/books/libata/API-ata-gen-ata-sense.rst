.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-gen-ata-sense:

=================
ata_gen_ata_sense
=================

*man ata_gen_ata_sense(9)*

*4.6.0-rc5*

generate a SCSI fixed sense block


Synopsis
========

.. c:function:: void ata_gen_ata_sense( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    Command that we are erroring out


Description
===========

Generate sense block for a failed ATA command ``qc``. Descriptor format
is used to accommodate LBA48 block address.


LOCKING
=======

None.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
