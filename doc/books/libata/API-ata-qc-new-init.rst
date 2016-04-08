
.. _API-ata-qc-new-init:

===============
ata_qc_new_init
===============

*man ata_qc_new_init(9)*

*4.6.0-rc1*

Request an available ATA command, and initialize it


Synopsis
========

.. c:function:: struct ata_queued_cmd ⋆ ata_qc_new_init( struct ata_device * dev, int tag )

Arguments
=========

``dev``
    Device from whom we request an available command structure

``tag``
    tag


LOCKING
=======

None.
