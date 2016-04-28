.. -*- coding: utf-8; mode: rst -*-

.. _API-mptspi-initTarget:

=================
mptspi_initTarget
=================

*man mptspi_initTarget(9)*

*4.6.0-rc5*

Target, LUN alloc/free functionality.


Synopsis
========

.. c:function:: void mptspi_initTarget( MPT_SCSI_HOST * hd, VirtTarget * vtarget, struct scsi_device * sdev )

Arguments
=========

``hd``
    Pointer to MPT_SCSI_HOST structure

``vtarget``
    per target private data

``sdev``
    SCSI device


NOTE
====

It's only SAFE to call this routine if data points to sane & valid
STANDARD INQUIRY data!

Allocate and initialize memory for this target. Save inquiry data.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
