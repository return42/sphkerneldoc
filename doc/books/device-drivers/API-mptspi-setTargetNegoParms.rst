.. -*- coding: utf-8; mode: rst -*-

.. _API-mptspi-setTargetNegoParms:

=========================
mptspi_setTargetNegoParms
=========================

*man mptspi_setTargetNegoParms(9)*

*4.6.0-rc5*

Update the target negotiation parameters


Synopsis
========

.. c:function:: void mptspi_setTargetNegoParms( MPT_SCSI_HOST * hd, VirtTarget * target, struct scsi_device * sdev )

Arguments
=========

``hd``
    Pointer to a SCSI Host Structure

``target``
    per target private data

``sdev``
    SCSI device


Description
===========

Update the target negotiation parameters based on the the Inquiry data,
adapter capabilities, and NVRAM settings.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
