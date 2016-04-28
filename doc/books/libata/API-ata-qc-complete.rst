.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-qc-complete:

===============
ata_qc_complete
===============

*man ata_qc_complete(9)*

*4.6.0-rc5*

Complete an active ATA command


Synopsis
========

.. c:function:: void ata_qc_complete( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    Command to complete


Description
===========

Indicate to the mid and upper layers that an ATA command has completed,
with either an ok or not-ok status.

Refrain from calling this function multiple times when successfully
completing multiple NCQ commands. ``ata_qc_complete_multiple`` should be
used instead, which will properly update IRQ expect state.


LOCKING
=======

spin_lock_irqsave(host lock)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
