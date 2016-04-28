.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-alloc-sdev:

===============
scsi_alloc_sdev
===============

*man scsi_alloc_sdev(9)*

*4.6.0-rc5*

allocate and setup a scsi_Device


Synopsis
========

.. c:function:: struct scsi_device * scsi_alloc_sdev( struct scsi_target * starget, u64 lun, void * hostdata )

Arguments
=========

``starget``
    which target to allocate a ``scsi_device`` for

``lun``
    which lun

``hostdata``
    usually NULL and set by ->slave_alloc instead


Description
===========

Allocate, initialize for io, and return a pointer to a scsi_Device.
Stores the ``shost``, ``channel``, ``id``, and ``lun`` in the
scsi_Device, and adds scsi_Device to the appropriate list.


Return value
============

scsi_Device pointer, or NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
