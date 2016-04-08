
.. _API-ata-sg-clean:

============
ata_sg_clean
============

*man ata_sg_clean(9)*

*4.6.0-rc1*

Unmap DMA memory associated with command


Synopsis
========

.. c:function:: void ata_sg_clean( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    Command containing DMA memory to be released


Description
===========

Unmap all mapped DMA memory associated with this command.


LOCKING
=======

spin_lock_irqsave(host lock)
