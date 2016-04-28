.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-sg-clean:

============
ata_sg_clean
============

*man ata_sg_clean(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
