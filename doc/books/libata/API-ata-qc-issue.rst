.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-qc-issue:

============
ata_qc_issue
============

*man ata_qc_issue(9)*

*4.6.0-rc5*

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

Prepare an ATA command to submission to device. This includes mapping
the data into a DMA-able area, filling in the S/G table, and finally
writing the taskfile to hardware, starting the command.


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
