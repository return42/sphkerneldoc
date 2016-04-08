
.. _API-ata-qc-issue:

============
ata_qc_issue
============

*man ata_qc_issue(9)*

*4.6.0-rc1*

issue taskfile to device


Synopsis
========

.. c:function:: void ata_qc_issue( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    command to issue to device


Description
===========

Prepare an ATA command to submission to device. This includes mapping the data into a DMA-able area, filling in the S/G table, and finally writing the taskfile to hardware,
starting the command.


LOCKING
=======

spin_lock_irqsave(host lock)
