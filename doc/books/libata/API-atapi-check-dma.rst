
.. _API-atapi-check-dma:

===============
atapi_check_dma
===============

*man atapi_check_dma(9)*

*4.6.0-rc1*

Check whether ATAPI DMA can be supported


Synopsis
========

.. c:function:: int atapi_check_dma( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    Metadata associated with taskfile to check


Description
===========

Allow low-level driver to filter ATA PACKET commands, returning a status indicating whether or not it is OK to use DMA for the supplied PACKET command.


LOCKING
=======

spin_lock_irqsave(host lock)


RETURNS
=======

0 when ATAPI DMA can be used nonzero otherwise
