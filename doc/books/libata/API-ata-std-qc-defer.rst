.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-std-qc-defer:

================
ata_std_qc_defer
================

*man ata_std_qc_defer(9)*

*4.6.0-rc5*

Check whether a qc needs to be deferred


Synopsis
========

.. c:function:: int ata_std_qc_defer( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    ATA command in question


Description
===========

Non-NCQ commands cannot run with any other command, NCQ or not. As upper
layer only knows the queue depth, we are responsible for maintaining
exclusion. This function checks whether a new command ``qc`` can be
issued.


LOCKING
=======

spin_lock_irqsave(host lock)


RETURNS
=======

ATA_DEFER_* if deferring is needed, 0 otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
