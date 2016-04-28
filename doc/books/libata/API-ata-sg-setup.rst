.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-sg-setup:

============
ata_sg_setup
============

*man ata_sg_setup(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
