.. -*- coding: utf-8; mode: rst -*-

.. _API-mptspi-is-raid:

==============
mptspi_is_raid
==============

*man mptspi_is_raid(9)*

*4.6.0-rc5*

Determines whether target is belonging to volume


Synopsis
========

.. c:function:: int mptspi_is_raid( struct _MPT_SCSI_HOST * hd, u32 id )

Arguments
=========

``hd``
    Pointer to a SCSI HOST structure

``id``
    target device id


Return
======

non-zero = true zero = false


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
