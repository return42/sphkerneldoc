.. -*- coding: utf-8; mode: rst -*-

.. _API-mptscsih-synchronize-cache:

==========================
mptscsih_synchronize_cache
==========================

*man mptscsih_synchronize_cache(9)*

*4.6.0-rc5*

Send SYNCHRONIZE_CACHE to all disks.


Synopsis
========

.. c:function:: void mptscsih_synchronize_cache( MPT_SCSI_HOST * hd, VirtDevice * vdevice )

Arguments
=========

``hd``
    Pointer to a SCSI HOST structure

``vdevice``
    virtual target device


Description
===========

Uses the ISR, but with special processing. MUST be single-threaded.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
