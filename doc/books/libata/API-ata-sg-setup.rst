
.. _API-ata-sg-setup:

============
ata_sg_setup
============

*man ata_sg_setup(9)*

*4.6.0-rc1*

DMA-map the scatter-gather table associated with a command.


Synopsis
========

.. c:function:: int ata_sg_setup( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    Command with scatter-gather table to be mapped.


Description
===========

DMA-map the scatter-gather table associated with queued_cmd ``qc``.


LOCKING
=======

spin_lock_irqsave(host lock)


RETURNS
=======

Zero on success, negative on error.
