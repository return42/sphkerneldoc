.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-to-sense-error:

==================
ata_to_sense_error
==================

*man ata_to_sense_error(9)*

*4.6.0-rc5*

convert ATA error to SCSI error


Synopsis
========

.. c:function:: void ata_to_sense_error( unsigned id, u8 drv_stat, u8 drv_err, u8 * sk, u8 * asc, u8 * ascq, int verbose )

Arguments
=========

``id``
    ATA device number

``drv_stat``
    value contained in ATA status register

``drv_err``
    value contained in ATA error register

``sk``
    the sense key we'll fill out

``asc``
    the additional sense code we'll fill out

``ascq``
    the additional sense code qualifier we'll fill out

``verbose``
    be verbose


Description
===========

Converts an ATA error into a SCSI error. Fill out pointers to SK, ASC,
and ASCQ bytes for later use in fixed or descriptor format sense blocks.


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
