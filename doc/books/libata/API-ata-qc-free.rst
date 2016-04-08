
.. _API-ata-qc-free:

===========
ata_qc_free
===========

*man ata_qc_free(9)*

*4.6.0-rc1*

free unused ata_queued_cmd


Synopsis
========

.. c:function:: void ata_qc_free( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    Command to complete


Description
===========

Designed to free unused ata_queued_cmd object in case something prevents using it.


LOCKING
=======

spin_lock_irqsave(host lock)
